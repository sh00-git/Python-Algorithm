# https://school.programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    answer = ''

    while n >= 1:
        n, rest = divmod(n, 3) # divmod(): 몫과 나머지를 같이 반환하는 함수
        answer += str(rest)

    answer = int(answer, 3) # int(x, base): base 진법으로 구성된 str 형식의 수를 10진법으로 변환

    return answer
