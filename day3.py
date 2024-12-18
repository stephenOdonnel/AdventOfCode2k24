import re
 
regex = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
regex_dont = r"don't\(\)"
regex_do = r"do\(\)"
 
#with open("input_day3.txt", "r") as file:
with open("example.txt", "r") as file:
    string = file.read()
 
match = re.findall(regex, string)
 
results = 0
for i in range (len(match)):
    for j in range(len(match[i])-1):
        results += int(match[i][j]) * int(match[i][j+1])
 
 
print("Result :" , results)