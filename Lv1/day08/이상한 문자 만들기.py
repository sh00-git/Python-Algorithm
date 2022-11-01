# https://school.programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    s = s.split(' ')
    
    for i in range(len(s)):
        answer = []
        for j in range(len(s[i])):
            if j % 2 == 0:
                answer.append(s[i][j].upper())
            else:
                answer.append(s[i][j].lower())
        s[i] = ''.join(answer)
    s = ' '.join(s)

    return s