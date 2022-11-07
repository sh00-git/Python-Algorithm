# https://school.programmers.co.kr/learn/courses/30/lessons/77884
def solution(left, right):
    answer = 0
    for i in range(left, right+1, 1):
        measure = 0
        for j in range(1, i+1):
            if i % j == 0:
                measure += 1
        if measure % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

## 약수의 개수가 홀수인 것들은 제곱수이다.
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i
    
    return answer