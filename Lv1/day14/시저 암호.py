# https://school.programmers.co.kr/learn/courses/30/lessons/12926
def solution(s, n):
    answer = ''
    for i in s:
        if ord(i) == 32: # 공백이면
            answer += ' '
        elif ord(i) >= 97: # 소문자면
            if (ord(i) + n) > 122:
                answer += (chr(ord(i) + n - 26))
            else:
                answer += (chr(ord(i)+n))
        else: # 대문자면
            if (ord(i) + n) > 90:
                answer += (chr(64 + n - (90 - ord(i))))
            else:
                answer += (chr(ord(i)+n))
    return answer