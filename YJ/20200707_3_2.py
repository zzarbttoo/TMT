#내 풀이
import collections

def solution(priorities, location):

    location_num = location
    hash = {}

    for i, pri in enumerate(priorities):
        hash[i] = hash.get(i, pri)

    queue = collections.deque([i for i in range(0, len(priorities))])
    count = 0 

    while(queue):
        isNotMax = False
        for i in range(0, len(queue)):
            if len(queue) != 0:
                if hash[queue[0]] < hash[queue[i]]:
                    isNotMax = True
                    break
        if isNotMax:
            queue.append(queue.popleft())
        else:
            temp = queue.popleft()
            count += 1
            if(temp == location_num):
                break

    return count 



print(solution([2,1,3,2], 2)) #1
print(solution([1,1,9,1,1,1], 0)) #5


#다른 사람의 풀이
def solution1(p, l):
    ans = 0
    #m은 우선 순위중 가장 큰 값 
    m = max(p)

    while True:
        v = p.pop(0)
        #pop 한게 max 값 -> 출력하고 +1
        if m == v:
            ans += 1
            #location 이 0번이면 끝
            if l == 0:
                break
            else:
                #아니면 location - 1
                l -= 1
            
            #그리고 다시 max 값을 찾는다
            m = max(p)
        #pop 한 것이 max 값이 아니라면 뒤로 보내야함
        else:
            p.append(v)
            if l == 0:
                l = len(p) - 1
            else:
                l -= 1
    return ans


#풀이 2
def solution(priorities, location):
    #queue에 튜플로 우선순위와 위치 정보를 함께 넣어줬다
    queue = [(i, p) for i, p in enumerate(priorities)]

    answer = 0

    while True:
        cur = queue.pop(0)
        #any : x 중 하나라도 참이라면 True return
        #cf all : x 가 모두 참이면 True
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer 

        

    


