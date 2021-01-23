def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])


def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


var1 = encode("are you ok")
var = decode('1000111111011110 110001110100101')
print(encode("yes,please get out"))
# print(var)
# print(var1)
# print(var1)
# print(decode(var1))
# var1Arr = var1.split(" ")
# for i in range(len(var1Arr)):
#     print(var1Arr[i])