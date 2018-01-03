'''https://www.codechef.com/problems/FBMT'''

t = int(input("Enter the number of test cases: "))

if(t>=1 and t<=10**5):  
    winner = []
    for i in range(0,t):
        n = int(input("Enter the number of logs: "))
        log = ['','']
        score = [0,0]
        if(n>0 and n<=10**5):
            for j in range(0,n):
                entry = input()
                if entry not in log:
                    if(entry!=log[0] and log[0]!=''):
                        log[1] = entry
                    else:
                       log[0] = entry
                if(entry==log[0]): score[0] += 1
                else: score[1] += 1
            
            if(score[0]>score[1]): winner.append(log[0])
            elif(score[0]<score[1]): winner.append(log[1])
            else: winner.append('Draw')
        else:
            winner.append('Draw')
            
    for i in range(0,len(winner)):
            print(winner[i])
