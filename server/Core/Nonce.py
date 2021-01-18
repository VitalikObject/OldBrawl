# -*- coding: utf-8 -*-

from os import urandom

from hashlib import blake2b
from _tweetnacl import crypto_box_NONCEBYTES


class Nonce:

    def __init__(self, nonce=None, clientKey=None, serverKey=None):
        if not clientKey:
            if nonce:
                self._nonce = nonce

            else:
                self._nonce = urandom(crypto_box_NONCEBYTES)

        else:
            b2 = blake2b(digest_size=24)
            if nonce:
                b2.update(bytes(nonce))
            b2.update(bytes(clientKey))
            b2.update(serverKey)
            self._nonce = b2.digest()

    def __bytes__(self):
        return self._nonce

    def __len__(self):
        return len(self._nonce)

    def increment(self):
        self._nonce = (int.from_bytes(self._nonce, 'little') + 2).to_bytes(
            crypto_box_NONCEBYTES, 'little')