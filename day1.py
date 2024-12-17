import numpy as np

#Load location IDs lists and store then in arrays
list1 =np.loadtxt('list.txt',dtype=int, delimiter=None, usecols = [0])
list2 =np.loadtxt('list.txt',dtype=int, delimiter=None, usecols = [1])

#Sort the lists
list1 = np.sort(list1)
list2 = np.sort(list2)
distance = 0
similarity = 0

#Part1
for i in range(len(list1)):
    distance += abs(list1[i] - list2[i])
    
print(distance)

#Part2
list_sim= list(list2)
for i in range(len(list1)):
    similarity += list_sim.count(list1[i]) *  list1[i]


print(similarity)
