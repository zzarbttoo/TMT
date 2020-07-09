# 3주차 k사 자물쇠와 열쇠

def rotate(key): # 90도 회전한 키
    M = len(key)
    rot_key = [[0] * M for i in range(M)]
    for i in range(M):
        for j in range(M):
            rot_key[j][M - 1 - i] = key[i][j]
    return rot_key

def can_open(key, lock, x, y): # 열 수 있는지 확인 / x, y는 열쇠가 시작되는 좌표
    N = len(lock)
    M = len(key)
    size = 2 * (M - 1) + N # 열쇠를 자물쇠에 끼울 때 필요한 공간
    grid = [[0] * size for i in range (size)]
    for i in range(M):
        for j in range(M):
            grid[x + i][y + j] += key[i][j] # 열쇠 표시
    for i in range(N):
        for j in range(N):
            grid[M - 1 + i][M - 1 + j] += lock[i][j] # 자물쇠 표시
            if grid[M - 1 + i][M - 1 + j] != 1 : # 1이 아니면 (0: 홈에 열쇠가 없음, 2: 돌기가 만남)
                return False # 열 수 없음
    return True

def solution(key, lock):
    answer = True
    N = len(lock)
    M = len(key)
    while r < 4: # 90, 180, 270, 360도 회전
        key = rotate(key) # 원래 것 회전
        for i in range(M + N - 1):
            for j in range(M + N - 1):
                answer = can_open(key, lock, i, j)
                if answer: # 열 수 있으면
                    return True
        r += 1
    return answer
