from common import *


def KSASST(key, n, t):
    num_key = str2num(key)
    key_length = len(num_key)
    s = list(range(n))

    marked_list = [False for _ in range(n)]
    marked_list[-1] = True
    marked_num = 1
    j = n
    i = 0
    while marked_num < n:
        i = i % n
        j = (j + s[i % n] + num_key[i % key_length]) % n
        swap(s, i, j)
        if marked_num < n / 2:
            if not marked_list[j] and not marked_list[i]:
                marked_list[j] = True
                marked_num += 1
        else:
            if (not marked_list[j] and marked_list[i]) or (not marked_list[j] and i == j):
                marked_list[j] = True
                marked_num += 1
        swap(marked_list, i, j)
        i += 1
    return s


d = 0
t = n = 16
length = 10
key = 'Wiki'
keystream_list = rc4_mdrop_d(key, n, t, d, KSASST, length)
print(keystream_list)
f = open(r"C:\Users\Latitude\Desktop\Studia - Git_repo\studia\Kryptografia\Lista 2\diehard\test.txt", 'w')
f.write(keystream_list)
