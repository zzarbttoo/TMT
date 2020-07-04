import collections

def solution(progresses, speeds):

    answer = []
    progresses = collections.deque(progresses)
    speeds = collections.deque(speeds)


    while(progresses):
        sum = 0
        for i in range (0, len(progresses)):
            if(progresses[i] < 100):
                progresses[i] += speeds[i]


        while(progresses):
            if progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                sum+=1
            else:
                if(sum != 0):
                    answer.append(sum)
                break
    if (sum > 0):
        answer.append(sum)
    return answer



progress1 = [93, 30, 55]
speeds1 = [1, 30, 5]

print(solution(progress1, speeds1))