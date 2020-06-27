#?�??1 : 근데 ?�거 ?�니????문제 ?�을 ?�해 못하겠어

# def solution(citiations):
	
# 	sum = 0
	
# 	for i in sorted(citiations):
		
# 		if i == (len(citiations) - sum):
# 			return i
# 		sum+=1
	

#?�??2 

def solution(citiations):

    
    citiations=sorted(citiations, reverse = True)
    if len(citiations) == 0: return None
    if citiations[0] == 0: return 0

    for i in range(citiations[0], 0, -1):
        t= len([x for x in citiations if x>=i])

        if(t >= i and len(citiations) - t <= i):
            return i
        

    

citations1 = [3, 0, 6, 1, 5]
citations2 = [1,2, 3, 5, 6]

citations3 = [0, 1, 3, 5, 5, 5, 5, 5, 5, 6]
citations4 = [0, 1, 1, 1, 1, 3, 3, 4] 
citations5 = [5, 5, 5, 5] 
citations6 = [] 

citations7 = [0, 0, 0, 0] 

print(solution(citations1))
print(solution(citations2))
print(solution(citations3))
print(solution(citations4))
print(solution(citations5))
print(solution(citations6))
print(solution(citations7))



#리스?�에???�하???�소�?출력 : https://coding-groot.tistory.com/21

# 다른 사람의 풀이(깔꼬롬)
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0