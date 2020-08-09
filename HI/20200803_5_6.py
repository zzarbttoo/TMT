# 6주차 5번 정수 삼각형

# 하향식 (제일 위부터 아래로 더해 감)
def solution(triangle):
    sum_tri = []
    for k in range(len(triangle)):
        sum_tri.append([0] * (k+1))
    sum_tri[0] = triangle[0]
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            sum_tri[i + 1][j] = max(sum_tri[i + 1][j], sum_tri[i][j] + triangle[i + 1][j])
            sum_tri[i + 1][j + 1] = max(sum_tri[i + 1][j + 1], sum_tri[i][j] + triangle[i + 1][j + 1])

    return max(sum_tri[-1])

# 상향식 (두 번째 줄부터 바로 윗줄을 비교하며 더함)
def solution2(triangle):
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][-1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
    return max(triangle[-1])

# 상향식이 효율성이 더 좋았음