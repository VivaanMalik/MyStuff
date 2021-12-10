import bitcoin
from hashlib import sha256
PrivateKeyDeLaMoi=bitcoin.random_key()
print("Private Key: %sn" % PrivateKeyDeLaMoi)
PublicKeyDeLaMoi=bitcoin.privtopub(PrivateKeyDeLaMoi)
print("Public Key: %sn" % PublicKeyDeLaMoi)
WallAdressDelaMoi=bitcoin.pubtoaddr(PublicKeyDeLaMoi)
print("Wallet Adress: %sn" % WallAdressDelaMoi)

## Variables! ===== Variables! ===== Variables! ===== Variables! ===== Variables! ===== Variables! ===== Variables! ===== Variables! ===== Variables! ===== Variables! ===== Variables! ===== Variables! ===== Variables! ===== Variables! ===== 

MAX_NONCE=10000000   

## Fuctions!! ====== Fuctions!! ====== Fuctions!! ====== Fuctions!! ====== Fuctions!! ====== Fuctions!! ====== Fuctions!! ====== Fuctions!! ====== Fuctions!! ====== Fuctions!! ====== Fuctions!! ====== Fuctions!! ====== Fuctions!! ====== 

def Encoder(txt):
    return sha256(txt.encode("ascii")).hexdigest()

def MINE(block_num, transaction, prevhash, prefix_0s):
    prefix_str='0'*prefix_0s
    for nonce in range(MAX_NONCE):
        text= str(block_num) + transaction + prevhash + str(nonce)
        hash = Encoder(text)
        # print(hash)
        if hash.startswith(prefix_str):
            print("Bitcoin mined with nonce value :",nonce)
            return hash
    x=input("couldn't find a hash from 0 to ", MAX_NONCE, " :( \n Try Again?[y/n]")
    if x.upper()=="Y":
        MINE()

transactions='''
A->B->10
B->c->5
'''
difficulty = 5
import time as t
begin=t.time()
new_hash = MINE(684260,transactions,"000000000000000000006bd3d6ef94d8a01de84e171d3553534783b128f06aad",difficulty)
print("Hash value : ",new_hash)
time_taken=t.time()- begin
print("The mining process took ",time_taken,"seconds")