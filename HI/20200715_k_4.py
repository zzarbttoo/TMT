# 4주차 k사 가사 검색

def check(Q, words):
    answer, count = 0, 0
    if Q[0] == '?':
        count = Q.count('?')
        string = Q[count:]
        for w in words:
            if w[count:] == string and len(w[:count]) == count:
                answer += 1
        return answer
    else:
        while Q[count] != '?':
            count += 1
        string = Q[:count]
        for w in words:
            if w[:count] == string and len(w[count:]) == (len(Q)-count):
                answer += 1
        return answer

def solution(words, queries):
    answer = []
    for Q in queries:
        answer.append(check(Q, words))
    return answer

'''정확성 테스트는 통과했지만 효율성 테스트를 통과하지 못함'''

# 공간복잡도가 작은 트라이(Trie) 구조 사용
# 출처: https://blog.ilkyu.kr/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-Trie-%ED%8A%B8%EB%9D%BC%EC%9D%B4-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0?category=684084

class Node: #각 문자를 저장하기 위한 노드
    def __init__(self, key):
        self.key = key
        self.count = 0
        self.child = {} #딕셔너리

class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def add(self, word):
        cur = self.head
        for ch in word:
            cur.count += 1
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
        cur.child['*'] = True #문자열 마지막에 '*' 삽입
    
    def search(self, word):
        cur = self.head

        for ch in word:
            if ch == '?':
                return cur.count
            if ch not in cur.child:
                return 0
            cur = cur.child[ch]
        if '*' in cur.child:
            return 1

def solution(words, queries):
    answer = []
    trie = [Trie() for i in range(0,10001)]
    rev_trie = [Trie() for i in range(0,10001)]

    for w in words:
        trie[len(w)].add(w)
        rev_trie[len(w)].add(w[::-1])
    
    for q in queries:
        if q[0] == '?':
            result = rev_trie[len(q)].search(q[::-1])
        else:
            result = trie[len(q)].search(q)
        if type(result) == int:
            answer.append(result)
        else:
            if result:
                answer.append(1)
            else:
                answer.append(0)
    return answer