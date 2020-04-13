lines=['헛소리',
'중앞',
'정민기 30',
'벅수호 50',
'헛소리',
'헛소리']
i=0
for line in lines:
    if line == '헛소리':
        print('헛소리')
        while i < len(lines) :
            print(lines[i])
            if lines[i] == "" :
                break
            i = i + 1