import string
from bruteforce import check,check_by_wordlist
import time
import sys
flag = "d"
try:
    flag = sys.argv[1]
    if flag == "w":
        print("Wordlist mode")
    else:
        print("Default mode")
except:
    print("Default mode")
characters =  string.digits+string.ascii_letters
token = str(raw_input("Insert token: "))
if flag !="w":
    maxlength = int(raw_input("Max length of secret: "))

    start = time.time()
    secret = check(token, characters, maxlength+1)
    end = time.time()
    print("Elapsed time: " + str(end - start) + "s")

    if secret or secret == "":
        print("The secret used to generate the token is \""+ secret +"\".")
    else:
        print("The secret could not be determined. Try increasing the maximum length.")

else:
    start = time.time()
    secret = check_by_wordlist(token)
    end = time.time()
    print("Elapsed time: " + str(end - start) + "s")

    if secret or secret == "":
        print("The secret used to generate the token is \"" + secret + "\".")
    else:
        print("The secret could not be determined. Try increasing the maximum length.")
