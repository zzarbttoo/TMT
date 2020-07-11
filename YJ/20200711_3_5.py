import heapq

def solution(jobs):
    answer = 0
    index = 0
    time = 0
    queue =[]

    heapq.heapify(queue) 
    jobs = sorted(jobs, key = lambda x : x[0])

    while(True):

        if index >= len(jobs) and len(queue) == 0:
            break

        while(True):
            if index >= len(jobs) or jobs[index][0] > time:
                break
            heapq.heappush(queue, (jobs[index][0], jobs[index][1]))
            index += 1

        if len(queue):
            time = jobs[index][0]
         
        else:
            job = heapq.heappop(queue)[1]
            answer += time - job[0] + job[1]
            time += job[1]
        
    answer = answer / len(jobs)


    return answer 

print(solution([[0,3] , [1, 9] , [2, 6]]))