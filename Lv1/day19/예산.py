# https://school.programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    answer = 0
    sum = 0
    for _ in range(len(d)):
        sum += min(d)
        if sum > budget:
            break
        else:
            answer+=1
            d.remove(min(d))
    return answer

# d를 먼저 sorted 한 후 for문으로 하나씩 확인하면 진행하는 방법도 생각하였으나, d의 길이가 길어지면 sorted할때 들어가는 시간이 오래걸릴 것 같다고 생각함.