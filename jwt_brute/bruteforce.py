from itertools import product
from signature_validation import validate
default_path = '/opt/rockyou.txt'
def checkSecret(token, secret, n):
    print("N="+ str(n) + " - tried secret: \"" + ''.join(secret) + "\"")
    if validate(token, ''.join(secret)):
        return ''.join(secret)

def check(token, characters, maxlength):
    for n in range(0, maxlength):
        generator=product(characters, repeat = n)
        for secret in generator:
            successful = checkSecret(token, secret, n)
            if successful or successful == "":
                return successful

def check_by_wordlist(token):
    f = open(default_path,'rb')
    l = f.readline().strip()
    while 1:
        n = len(l)
        successful = checkSecret(token, l, n)
        if successful or successful == "":
            return successful
        l = f.readline().strip()
