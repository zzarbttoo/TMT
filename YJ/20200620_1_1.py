
# 내 풀이
#for문을 두번 돌린 아주 안 좋은 코드인듯
def solution(array, commands):
	answer = []
	
	
	
	for i in commands:
		temp_array=[]
		for j in range(i[0]-1 , i[1]):
			temp_array.append(array[j])
		 
		temp_array = sorted(temp_array)
		answer.append(temp_array[i[2]-1])

	return answer



array1 = [1, 5, 2, 6, 3, 7, 4]
commands1 = [[2, 5, 3], [4,4,1], [1, 7, 3]]

print(solution(array1, commands1))

#다른 사람 1
#map과 lambda x 식을 활용해서 풀었다
#1. lambda x를 이용해 sorted 된 array를 한번에 입력 -> 이 때 commands[0], commands[1], commands[2] 가 변수이므로 
#commands -> x 로 놓음
#2. map 함수를 이용해 commands[0], commands[1], commands[2] 를 한번에 표현
#3. list로 반환
def solution2(array, commands):
    return  list(map(lambda x : sorted(array[x[0]-1: x[1]])[x[2]-1] , commands))

print(solution2(array1, commands1))


#다른 사람 2
# command[] 내부의 리스트의 내용을 변수로 한번에 입력할 수 있다는 사실!
def solution3(array, commands):
    answer=[]

    for command in commands:
        #안의 내용을 변수에 한번에 입력함
        i, j, k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])