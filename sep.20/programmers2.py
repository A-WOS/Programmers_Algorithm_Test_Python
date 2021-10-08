def solution(a, b, g, s, w, t):
    # x = [for i in range(len(g))]
    x = len(g)
    #   왕복
    answer = [i for i in range(x)]
    print(w[x - 1], type(w[x - 1]))
    for i in range(x):
        a1 = a
        b1 = b
        while True:
            if a1 <= 0 and b1 <= 0:
                break
            elif 0 < a1 + b1 < w[i]:
                answer[i] += t[i]
                a1 -= w[i]
                b1 -= w[i]
            elif a1 > w[i] and b1 > w[i]:
                a1 -= w[i]
                b1 -= w[i]
                answer[i] += t[i] * 2

            elif a1 < w[i] < b1:
                b1 -= w[i]
                answer[i] += t[i]
            elif b1 < w[i] < a1:
                a1 -= w[i]
                answer[i] += t[i]

            if a1 >= 0:
                answer[i] += t[i]
            if b1 >= 0:
                answer[i] += t[i]

    return max(answer)


# a = 10
# b = 10
# g = [100]
# s = [100]
# w = [7]
# t = [10]

a = 90
b = 500
g = [70, 70, 0]
s = [0, 0, 500]
w = [100, 100, 2]
t = [4, 8, 1]

print(len(g), len(s), len(w), len(t))
# print(numbers)
print(solution(a, b, g, s, w, t))
