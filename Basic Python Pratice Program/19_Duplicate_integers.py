# [Pooja Patil](https://github.com/Twist-hash)
# print duplicates from a list of integers

#function
def duplicate(list):
    n=len(list)
    dup=[]
    for i in range(n):
        k = i + 1
        for j in range(k,n):
            if list[i] == list[j] and list[i] not in dup:
                dup.append(list[i])
    return dup

#test
list=[ 10, 20, 30, -10, -20, 10, 80, -10, -20, 30]
print("Duplicate integeres: ",duplicate(list))