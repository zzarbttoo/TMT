# 1주차 K_문자열 압축
def solution(s):
    nslice = 1
    count = 1
    length = 0
    result = len(s)

    while nslice <= len(s):
        i = 0   #i는 비교하는 현재 위치
        zip_string = []   #압축된 문자열
        
        while i <= len(s)-nslice:
            if s[i:i+nslice] == s[i+nslice:i+2*nslice]:
                count += 1   #중복된 횟수
            elif count > 1:   #문자열이 압축된 경우
                zip_string.append(str(count))
                zip_string.append(s[i:i+nslice])
                count = 1
            else:   #압축된게 없는 경우
                zip_string.append(s[i:i+nslice])
            i += nslice

        if s[i:len(s)] != '':   #비교 끝난 후 나머지 문자열 추가
            zip_string.append(s[i:len(s)])
        
        length = len(''.join(zip_string))   #리스트를 문자열로 변환해 길이 추출
        
        if result > length:   #전보다 문자열의 길이가 줄었을 경우 result 갱신
            result = length
        
        nslice += 1   #nslice값 증가하여 비교
        
    return result