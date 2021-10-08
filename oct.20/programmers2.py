def solution(n, left, right):
    fake = []
    i_list = [x for x in range(1, n)]

    # print(i_list)
    # for i in range(n):
    #     for j in range(n):
    #         if i == j or i>j:
    #             fake[i][j] = i_list[i]
    #             fake[j][i] = i_list[i]

    print(fake)
    answer = []
    # for val in fake:
    #     answer += val
    # return answer[left:right+1]
    return


print(solution(3, 2, 5))
