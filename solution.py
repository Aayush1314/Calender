import datetime

def BasicOutput():
    flag = 0
    output = {"Mon":0 ,"Tue":0,"Wed":0,"Thu":0,"Fri":0,"Sat":0,"Sun":0}     #Disired output format
    for day in output:
        for j in range(0,ld,2):         # This is loop is for cheaking all the dates for a particular day
            l = D[j].split("-")
            x = datetime.date(int(l[0]), int(l[1]), int(l[2]))
            if x.strftime("%a")==day:
                if flag == 0:
                    stack.add(day)
                output[day] = output[day] + int(D[j+1])
                flag = 1
        flag = 0
    return(output)

def ValidatedOutput(output, stack):
    count = 0
    stackout = []   #for keeping track of days that are not in input
    for day in output:
        if day in stack:
            if count!=0:
                d = (output[day]-output[prevDay])/(count+1)
                c=1
                for l in stackout:
                    output[l] = output[prevDay] + int(round(c*d))
                    c+=1
                stackout = []
                count=0
            prevDay=day
            continue
        else:
            stackout.append(day)
            count+=1
        
    return(output)

D = input().split()
ld = len(D)
stack = set()
dic= {}
# Making dictionary from input
for i in range(0,ld,2):
    dic[D[i]] = int(D[i+1])

output = BasicOutput()      #for iterating through the dates
FinalOutput = ValidatedOutput(output, stack)        #Checking for missed days and setting up their value

print(FinalOutput)
