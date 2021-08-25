import numpy as np

POSITIVE_ZERO = 1e-7
MINUS_ZERO = -1e-7
BIG_M = float(65536)


def dual_simplex_solve(init_simplex_tableau, basic_variable_idxs):
    M = init_simplex_tableau
    print(M)
    print("基变量：", basic_variable_idxs)
    while (M[: -1, -1] < MINUS_ZERO).any():
        r = np.argmin(M[: -1, -1])
        ratios = [column[-1] / column[r] if column[r] < MINUS_ZERO else np.inf for column in M[:, :-1].T]
        # print(ratios)
        if all([ratio == np.inf for ratio in ratios]):
            print("无最优解(最优解无界)！")
            return
        c = np.argmin(ratios)
        print("选中：", r, "行", c, "列\n")
        M[r] = M[r] / M[r, c]
        for row in M[:r]:
            row -= np.dot(row[c], M[r])
        for row in M[r + 1:]:
            row -= np.dot(row[c], M[r])
        basic_variable_idxs[r.item()] = c
        print(M)
        print("基变量：", basic_variable_idxs)
    end_simplex_tableau = M
    return end_simplex_tableau, basic_variable_idxs


def simplex_solve(init_simplex_tableau, basic_variable_idxs):
    M = init_simplex_tableau
    print(M)
    print("基变量：", basic_variable_idxs)
    while (M[-1, :-1] > POSITIVE_ZERO).any():
        c = np.argmax(M[-1, :-1])
        ratios = [row[-1] / row[c] if row[c] > POSITIVE_ZERO else np.inf for row in M[:len(basic_variable_idxs)]]
        if all([ratio == np.inf for ratio in ratios]):
            print("无最优解(最优解无界)！")
            return
        r = np.argmin(ratios)
        print("选中：", r, "行", c, "列\n")
        M[r] = M[r] / M[r, c]
        for row in M[:r]:
            row -= np.dot(row[c], M[r])
        for row in M[r + 1:]:
            row -= np.dot(row[c], M[r])
        basic_variable_idxs[r.item()] = c
        print(M)
        print("基变量：", basic_variable_idxs)
    end_simplex_tableau = M
    return end_simplex_tableau, basic_variable_idxs
