def solution(s):
    nmg = len(s) % 2
    mok = len(s) // 2
    if nmg:
        answer = s[mok]
    else:
        answer = s[mok - 1: mok + 1]
    return answer


word = input()
print(solution(word))
