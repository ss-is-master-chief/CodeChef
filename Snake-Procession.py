'''https://www.codechef.com/problems/SNAKPROC'''

r = int(input("Enter the number of reports to be checked: "))
validity = []
if(r>=1 and r<=500):
    for i in range(0,r):
        l = int(input("Enter length of report: "))
        report_content = input()
        if(len(report_content)>500 or len(report_content)<1):
            validity.append('Invalid')
        else:
            if(len(report_content)!=l):
                validity.append('Invalid')
            if('H' not in list(report_content) and 'T' not in list(report_content)):
                validity.append('Valid')
                if(('H' not in list(report_content) and 'T' in list(report_content)) or
                   ('T' not in list(report_content) and 'H' in list(report_content))):
                    validity.pop()
                    validity.append('Invalid')
            else:
                ini = []
                flag = 0
                for x in range(0,len(report_content)):
                    if(report_content[x]=='H'):
                        ini.append('H')
                    elif(report_content[x]=='T'):
                        ini.append('T')
                for i in range(0,len(ini)-1):
                        if(ini[i]==ini[i+1]):
                            flag = 1
                            break
                if(ini[0]=='T' or ini.count('H')!=ini.count('T') or flag==1):
                    validity.append('Invalid')                  
                else:
                    validity.append('Valid')
    for i in validity:
        print(i)
                




