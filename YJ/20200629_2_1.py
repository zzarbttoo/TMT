#풀이 1 
def solution(phone_book):

    answer = True
    phone_book = sorted(phone_book)
    for i in range(0, len(phone_book)):
        for j in range (i+1, len(phone_book)):

            if phone_book[j].startswith(phone_book[i]):
                #바로 return 을 하면 효율성 테스트를 통과할 수 있다
                return False 
    return answer 



#sorted를 하지 않을 경우 이 두개를 구분할 수 없다(순차적으로 비교하기 때문)
print(solution(["119", "1192456"]))
print(solution(["1192456", "119"]))

print(solution(["11"]))
print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))

#API 확인을 생활화하자! : https://docs.python.org/ko/3/library/index.html
# 다중 반복문 탈출 : https://m.blog.naver.com/PostView.nhn?blogId=upssuyo&logNo=80092174516&proxyReferer=https:%2F%2Fwww.google.com%2F