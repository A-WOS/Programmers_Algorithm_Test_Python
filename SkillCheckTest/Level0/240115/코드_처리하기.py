def solution(code):
    ret = ''
    idx, mode = 0, 0
    while idx < len(code):
        if mode == 0:
            if code[idx] != "1" and idx % 2 == 0:
                ret += code[idx]
            elif code[idx] == "1":
                mode = 1
        elif mode == 1:
            if code[idx] != "1" and idx % 2:
                ret += code[idx]
            elif code[idx] == "1":
                mode = 0
        idx += 1

    return "EMPTY" if ret == '' else ret


print(solution("abc1abc1abc"))  # "acbac"
