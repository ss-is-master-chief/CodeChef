log = []
flag = 0
while(flag==0):
    x = int(input())
    if(x==42):
        flag = 1
        break
    else:
        log.append(x)

for i in log:
    print(i)
