content = input().split()
i,result = 0,0.0
while (i < len(content)):
    if(content[i] == '*'):
        content[i-1] = float(content[i-1]) * float(content[i+1])
        del content[i:i+2]
        i-=1
    elif(content[i] == '/'):
        content[i-1] = float(content[i-1]) / float(content[i+1])
        del content[i:i+2]
        i-=1
    i+=1
i = 0
while(i<len(content)):
    if(content[i] == '+'):
        content[i-1] = float(content[i-1]) + float(content[i+1])
        del content[i:i+2]
        i-=1
    elif(content[i] == '-'):
        content[i-1] = float(content[i-1]) - float(content[i+1])
        del content[i:i+2]
        i-=1
    i+=1
print('%.2f' % float(content[0]))
        