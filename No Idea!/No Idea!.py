#Example Input:
'''
3 2
1 5 3
3 1
5 7
'''
#Output:
'''
1
'''
#Explanation:
'''
You gain 1 unit of happiness for elements 3 and 3 in set A.
You lose 1 unit for 5 in set B.
The element 7 in set B does not exist in the array so it is not included in the calculation.
Hence, the total happiness is 2-1=1.

**NOTE**:
-> Array/List can have duplicate elements.
-> Sets do not have any duplicate element.
'''
#Code
nm=list(map(int,input().split()))
n=nm[0]
m=nm[1]
s=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
a1=set(a)
b1=set(b)
hp=0
for i in range(len(s)):
    if s[i]:
        if s[i] in a1:
            hp+=1
        elif s[i] in b1:
            hp-=1
print(hp)
