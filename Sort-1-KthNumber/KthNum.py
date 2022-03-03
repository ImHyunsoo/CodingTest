def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        cut_array = array[commands[i][0]-1:commands[i][1]]
        cut_array.sort()
        answer.append(cut_array[commands[i][2]-1])
    return answer
