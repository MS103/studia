from openssl import OpenSSL
from random import randint
import time

# private values
s = 16  # len(secret)
n = 24  # len(msg)
# N = pow(2, n)  # len(secrets)
N = 1000

# Placeholder
msgs = []
keys = []
secrets = []
start = time.time()
# ALICE (Encryption)
for i in range(0, N):
    secret = str(randint(1000000000000000000000000, 9999999999999999999999999))
    key = str(randint(1000, 9999))

    enc_suite = OpenSSL('cbc')
    msg = enc_suite.encrypt('0' * (n - s) + secret, key * 4, key * 4)

    msgs.append(msg)
    keys.append(key)
    secrets.append(secret)

# ALICE sends "msgs" Block to BOB

# BOB (Brute force Decryption)
decrypted_msg = ''
rand_msg_solve = randint(0, N-1)

print("Start decrypting at {}".format(time.time() - start))
keys = [str(x) for x in range(1000, 9999)]
while not decrypted_msg[:(n - s)] == '0' * (n - s):
    if len(keys) == 0:
        print("Could not find decryption")
        exit(-1)
    key = keys.pop(randint(0, len(keys)-1))
    dec_suite = OpenSSL('cbc')
    decrypted_msg = dec_suite.decrypt(msgs[rand_msg_solve], key * 4, key * 4)

print('Bob decrypted secret:\t\t' + decrypted_msg[(n - s):])
print('Alice secret (' + str(rand_msg_solve) + '):\t\t' + secrets[rand_msg_solve])
print(time.time() - start)
