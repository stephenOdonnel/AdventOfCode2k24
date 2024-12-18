def Distance(a,  b):
    if (abs(a-b)) >= 1 and (abs(a-b)) <= 3: 
        return True
    else:
        #print("Error - out of range : abs(", a,",", b,") =", abs(a-b))
        return False
 
def IsDecr( a,  b):
    if a >= b: 
        if Distance(a,b):
            return True
        else:
            return False
    else:
        return False
 
def IsIncr( a,  b):
    if a <= b: 
        if Distance(a,b):
            return True
        else:
            return False
    else:
        return False
 
def IsSafe (i):
    Inc=1
    Dec=1
    for j in range (len(i)-1):
        if IsIncr(i[j],i[j+1]):
            Inc += 1
        elif IsDecr(i[j],i[j+1]):
            Dec += 1
    if Inc == (len(i)) or Dec == (len(i)):
        return True
    else:
        return False
def Dampener(lists):
    i = lists.copy()
    temp = lists.copy()
    for j in range(len(i)):
        i.pop(j)
        if IsSafe(i):
            return True
        else:
            i = temp.copy()
    return False

 
 
safe_counter = 0
unsafe_counter = 0
 
 
with open('input_day2.txt') as file:
#with open('example.txt') as file:  
  lines = [list(map(int,line.split())) for line in file]
 
for i in lines:
    if IsSafe(i):
        safe_counter +=1
        print("Safe ",  i)
    else:
        if Dampener(i):
            safe_counter +=1
            print("Safe with Dampener",  i)
        else:
            unsafe_counter += 1
            print("Unsafe ", i)  
 
print("Results:")
print("Safe", safe_counter)
print("Unsafe", unsafe_counter)