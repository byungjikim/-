num, base = map(int, input().strip().split(' '))
st_num= str(num)
k=0
answer = 0
for i in st_num:
    answer += int(st_num[k])*(base**(len(st_num)-k-1))
    k=k+1
print(answer)

# int(num,base) 진법 변환 지원해
