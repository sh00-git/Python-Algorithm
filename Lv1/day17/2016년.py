# https://school.programmers.co.kr/learn/courses/30/lessons/12901
def solution(a, b):
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = 0
    for i in range(1, a):
        day += month[i-1]
    day += b
    return week[(day % 7)-1]