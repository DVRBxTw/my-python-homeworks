pattern = input().split() #把pattern的輸入 例如：S D D C H --> ["S","D","D","C","H"]
card = input().split() #A K 5 Q J
card_point,index,bonus_point = 0,0,0
maximum = []
stoper = set()
temp = ''
#判斷建議行動
S_count,H_count,D_count,C_count = pattern.count("S"),pattern.count("H"),pattern.count("D"),pattern.count("C")
maxi = max(S_count,H_count,D_count,C_count)
count = {"S":S_count,"H":H_count,"D":D_count,"C":C_count} 
for i,j in count.items():
    if j == maxi:
        maximum.append(i)
if(len(maximum) > 1):
    if("S" in maximum):
        action = "Spade"
    elif("H" in maximum):
        action = "Heart"
    elif("D" in maximum):
        action = "Diamond"
    elif("C" in maximum):
        action = "Club"
else:
    if("S" in maximum):
        action = "Spade"
    elif("H" in maximum):
        action = "Heart"
    elif("D" in maximum):
        action = "Diamond"
    elif("C" in maximum):
        action = "Club"
    
#轉換點數 及 計算總點力
if len(set(pattern)) == 1:
    bonus_point = 2
for i in card:
    if(i == "A"):
        card_point += 4
    elif(i == 'K'):
        card_point += 3
    elif(i == 'Q'):
        card_point += 2
    elif(i == 'J'):
        card_point += 1
total_point = card_point + bonus_point


if('A' in card):
    for i,j in zip(pattern,card):
        if(j == 'A'):
            stoper.add(i)
if('K' in card):
    temp = ''
    for i,j in zip(pattern,card):
        if(j == 'K'):
            temp += i
            if len(temp) > 1:
                stoper.add(temp)

if('Q' in card):
    temp = ''
    for i,j in zip(pattern,card):
        if(j == 'Q'):
            temp += i
            if len(temp) > 2:
                stoper.add(temp)
stop = list(stoper)


if(total_point < 8):
    suggest = "Pass"
elif(total_point >= 15):
    suggest = "Strong Open"
elif(total_point >= 8 and total_point <= 14):
    suggest = f"Open {action}"

print(f"HCP: {card_point}\nTotal Points: {total_point}\nDistribution (S-H-D-C):{S_count}-{H_count}-{D_count}-{C_count}\nStopped Suits: {stop}\nOpening Bid: {suggest}")