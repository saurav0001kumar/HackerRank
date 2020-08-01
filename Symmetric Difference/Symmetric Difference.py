'''To find Symmetric Difference between two Sets.'''
#Example INPUT:
'''
4
2 4 5 9
4
2 4 11 12
'''
#OUTPUT: (Symmetric difference in ascending order)
'''
5
9
11
12
'''
#Code
n=int(input())
a=[int(i) for i in input().split()]
m=int(input())
b=[int(i) for i in input().split()]
a1=set(a)
b1=set(b)
t=a1.union(b1)
f=t-(a1.intersection(b1))
tt=list(f)
tt.sort()
for i in tt:
    print(i)
