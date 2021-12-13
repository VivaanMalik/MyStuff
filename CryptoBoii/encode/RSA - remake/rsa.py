from Crypto.Util import number
import random
kriptoe=' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_~`!@#$%^&*()+=[{}]|\\:;"<>,./?'+"'"
def JenKeyz(len): #GenKeys
    primeNum1 = number.getPrime(len)
    primeNum2 = number.getPrime(len)
    n=primeNum2*primeNum1
    phi=(primeNum1-1)*(primeNum2-1)
    e=1
    while n%e==0:
        e=random.randrange(2, phi)
    k=random.randrange(1, 1000)
    d=((k*phi)+1)/e
    return Publikee(1, [n, e]), Praivetkee(1, d)
def deekript(text:str, publikee, praivetkee): #decrypt
    text=int(text)
    text=text**int(praivetkee.value)
    text=text%int(publikee.value[0])
    msg=''
    text=str(text)
    for i in range(round(len(str(text))/2)):
        if text[i]=='0':
            eendecks=text[i+1]
        else:
            eendecks=text[i]+text[i+1]
        print(eendecks)
        eendecks=int(eendecks)
        msg+=kriptoe[eendecks]
    return msg
def Nkript(text, publikee): # encrypt
    kriptedtext='93'
    for i in text:
        eendeckz=kriptoe.index(i)
        eendeckz=str(eendeckz)
        if len(eendeckz)==1:
            eendeckz+='0'
        kriptedtext+=eendeckz
    kriptedtext=int(kriptedtext)
    kriptedtext**publikee.value[1]
    kriptedtext=kriptedtext%publikee.value[0] 
    return str(kriptedtext)
class Publikee(): # Public Key
    def __init__(self, sections:int, value:list):
        self.value=value
        self.sect=sections
class Praivetkee: # Private Key
    def __init__(self, sections:int, value:list):
        self.value=value
        self.sect=sections
text=input('Enter text to encrypt:\n')
pub, priv = JenKeyz(4)
print('1')
nkript=Nkript(text, pub)
print('2')
print('3')
print(deekript(nkript, pub, priv))
