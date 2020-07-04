def solution(genres, plays):
    answer = []
    
    hash = {}


    for i in range(0, len(genres)):
        hash[genres[i]] = hash.get(genres[i], [0, []]) 
        hash[genres[i]][0] += plays[i]
        hash[genres[i]][1].append((plays[i], i))


    hash = sorted(hash.items(), key = lambda x: x[1][0], reverse=True)

    for num in hash:
        num[1][1] = sorted( num[1][1], key = lambda x: (-x[0] , x[1]))


    for num in hash:
        tempNum = 0
        for i in range(0, len(num[1][1])):
            answer.append(num[1][1][i][1])
            tempNum+=1
            if(tempNum == 2):
                break
    
    return answer





    
# print(solution(["classic", "pop", "classic", "classic", "pop"] , [500, 600, 150, 800, 2500]))
# print(solution(["a", "b", "a", "b", "c"], [100, 200, 300, 400, 500]))
# print(solution(["a"],[1]))
print(solution( ["a", "a", "a"], [1, 1, 1]))


    