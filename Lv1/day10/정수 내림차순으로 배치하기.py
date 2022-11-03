# https://school.programmers.co.kr/learn/courses/30/lessons/12933
def solution(n):
    n = list(str(n))
    for i in range(len(n)-1):
        for j in range(i+1, len(n)):
            if n[i] < n[j] :
                n[i], n[j] = n[j], n[i]
    return int(''.join(n))

# sorted 함수 사용
def solution(n):
    return int(''.join(sorted(list(str(n)), reverse = True)))

# sorted 하면 리스트로 반환되기 때문에 list 사용하지 않아도 됨.
def solution(n):
    return int(''.join(sorted(str(n), reverse = True)))
