def solution(array, commands):
    answer = []
    for n in commands:
        for i in commands[n]:
            array1 = array[(commands[n][0]-1):(commands[n][1]-1)]
            array1.sort()
            answer = array1[commands[n][2]]
    return answer

solution([1,5,2,6,3,7,4],[[2,5,3],[4,4,1],[1,7,3]])
