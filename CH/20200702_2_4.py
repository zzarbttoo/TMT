def solution(progresses, speeds):
    day=[]
    answer = []
    n=-0
    for i in range(len(progresses)) :
        if (100-progresses[i])%speeds[i]==0 :                #작업 완료까지 걸리는 일수 책정
            day.append((100-progresses[i])//speeds[i])       #나머지가 없으면 그냥 넣고
        else :
            day.append((100-progresses[i])//speeds[i]+1)     #나머지가 있으면 +1 해서 넣음
    val=day[0]                                               #기준값은 제일 첫번째 기능이 완료되는 날
    j=0
    for i in range(len(day)):
        while day[j]<=val:                                   #기준값보다 낮은 것을 찾는다.
            n+=1                                             #기준값보다 낮은 작업의 개수 카운팅
            j+=1
            if j==len(day):
                break
        answer.append(n)                                     #기준값보다 낮은 작업의 개수를 넣음
        n=0
        if j==len(day):
                break
        val=day[j]                                           #기준값 재설정(남은 애들 중 가장 앞에 있는 기능)

    return answer
