#To find the count of input substring in the input string.
#For Example: 
'''
Input String = "ABCDCDC"
Input Substring = "CDC"

OUTPUT: 2

Explanation: The count of substring is 2 as it's 1st occurence is from index 2 to 4 and 2nd occurence is from index 4 to 6.

'''

def count_substring(st, sub):
    c=0
    s=[]
    for k in range(1,len(st)):
        for i in range(len(st)):
            s.append(st[i:k+1])

    cc=list(filter(lambda x: x==sub,s))
    c=len(cc)
    return c
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)