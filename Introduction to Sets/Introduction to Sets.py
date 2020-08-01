''' Finding Average of DISTINCT Numbers using Set in python. '''
#Example Input:
'''
10
161 182 161 154 176 170 167 171 170 174
'''
#Output:
'''
169.375
'''
#Code
def average(a):
    s=set(a)
    add=0
    for i in s:
        add+=int(i)
    res=add/len(s)
    return(res)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
