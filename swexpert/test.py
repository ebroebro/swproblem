for _ in range(3):
    lines=list(input())
    i=0
    while i < len(lines):
        if lines[i]=="'":
            tmp=[]
            while True:
                i+=1
                if lines[i]=="'":
                    break
                tmp.append(lines[i])
            print(''.join(tmp))
        i+=1
