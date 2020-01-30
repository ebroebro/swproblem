#2047. 신문헤드라인
word = input()
for i in word:
    if ord('a') <= ord(i) <=ord('z'):   #  ord  문자- > 아스키코드
        i=chr(ord(i)+ord('A')-ord('a'))   # chr  코드 -> 문자
    print(i,end="")
