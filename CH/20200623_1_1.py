def solution(array, commands):
    answer=[]
    for i in range(0,len(commands)):
        answer.append(sorted(array[(commands[i][0]-1):(commands[i][1])])[commands[i][2]-1]) #commands의 원소를 순서대로 불러와서 수행
        i+=1
    return answer
