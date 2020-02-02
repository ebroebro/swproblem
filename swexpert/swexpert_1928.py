#1928 Base64 Decoder
import base64  ##  Base 64 encoding , decoding 하는 함수

T = int(input())
for z in range(T):
    words = base64.b64decode(input())
    rslt = words.decode("UTF-8")
    print("#{} {}".format(z + 1, rslt))

    '''
import base64


s = "Hello World!"

##encoding 과정  (문자 -> byte -> 64base)
# 문자를 byte로 encoding 하기
b = s.encode("UTF-8")

# 64Base로 encode하기
e = base64.b64encode(b)


# 64Base로 변환된 것을 그대로 문자화해보자.
s1 = e.decode("UTF-8")
print("Base64 Encoded:", s1)

##decoding 과정 (64base-> byte->문자)
# Decoding the Base64 bytes
d = base64.b64decode(b)
# Decoding the bytes to string
s2 = d.decode("UTF-8")
print(s2)
'''