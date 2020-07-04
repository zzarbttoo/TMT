# 2주차 5번 베스트 앨범

from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_dict = defaultdict(int) # value가 없으면 0으로
    play_dict = defaultdict(list) # value가 없으면 []로

    for i, (g, p) in enumerate(zip(genres, plays)):
        play_dict[g].append((p, i)) # 장르별 각 곡의 플레이 수, 고유번호 저장
        genre_dict[g] += p # 장르별 총 플레이 수
    
    # 장르별 총 플레이 수가 큰 것부터 정렬
    sorted_genre = sorted(genre_dict.items(), key=lambda item: item[1], reverse=True)

    for genre in sorted_genre:
        # 장르별 각 플레이 수가 큰 것부터 정렬
        sorted_play = sorted(play_dict[genre[0]], key=lambda item: item[0], reverse=True)
        for i in range(2):
            answer.append(sorted_play[i][1])
            if len(sorted_play) == 1:
                break
    return answer