# coding: utf-8

from itertools import combinations
import numpy as np


class BasicFeasibleSolver:

    def __init__(self, A, b, c, mode):
        """ 初始化基本可行解求解器
        :param A: A矩阵，m×n的np.array，需要自行添加松弛变量
        :param b: b向量，m×1的np.array
        :param c: 优化目标函数的系数向量，1×n的np.array，需要自行添加松弛变量
        :param mode: 最大还是最小化目标函数，"max"或"min"
        """
        self.A = A
        self.b = b
        self.c = c
        self.row_num, self.column_num = A.shape
        self.update_condition = None
        if mode == "max":
            self.update_condition = lambda l, r: l > r
        elif mode == "min":
            self.update_condition = lambda l, r: l < r
        else:
            print("Mode can only be min and max! Default min.")
            self.update_condition = lambda l, r: l < r

    def solve(self):
        memory = {"collection": None,
                  "z": 0,
                  "x_B": None}
        for combination in combinations(range(self.column_num), self.row_num):
            B = self.A[:, combination]
            x_B = np.dot(np.linalg.inv(B), self.b)
            z = np.dot(self.c[:, combination], x_B).item()
            if (x_B >= 0).all():
                if self.update_condition(z, memory["z"]):
                    memory["collection"] = combination
                    memory["z"] = z
                    memory["x_B"] = x_B
        x = np.zeros((self.column_num, 1))
        x[memory["collection"], 0] = memory["x_B"].reshape(1, -1)
        return x, memory["z"]


def try_it():
    A = np.array([[1, 2, 1, 0, 0],
                  [2, -1, 0, 1, 0],
                  [1, -4, 0, 0, 1]])
    b = np.array([[10],
                  [5],
                  [4]])
    c = np.array([[5, -6, 0, 0, 0]])
    solver = BasicFeasibleSolver(A, b, c, "min")
    x, z = solver.solve()
    print(x)
    print(z)


if __name__ == "__main__":
    try_it()
