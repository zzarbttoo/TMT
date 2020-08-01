#2번 카펫
def solution(brown, yellow):
    total=brown+yellow            #총개수 = 브라운 + 옐로
    width=3                       #가로 길이는 3으로 시작(yellow가 최소 1이상이기 때문)
    while True :
        height=(brown+4)//2-width #높이는 이러하다
        if height*width==total:   #너비*높이가 총개수와 같을 때
            if width>=height :    #너비가 높이보다 크거나 같아지면 종료
                break
        width+=1                   
    return [width, height]
