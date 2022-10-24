# https://school.programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    answer = []
    while len(s) > 0:
        if s[0] == 'z':
            s = s[4:]
            answer.append('0')
        elif s[0] == 'o':
            s = s[3:]
            answer.append('1')
        elif s[:2] == 'tw':
            s = s[3:]
            answer.append('2')
        elif s[:2] == 'th':
            s = s[5:]
            answer.append('3')
        elif s[:2] == 'fo':
            s = s[4:]
            answer.append('4')
        elif s[:2] == 'fi':
            s = s[4:]
            answer.append('5')
        elif s[:2] == 'si':
            s = s[3:]
            answer.append('6')
        elif s[:2] == 'se':
            s = s[5:]
            answer.append('7')
        elif s[0] == 'e':
            s = s[5:]
            answer.append('8')
        elif s[0] == 'n':
            s = s[4:]
            answer.append('9')
        else:
            answer.append(s[0])
            s = s[1:]
    
    answer = int(''.join(answer))
    return answer

# dictionary를 활용한 풀이
# dictionary의 items()함수 사용법을 익힐 수 있었다.
def solution(s):
    num_dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 
               'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    for key, value in num_dic.items():
        s = s.replace(key, value)
    return int(s)