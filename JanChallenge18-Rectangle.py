t = int(input())
log = []
result = []
if(t>=1 and t<=1000):
    for i in range(0,t):
        ini = input().split(' ')
        entry = [int(ini[0]),int(ini[1]),int(ini[2]),int(ini[3])]
        res = []
        go = 0
        for i in entry:
            if(i>=1 and i<=10000):
                go += 1
        if(go==4):
            for j in range(0,len(entry)):
                res.append(entry.count(entry[j]))
            flag = 0
            for x in range(0,len(res)-1):
                if(res[x]==res[x+1] and res[x]!=1 and res[x+1]!=1):
                    flag += 1
            if(flag==3):
                result.append("YES")
            else:
                result.append("NO")
    
for i in result:
    print(i)
