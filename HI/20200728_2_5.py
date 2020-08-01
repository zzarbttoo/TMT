# 5주차 2번 카펫

def solution(brown, yellow):
    answer = []
    y_h = 0
    y_v = 0

    for i in range(yellow, 0 , -1):
        if yellow % i == 0: # i가 약수일 경우
            y_h = i
            y_v = yellow // i
            # 테두리 한 줄은 갈색으로 칠해져 있음
            if brown == (y_h + 2) * 2 + y_v * 2: 
                break
    
    answer = [y_h + 2, y_v + 2]        
    return answer
