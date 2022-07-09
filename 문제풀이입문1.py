'''def solution(mylist):
    answer=[]
    k=0
    for i in mylist:        
        answer += [len(mylist[k])]
        k+=1
    return answer

solution([[1],[2]])
solution([[1,2],[3,4],[5]])

'''
def solution(mylist):
    return list(map(len,mylist))

print(solution([[1],[2]]))
print(solution([[1,2],[3,4],[5]]))
