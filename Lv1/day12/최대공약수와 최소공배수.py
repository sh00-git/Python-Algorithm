# https://school.programmers.co.kr/learn/courses/30/lessons/12940
def solution(n, m):
    answer = []
    for i in range(min(n, m), 0, -1):
        if (n%i==0) & (m%i==0):
            answer.append(i)
            answer.append(i * (n//i) * (m//i))
            break
    return answer