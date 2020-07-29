'''To Wrap the text in the group of W characters.'''

# FOR EXAMPLE : Width W=4 and Text="ABCDEFGHIJKLIMNOQRSTUVWXYZ"

#Input:
'''
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
'''
#Output:
'''
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''
#Code

def wrap(s, w):
    left=len(s)//w
    left=len(s)-(left*w)
    ls=s[len(s)-left:len(s)]
    a=[]
    i=0
    while i<len(s)-w:
        t=""
        for j in range(w):
            t+=s[i+j]
        a.append(t)
        i+=w
        
    a.append(ls)
    res='\n'.join(a)

    return(res)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
