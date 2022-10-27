# https://school.programmers.co.kr/learn/courses/30/lessons/12922
def solution(n):
    answer = []
    for i in range(n):
        if i % 2 == 0:
            answer.append('수')
        else:
            answer.append('박')
    answer = ''.join(answer)
    return answer

# string의 합이 가능하므로 다음과 같은 방법도 가능
def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer