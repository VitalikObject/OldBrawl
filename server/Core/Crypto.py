# -*- coding: utf-8 -*-

import os

from _tweetnacl import (
                            crypto_box_afternm,
                            crypto_box_beforenm,
                            crypto_scalarmult_base,
                            crypto_box_open_afternm,
                            crypto_secretbox,
                            crypto_secretbox_open
                            )
from Core.Nonce import Nonce
from Utils.Helpers import Helpers


class Crypto:

    def __init__(self):
        self.session_key = None
        self.server_key = bytes.fromhex('78BD03628030B86BCF17817DF13A3E9C0E8FD03F06F222A44C40CA70F3ECC748')
        self.client_sk = bytes.fromhex('BB14D6FD2B7C9823EAEDB4338CB7237F61E422D23C4977F74ADA052702C0C62D')
        #testers - BB14D6FD2B7C9823EAEDB4338CB7237F61E422D23C4977F74ADA052702C0C62D
        #dev - 8AD0E78B0AF8DC8D6FD52FE16943F54757ACF369D81FB4CCF5271623B576AF27
        self.client_pk = crypto_scalarmult_base(self.client_sk)
        self.nonce = None
        self.encryptNonce = Nonce(bytes.fromhex(Helpers.randomkey(24)))
        self.decryptNonce = None
        self.s = crypto_box_beforenm(self.server_key, self.client_sk)
        self.shared_en = bytes.fromhex(Helpers.randomkey(32))
        self.ss = None

    def encrypt_client_packet(self, packet_id, payload):
        if packet_id == 10100:
            return payload

        elif packet_id == 10101:
            payload = self.session_key + bytes(self.decryptNonce) + payload
            encrypted = crypto_box_afternm(payload, bytes(self.nonce), self.s)
            return self.client_pk + encrypted

        elif self.decryptNonce is None:
            return payload

        else:
            return crypto_box_afternm(payload, bytes(self.decryptNonce), self.shared_en)

    def decrypt_client_packet(self, packet_id, payload):
        if packet_id in (10100, 10108, 10212):
            return payload

        elif packet_id == 10101:
            if payload[:32] != self.client_pk:
                print('[*] It look like frida didn\'t attached properly to your device since client pk don\'t match with the static one !')
                os._exit(0)

            payload = payload[32:]  # skip the pk since we already know it
            self.nonce = Nonce(clientKey=self.client_pk, serverKey=self.server_key)

            decrypted = crypto_secretbox_open(payload, bytes(self.nonce), self.s)
            self.ss = decrypted[24:48]
            self.decryptNonce = Nonce(decrypted[24:48])

            return decrypted[48:]

        elif self.decryptNonce is None:
            return payload

        else:
            self.decryptNonce.increment()
            decrypted = crypto_secretbox_open(payload, bytes(self.decryptNonce), self.shared_en)
            return decrypted

    def encrypt_server_packet(self, packet_id, payload):
        if packet_id == 20100:
            return payload

        elif packet_id in (20103, 20104):
            nonce = Nonce(self.decryptNonce, self.client_pk, self.server_key)
            payload = bytes(self.encryptNonce) + self.shared_en + payload
            encrypted = crypto_secretbox(payload, bytes(nonce), self.s)

            return encrypted        
            

        else:
            self.encryptNonce.increment()
            encrypted = crypto_secretbox(payload, bytes(self.encryptNonce), self.shared_en)
            return encrypted

    def decrypt_server_packet(self, packet_id, payload):
        if packet_id == 20100:
            self.session_key = payload[-24:]
            return payload

        elif packet_id == 20103 and not self.session_key:
            return payload

        elif packet_id in (20103, 20104):
            nonce = Nonce(self.decryptNonce, self.client_pk, self.server_key)

            decrypted = crypto_box_open_afternm(payload, bytes(nonce), self.s)

            self.encryptNonce = Nonce(decrypted[:24])
            self.shared_en = decrypted[24:56]

            return decrypted[56:]

        else:
            self.encryptNonce.increment()
            return crypto_box_open_afternm(payload, bytes(self.encryptNonce), self.shared_en)