content = input().split() #假設 1 + 2 * 3 - 4 / 5 會變成["1","+","2","*","3","-","4","/","5"]
i,result = 0,0.0
while (i < len(content)): #判斷i的範圍是否在content的list長度內
    if(content[i] == '*'):
        content[i-1] = float(content[i-1]) * float(content[i+1]) #因為index偵測在index = 3 的時候是*號 所以會變成["1","+","6.0","*","3","-","4","/","5"]
        del content[i:i+2] #把*跟3刪除 ["1","+","6.0","-","4","/","5"]
        i-=1 #index倒退1位 (從原本指向index 3變成 index 2) 為了判斷運算子
    elif(content[i] == '/'):
        content[i-1] = float(content[i-1]) / float(content[i+1]) #因為index偵測在index = 6 的時候是/號 所以會變成["1","+","6.0","-",0.8","/","5"]
        del content[i:i+2] #把/跟5刪除 ["1","+","6.0","-","0.8"]
        i-=1 #index倒退1位 (從原本指向index 6變成 index 5) 為了判斷運算子
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

        
