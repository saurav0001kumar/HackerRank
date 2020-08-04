'''
Stacking the cubes with sizes in descending order from bottom to top.

**NOTE**
Every time only the left-most or the right-most cube can be stacked from the array/list.
'''
#Input Format:
'''
The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains N, the number of cubes.
The second line contains N space separated integers, denoting the sideLengths of each cube in that order.
'''
#Sample Input:
'''
2
6
4 3 2 1 3 4
3
1 3 2
'''
#OUTPUT:
'''
Yes
No
'''
#Code
for t in range(int(input())):
    n=int(input())
    c=list(map(int,input().split()))
    s=[]
    i=0
    for i in range(n):
        if c==[]:
            break
        if (c[0]>=c[-1] and s==[]) or (c[0]>=c[-1] and s[-1]>=c[0]):
            s.append(c[0])
            c.remove(c[0])
        elif (c[0]<c[-1] and s==[]) or (c[0]<c[-1] and s[-1]>=c[-1]):
            s.append(c[-1])
            c.pop(-1)
    if c==[]:
        print("Yes")
    else:
        print("No")
