from os import urandom
from hashlib import blake2b
from _tweetnacl import (crypto_box_afternm,crypto_box_beforenm,crypto_scalarmult_base,crypto_box_open_afternm, crypto_box_NONCEBYTES, crypto_hash, crypto_secretbox, crypto_secretbox_open)

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
		self._nonce = (int.from_bytes(self._nonce, 'little') + 2).to_bytes(crypto_box_NONCEBYTES, 'little')
                                        
class Crypto:
	def __init__(self):
		self.server_key = bytes.fromhex("78BD03628030B86BCF17817DF13A3E9C0E8FD03F06F222A44C40CA70F3ECC748")
		self.client_sk = bytes.fromhex("BB14D6FD2B7C9823EAEDB4338CB7237F61E422D23C4977F74ADA052702C0C62D")
		self.client_pk = crypto_scalarmult_base(self.client_sk)
		self.session_key = b'\x13Y\xd8\x13M\x19\xf6\xffv\xe7q{\xb0\x9dl\x0c\x81\xe7)(\x9b\t\xc3\xfc'
		self.shared_key = None
		self.decryptNonce = None
		self.encryptNonce = Nonce(urandom(24))
		self.shared_en = bytes(urandom(32))
		self.public_key = None
		self.s = None
		self.nonce = None
	
	def decrypt_server(self, packet_id, payload):
		#self.encryptNonce.increment()
		return crypto_secretbox_open(payload, bytes(self.encryptNonce), self.shared_en)
		
	def decrypt(self, packet_id, payload):
		if packet_id == 10100:
			return payload
			
		elif packet_id == 10101:
			if payload[:32] != self.client_pk:
				print(f"[ERROR] Cryptography error, message: {packet_id}, client private key: {self.client_pk}, message key: {payload[:32]}")
			else:
				self.public_key = payload[:32]
				payload = payload[32:]
				self.nonce = Nonce(clientKey=self.client_pk, serverKey=self.server_key)
				self.s = crypto_box_beforenm(self.server_key, self.client_sk)
				decrypted = crypto_secretbox_open(payload, bytes(self.nonce), self.s)
				session_key = decrypted[0:24]
				self.decryptNonce = Nonce(decrypted[24:48]) # decrypted nonce
				return decrypted[48:]
		elif self.decryptNonce is None:
			return payload
		else:
			self.decryptNonce.increment()
			decrypted = crypto_secretbox_open(payload, bytes(self.decryptNonce), self.shared_en)
			return decrypted
					
	def encrypt(self, packetID, payload):
		if packetID == 20100 or packetID == 20103:
			return payload
		else:
			if packetID == 20104:
				nonce = Nonce(self.decryptNonce, clientKey=self.client_pk, serverKey=self.server_key)
				payload = bytes(self.encryptNonce) + self.shared_en + payload
				encrypted = crypto_secretbox(payload, bytes(nonce), self.s)
				return encrypted
			else:
				self.encryptNonce.increment()
				encrypted = crypto_secretbox(payload, bytes(self.encryptNonce), self.shared_en)
				return encrypted