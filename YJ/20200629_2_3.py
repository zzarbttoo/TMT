def solution(heights):

    answer = []

    for i in range(0, len(heights)):

        temp_num = 0       
        length_num = i
        temp_stack = heights[0:i]

        while(temp_stack):
            length_num -=1
            pop_num = temp_stack.pop()
            if pop_num> heights[i]:
                temp_num = heights.index(pop_num, length_num, i) + 1
                break
        answer.append(temp_num)

    return answer 

# print(solution([6,9,5,7,4])) # 0 0 2 2 4
print(solution([3,9,9,3,5,7,2])) # 0 0 0 3 3 3 6
print(solution([1,5,3,6,7,6,5])) # 0 0 2 0 0 5 6
