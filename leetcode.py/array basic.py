"""
#Array Traversal (Basic loop)

a = [1, 2, 3]

for i in a:
    print(i)


#sum of elements

arr = [1,2,3,4]
total = 0

for a in arr:
    total = total + a

print(total)




#Find Maximum element

arr = [5,8,33,28,7]
total =0

for i  in arr:                 #Concept: comparison + traversal
    if i > total:
        total = i

print(f"the largest number is {total} in the array")


#Count Even & Odd

arr = [1,2,3,4,5,6,7]

even = 0
odd = 0

for j in arr:
    if j % 2 == 0:
        even += 1

    else:
        odd += 1

print("total odd : ",odd)
print("total even : ",even)



#count of elements

arr = [1,2,3,4]
count = 0

for a in arr:
    count +=  1

print("total count :",count)



#Reverse an Array

a = [33,55,26,88]
order = []

for i in range(len(a)-1,-1,-1):       #index dhan matter in reverse in array///add ku range(0,len(a),1)
    order.append(a[i])
print(order)



#Check element exists (Linear Search) ----->>>>Binary Search

arr = [33,44,55,66,77,88]

finds = 88

found = False

for i in arr:
    if i == finds:
        found = True
        break


print(found)


#Find Duplicate elements

array=[1, 2, 3, 2, 4, 1]

dup=[]
for i  in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i] == array[j] and array[i] not in dup:
            dup.append(array[i])
print(dup)

"""

#Remove duplicates

a =[1,2,2,3,4,5,5,7,8,9,8]

after_remove =[]

for i in a :
    if i not in after_remove:
        after_remove.append(i)

print(after_remove)














