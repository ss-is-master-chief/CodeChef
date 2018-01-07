n = int(input())
if(n>=1 and n<=2**17):
    h = input().split(' ')
    flag = 0
    for i in range(0,n):
        h[i] = int(h[i])
        if(h[i]>=1 and h[i]<=10**9):
            flag += 1
    if(flag==n):
        q = int(input())
        if(q>=1 and q<=2**18):
            actions = []
            corr = 0
            for i in range(0,q):
                xy = input().split(' ')
                xy[0] = int(xy[0])
                xy[1] = int(xy[1])
                if(xy[0]>=0 and xy[0]<=10**9 and xy[1]>=1 and xy[1]<=10**9):
                    actions.append(xy)
                    corr += 1
            if(corr==q):
                score = h[:]
                for i in range(0,q):
                    for j in range(0,n):
                       if((j&actions[i][0])==j):
                            score[j] = score[j] - actions[i][1]
                    cnt = 0
                    for m in score:
                        if(m>0):
                            cnt += 1
                    print(cnt)
          
                        
                
        
                
            
        
