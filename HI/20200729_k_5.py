# 5주차 k사 기둥과 보 설치
def solution(n, build_frame):
    
    answer = []

    def possible(x, y, a):
        if a == 0: # 기둥 제한 조건
            if y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
                return True # 가능
            return False # 불가
        
        else: # 보 제한 조건
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                return True # 가능
            return False # 불가
    
    for f in build_frame:
        if f[3] == 1 and possible(f[0], f[1], f[2]): # 설치가 가능하다면
            answer.append([f[0], f[1], f[2]]) # 설치
        elif f[3] == 0: # 삭제 시
            answer.remove([f[0], f[1], f[2]]) # 우선 삭제
            for a in answer:
                if possible(a[0], a[1], a[2]) is False: # 나머지 요소에 대한 제한 조건 검사
                    answer.append([f[0], f[1], f[2]]) # 불가 시 되돌리기
                    break
    
    answer.sort()
    return answer