def solution(genres, plays):
    answer = []
    genre={}
    gen=list(set(genres))           #장르 추출(중복 제거)
    play={}
    for g in range(len(genres)):    #초기값 설정
        genre[genres[g]]=[]
        play[genres[g]]=0
    for i in range(len(genres)):
        play[genres[i]]+=plays[i]   #장르별 총 플레이 횟수 계산
        genre[genres[i]].append(i)  #장르별 노래의 고유번호 입력
    for j in range(len(gen)):
        genre[gen[j]].append(play[gen[j]])    #장르별 노래의 고유번호 집합과 장르별 총 플레이 횟수를 붙여줌
    genre=sorted(genre.items(),key=(lambda x: x[1][-1]),reverse=True) #노래가 많이 재생된 장르 순으로 정렬
    for i in range(len(gen)):
        genre[i][1].pop()           #총 플레이 횟수를 없애줌(이제 필요없는 정보)
        genre[i]=genre[i][1]        #3차원 list를 2차원으로 바꿔줌
        genre[i]=sorted(genre[i], key=(lambda x: plays[x]),reverse=True) #장르 내에서 재생 횟수순으로 정렬
    for i in range(len(genre)):
        for j in range(2):                  #2개만 뽑아줌
            answer.append(genre[i][j])      #i번째 장르에서 j번째 음악을 추출
            if len(genre[i])==1:            #장르에 노래가 하나면 끝냄
                break
    return answer

    '''해쉬를 처음 제대로 써봐서 그런지 불필요한 요소가 많이 들어간것 같네요ㅠㅠ'''
