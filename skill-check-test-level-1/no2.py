def solution(n):
    answer = int(''.join(sorted(str(n), reverse=True)))
    return answer


s = int(input())
print(solution(s))