def solution(clothes):

    hash = {}
    sum = 0
    mul = 1

    for i in clothes:
        hash[i[1]] = hash.get(i[1], []) + [i[0]]
    
    for i in hash:
        sum = 1 + len(hash[i])
        mul *= sum
    
    answer = mul - 1
    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))