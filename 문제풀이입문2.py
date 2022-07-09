a, b = map(int, input().strip().split(' '))
mok = a//b
merge = a%b
print(str(mok)+' '+str(merge))
