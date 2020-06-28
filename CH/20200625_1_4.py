def solution(numbers):
    number=''
    b=sorted([str(q) for q in numbers], reverse= True)   #문자형식으로 변환후 소팅
    for num in b:                                        #추가
        number+=num
    number=int(number)
    return str(number)


'''다른 것들은 잘되는데 3과 30이나 11이나 110같은 숫자는 원하는대로 소팅이 안됨ㅠㅠ'''
