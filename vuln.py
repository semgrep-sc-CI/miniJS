#import vulnerable library to recreate one of two scenarios:
# a : A reachable finding
# b : importing a library that is vulnerable

import pyjwt
import sys


def insecure_verify_reachable(semgrepToken):
    decoded = jwt.decode(semgrepToken, verify = False)
    print(decoded)
    return True

def insecure_verify_unreachable(semgrepToken):
    # Making a good jwt token that should work by signing it with the private key
    encoded_good = jwt.encode({"test": 1234}, priv_key_bytes, algorithm="ES256")
    print(decoded)
    return True
