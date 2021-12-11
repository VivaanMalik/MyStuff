from Crypto.Util import number
import random
def JenKeyz(len): #GenKeys
    primeNum1 = number.getPrime(len)
    primeNum2 = number.getPrime(len)
    n=primeNum2*primeNum1
    phi=(primeNum1-1)*(primeNum2-1)
    e=1
    while n%e==0:
        print('huh?')
        e=random.randrange(2, phi)
    k=random.randrange(1, 1000)
    d=((k*phi)+1)/e
    return Publikee(1, [n, e]), Praivetkee(1, d)
class Publikee(): # Public Key
    def __init__(self, sections:int, value:list):
        self.value=value
        self.sect=sections
class Praivetkee: # Private Key
    def __init__(self, sections:int, value:list):
        self.value=value
        self.sect=sections
print(JenKeyz(2048))