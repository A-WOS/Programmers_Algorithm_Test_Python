def solution(scores):
    avg = []
    answer = ''
    eval_l = [[scores[i][j] for i in range(len(scores))] for j in range(len(scores))]
    for i in range(len(eval_l)):
        if eval_l[i][i] == max(eval_l[i]) and eval_l[i].count(max(eval_l[i])) == 1:
            eval_l[i].remove(eval_l[i][i])
        elif eval_l[i][i] == min(eval_l[i]) and eval_l[i].count(min(eval_l[i])) == 1:
            eval_l[i].remove(eval_l[i][i])
        else:
            continue
    avg += [sum(eval_l[i]) / len(eval_l[i]) for i in range(len(eval_l))]
    for score in avg:
        if score >= 90:
            answer += 'A'
        elif 80 <= score < 90:
            answer += 'B'
        elif 70 <= score < 80:
            answer += 'C'
        elif 50 <= score < 70:
            answer += 'D'
        else:
            answer += 'F'
    return answer


print(solution(
    [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))
print(solution([[50, 90], [50, 87]]))
print(solution([[70, 49, 90], [68, 50, 38], [73, 31, 100]]))
