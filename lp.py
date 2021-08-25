from solvers import *
from inequality import *


class LP:
    def __init__(self, variables, inequalities, obj_fn, mode):
        self.inequalities = inequalities
        self.obj_fn = obj_fn
        self.mode = mode
        self.variables = variables
        self.basic_variables = []
        self.non_basic_variables = []
        self.artificial_variables = []
        for variable in self.variables:
            coefficients = [inequality.LHS.get_coefficient(variable) for inequality in self.inequalities]
            if sum([bool(coefficient) for coefficient in coefficients]) == 1:
                for idx, coefficient in enumerate(coefficients):
                    if coefficient == 1:
                        self.basic_variables.append(variable)
        for variable in self.variables:
            if variable not in self.basic_variables:
                self.non_basic_variables.append(variable)
        print("创建LP问题：")
        print(self)

    def __str__(self):
        string = self.mode + " z = " + str(self.obj_fn) + "\ns.t."
        for inequality in self.inequalities:
            string += "\n\t" + str(inequality)
        return string + '\n'

    def add_slack_variables(self):
        print("添加松弛变量：")
        for idx, inequality in enumerate(self.inequalities):
            if inequality.type == "<=":
                s = NonMinusVariable("s" + str(idx))
                inequality.LHS.add_items(s)
                self.variables.append(s)
                self.basic_variables.append(s)
                inequality.type = "="
            elif inequality.type == ">=":
                s = NonMinusVariable("s" + str(idx))
                inequality.LHS.add_items(-s)
                self.variables.append(s)
                inequality.type = "="
        print(self)

    def add_artificial_variables(self, mode="two_phase"):
        print("添加人工变量：")
        artificial_flags = [True for _ in self.inequalities]
        for variable in self.variables:
            coefficients = [inequality.LHS.get_coefficient(variable) for inequality in self.inequalities]
            if sum([bool(coefficient) for coefficient in coefficients]) == 1:
                for idx, coefficient in enumerate(coefficients):
                    if coefficient == 1:
                        artificial_flags[idx] = False
        for idx, flag in enumerate(artificial_flags):
            if flag:
                a = NonMinusVariable("a" + str(idx))
                self.inequalities[idx].LHS.add_items(a)
                self.variables.append(a)
                self.basic_variables.append(a)
                self.artificial_variables.append(a)
                if mode == "big_m":
                    self.obj_fn.add_items(a * (BIG_M * (-1 if self.mode == "max" else 1)))
        print(self)

    def get_init_simplex_tableau(self):
        inequality_num = len(self.inequalities)
        variable_num = len(self.variables)
        init_simplex_tableau = np.zeros((inequality_num + 1, variable_num + 1))
        for i, inequality in enumerate(self.inequalities):
            for coefficient, variable in inequality.LHS:
                init_simplex_tableau[i, self.variables.index(variable)] = coefficient
            init_simplex_tableau[i, -1] = inequality.RHS
        sign = -1 if self.mode == "min" else 1
        for coefficient, variable in self.obj_fn:
            init_simplex_tableau[-1, self.variables.index(variable)] = sign * coefficient
        basic_variable_idxs = []
        for row in init_simplex_tableau[: -1]:
            for basic_variable in self.basic_variables:
                basic_variable_idx = self.variables.index(basic_variable)
                if row[basic_variable_idx] == 1:
                    basic_variable_idxs.append(basic_variable_idx)
                    break
        init_simplex_tableau[-1] -= np.dot(init_simplex_tableau[-1][basic_variable_idxs], init_simplex_tableau[:-1, :])
        return init_simplex_tableau, basic_variable_idxs

    def big_m_solve(self):
        self.add_slack_variables()

        for inequality in self.inequalities:
            if inequality.RHS < 0:
                inequality.RHS *= -1
                for item in inequality.LHS:
                    item[0] *= -1
        print("等号右边变为正数:")
        print(self)

        self.add_artificial_variables(mode="big_m")

        print("开始求解：")
        init_simplex_tableau, basic_variable_idxs = self.get_init_simplex_tableau()
        np.set_printoptions(formatter={'float': '{: 12.4f}'.format})

        end_simplex_tableau, basic_variable_idxs = simplex_solve(init_simplex_tableau, basic_variable_idxs)

        solution = np.zeros(end_simplex_tableau.shape[1] - 1)
        for i, basic_variable_idx in enumerate(basic_variable_idxs):
            solution[basic_variable_idx] = end_simplex_tableau[i, -1]
        best_value = end_simplex_tableau[-1, -1] * (-1 if self.mode == "max" else 1)
        print("最优解为：", solution, "\n最优值为：", best_value, "\n")

        return solution, best_value, end_simplex_tableau, basic_variable_idxs

    def two_phase_solve(self):
        self.add_slack_variables()

        for inequality in self.inequalities:
            if inequality.RHS < 0:
                inequality.RHS *= -1
                for item in inequality.LHS:
                    item[0] *= -1
        print("等号右边变为正数:")
        print(self)

        self.add_artificial_variables(mode="two_phase")

        init_simplex_tableau, basic_variable_idxs = self.get_init_simplex_tableau()
        np.set_printoptions(formatter={'float': '{: 12.4f}'.format})

        if not self.artificial_variables:
            print("无人工变量, 开始求解第二阶段：")
            end_simplex_tableau, basic_variable_idxs = simplex_solve(init_simplex_tableau, basic_variable_idxs)

            solution = np.zeros(end_simplex_tableau.shape[1] - 1)
            for i, basic_variable_idx in enumerate(basic_variable_idxs):
                solution[basic_variable_idx] = end_simplex_tableau[i, -1]
            best_value = end_simplex_tableau[-1, -1] * (-1 if self.mode == "max" else 1)
            print("最优解为：", solution, "\n最优值为：", best_value, "\n")

            return solution, best_value, end_simplex_tableau, basic_variable_idxs

        print("开始求解第一阶段：")
        artificial_variable_idxs = [self.variables.index(variable) for variable in self.artificial_variables]
        artificial_row_idxs = [basic_variable_idxs.index(artificial_variable_idx)
                               for artificial_variable_idx in artificial_variable_idxs]
        init_simplex_tableau = np.r_[init_simplex_tableau,
                                     np.sum(init_simplex_tableau[artificial_row_idxs], 0).reshape(1, -1)]
        init_simplex_tableau[-1, artificial_variable_idxs] = 0

        end_simplex_tableau, basic_variable_idxs = simplex_solve(init_simplex_tableau, basic_variable_idxs)

        if end_simplex_tableau[-1, -1] > POSITIVE_ZERO or end_simplex_tableau[-1, -1] < MINUS_ZERO:
            print("无基本可行解！")
        else:
            solution = np.zeros(end_simplex_tableau.shape[1] - 1)
            for i, basic_variable_idx in enumerate(basic_variable_idxs):
                solution[basic_variable_idx] = end_simplex_tableau[i, -1]
            print("得到一个基本可行解：", solution[: -len(artificial_variable_idxs)])
            init_simplex_tableau = np.delete(end_simplex_tableau, artificial_variable_idxs, 1)[: -1]

            for idx, basic_variable_idx in enumerate(basic_variable_idxs):
                if basic_variable_idx in artificial_variable_idxs:
                    init_simplex_tableau = np.delete(init_simplex_tableau, idx, 0)
                    basic_variable_idxs.remove(basic_variable_idx)

            print("新的初始单纯形表：")
            end_simplex_tableau, basic_variable_idxs = simplex_solve(init_simplex_tableau, basic_variable_idxs)

            solution = np.zeros(end_simplex_tableau.shape[1] - 1)
            for i, basic_variable_idx in enumerate(basic_variable_idxs):
                solution[basic_variable_idx] = end_simplex_tableau[i, -1]
            best_value = end_simplex_tableau[-1, -1] * (-1 if self.mode == "max" else 1)
            print("最优解为：", solution, "\n最优值为：", best_value, "\n")

            return solution, best_value, end_simplex_tableau, basic_variable_idxs

    def dual_solve(self):
        print("改变符号：")
        for inequality in self.inequalities:
            if inequality.type == ">=":
                inequality.type = "<="
                inequality.RHS *= -1
                for item in inequality.LHS.items:
                    item[0] *= -1
        print(self)

        expand_flag = False

        if self.mode == "max":
            if any([item[0] > 0 for item in self.obj_fn.items]):
                expand_flag = True
                print("构造扩充问题,")
                self.inequalities.append(Inequality([[1, variable] for variable in self.non_basic_variables],
                                                    "<=", BIG_M))
        elif self.mode == "min":
            if any([item[0] < 0 for item in self.obj_fn.items]):
                expand_flag = True
                print("构造扩充问题,")
                self.inequalities.append(Inequality([[1, variable] for variable in self.non_basic_variables],
                                                    "<=", BIG_M))

        self.add_slack_variables()

        print("开始求解：")
        init_simplex_tableau, basic_variable_idxs = self.get_init_simplex_tableau()
        np.set_printoptions(formatter={'float': '{: 12.4f}'.format})

        if expand_flag:
            print(init_simplex_tableau)
            print("求解扩充问题")
            c = np.argmax(init_simplex_tableau[-1, :-1])
            print("选中第", c, "列")
            init_simplex_tableau[-2] = init_simplex_tableau[-2] / init_simplex_tableau[-2, c]
            for row in init_simplex_tableau[:-2]:
                row -= np.dot(row[c], init_simplex_tableau[-2])
            init_simplex_tableau[-1] -= np.dot(init_simplex_tableau[-1][c], init_simplex_tableau[-2])
            basic_variable_idxs[-1] = c

        print("对偶单纯形法：")
        end_simplex_tableau, basic_variable_idxs = dual_simplex_solve(init_simplex_tableau, basic_variable_idxs)

        solution = np.zeros(end_simplex_tableau.shape[1] - 1)
        for i, basic_variable_idx in enumerate(basic_variable_idxs):
            solution[basic_variable_idx] = end_simplex_tableau[i, -1]
        best_value = end_simplex_tableau[-1, -1] * (-1 if self.mode == "max" else 1)
        print("最优解为：", solution, "\n最优值为：", best_value, "\n")

        return solution, best_value, end_simplex_tableau, basic_variable_idxs

    def modify_b(self, end_simplex_tableau, basic_variable_idxs, new_b):
        inverse_B = end_simplex_tableau[: -1, ([self.variables.index(variable) for variable in self.basic_variables])]
        b_bar = np.dot(inverse_B, new_b)
        print("修改右端向量为：\n", inverse_B, "·\n", new_b, "=\n", b_bar)
        end_simplex_tableau[: -1, -1:] = b_bar
        end_simplex_tableau[-1, -1] = 0
        for item in self.obj_fn:
            if self.variables.index(item[1]) in basic_variable_idxs:
                if self.mode == "min":
                    end_simplex_tableau[-1, -1] += \
                        b_bar[basic_variable_idxs.index(self.variables.index(item[1]))] * item[0]
                else:
                    end_simplex_tableau[-1, -1] -= \
                        b_bar[basic_variable_idxs.index(self.variables.index(item[1]))] * item[0]
        print("右下角修改为：", end_simplex_tableau[-1, -1])
        print("用对偶单纯形法求解：")
        end_simplex_tableau, basic_variable_idxs = dual_simplex_solve(end_simplex_tableau, basic_variable_idxs)
        solution = np.zeros(end_simplex_tableau.shape[1] - 1)
        for i, basic_variable_idx in enumerate(basic_variable_idxs):
            solution[basic_variable_idx] = end_simplex_tableau[i, -1]
        best_value = end_simplex_tableau[-1, -1] * (-1 if self.mode == "max" else 1)
        print("最优解为：", solution, "\n最优值为：", best_value, "\n")

    def modify_c(self, end_simplex_tableau, basic_variable_idxs, variable, param):
        if self.variables.index(variable) in basic_variable_idxs:
            print(variable, "是基变量")
            r = basic_variable_idxs.index(self.variables.index(variable))
            if self.mode == "min":
                end_simplex_tableau[-1] += (param - self.obj_fn.get_coefficient(variable)) * end_simplex_tableau[r]
                print("将第", r, "行", param - self.obj_fn.get_coefficient(variable), "倍加到检验数行")
            elif self.mode == "max":
                end_simplex_tableau[-1] -= (param - self.obj_fn.get_coefficient(variable)) * end_simplex_tableau[r]
                print("将第", r, "行", param - self.obj_fn.get_coefficient(variable), "倍减到检验数行")
            end_simplex_tableau[-1, self.variables.index(variable)] = 0
            if (end_simplex_tableau[-1] > 0).any():
                print("存在判别数 > 0，继续迭代")
            else:
                print("判别数都 <= 0，最优解不变")

        else:
            print(variable, "非基变量")
            if self.mode == "max":
                end_simplex_tableau[-1, self.variables.index(variable)] += param - self.obj_fn.get_coefficient(variable)
            elif self.mode == "min":
                end_simplex_tableau[-1, self.variables.index(variable)] -= param - self.obj_fn.get_coefficient(variable)
            print(variable, "判别数修改为：", end_simplex_tableau[-1, self.variables.index(variable)])
            if end_simplex_tableau[-1, self.variables.index(variable)] > 0:
                print("判别数 > 0，继续迭代")
            else:
                print("判别数 <= 0，最优解不变")
                # return

        print("用单纯形法求解：")
        end_simplex_tableau, basic_variable_idxs = simplex_solve(end_simplex_tableau, basic_variable_idxs)
        solution = np.zeros(end_simplex_tableau.shape[1] - 1)
        for i, basic_variable_idx in enumerate(basic_variable_idxs):
            solution[basic_variable_idx] = end_simplex_tableau[i, -1]
        best_value = end_simplex_tableau[-1, -1] * (-1 if self.mode == "max" else 1)
        print("最优解为：", solution, "\n最优值为：", best_value, "\n")

    def modify_A(self, end_simplex_tableau, basic_variable_idxs, variable, new_p):
        if self.variables.index(variable) in basic_variable_idxs:
            print("要修改的列为基列，请新建lp计算")
            return
        end_simplex_tableau[-1, self.variables.index(variable)] = \
            self.obj_fn.get_coefficient(variable) * (-1 if self.mode == "min" else 1)
        inverse_B = end_simplex_tableau[: -1, ([self.variables.index(variable) for variable in self.basic_variables])]
        c_B = np.array([self.obj_fn.get_coefficient(self.variables[basic_variable_idx])
                        for basic_variable_idx in basic_variable_idxs])
        if self.mode == "max":
            print(variable, "判别数修改为", end_simplex_tableau[-1, self.variables.index(variable)], "减去")
            end_simplex_tableau[-1, self.variables.index(variable)] -= np.dot(c_B, np.dot(inverse_B, new_p))
        else:
            print(variable, "判别数修改为", end_simplex_tableau[-1, self.variables.index(variable)], "加上")
            end_simplex_tableau[-1, self.variables.index(variable)] += np.dot(c_B, np.dot(inverse_B, new_p))
        print(c_B, "·\n", inverse_B, "·\n", new_p, "=\n", np.dot(c_B, np.dot(inverse_B, new_p)).item())
        print("修改为", end_simplex_tableau[-1, self.variables.index(variable)])
        if end_simplex_tableau[-1, self.variables.index(variable)] <= 0:
            print("判别数仍 <= 0，最优解不变")
        else:
            print("判别数 > 0，继续迭代")

        print("用单纯形法求解：")
        end_simplex_tableau, basic_variable_idxs = simplex_solve(end_simplex_tableau, basic_variable_idxs)
        solution = np.zeros(end_simplex_tableau.shape[1] - 1)
        for i, basic_variable_idx in enumerate(basic_variable_idxs):
            solution[basic_variable_idx] = end_simplex_tableau[i, -1]
        best_value = end_simplex_tableau[-1, -1] * (-1 if self.mode == "max" else 1)
        print("最优解为：", solution, "\n最优值为：", best_value, "\n")

    def modify_by_adding_constraints(self, end_simplex_tableau, basic_variable_idxs, new_inequality):
        if new_inequality.type != "<=":
            print("目前只接受添加<=约束")
            return
        LHS = 0
        for item in new_inequality.LHS:
            if self.variables.index(item[1]) in basic_variable_idxs:
                LHS += item[0] * end_simplex_tableau[basic_variable_idxs.index(self.variables.index(item[1])), -1]
        print("LHS = ", LHS, "; RHS = ", new_inequality.RHS)
        if new_inequality.type == ">=" and LHS >= new_inequality.RHS:
            print("原最优解满足新约束")
            return
        if new_inequality.type == "=" and LHS == new_inequality.RHS:
            print("原最优解满足新约束")
            return
        if new_inequality.type == "<=" and LHS <= new_inequality.RHS:
            print("原最优解满足新约束")
            return
        print("原最优解不满足新约束，将新约束加进单纯形表")
        LU = end_simplex_tableau[: -1, : -1]
        RU = end_simplex_tableau[: -1, -1:]
        LD = end_simplex_tableau[-1:, : -1]
        RD = end_simplex_tableau[-1:, -1:]
        LU = np.c_[LU, np.zeros((LU.shape[0], 1))]
        LU = np.r_[LU, np.zeros((1, LU.shape[1]))]
        for item in new_inequality.LHS:
            LU[-1, self.variables.index(item[1])] = item[0]
        LU[-1, -1] = 1
        RU = np.r_[RU, np.array([[new_inequality.RHS]])]
        LD = np.c_[LD, np.array([[0]])]
        end_simplex_tableau = np.r_[np.c_[LU, RU], np.c_[LD, RD]]
        print("得到新的单纯形表：\n", end_simplex_tableau)
        for idx, basic_variable_idx in enumerate(basic_variable_idxs):
            if end_simplex_tableau[-2, basic_variable_idx] > POSITIVE_ZERO or \
                    end_simplex_tableau[-2, basic_variable_idx] < MINUS_ZERO:
                end_simplex_tableau[-2] -= end_simplex_tableau[-2, basic_variable_idx] * end_simplex_tableau[idx]
                print("消元")
        basic_variable_idxs.append(LU.shape[1] - 1)

        print("用单纯形法求解：")
        end_simplex_tableau, basic_variable_idxs = dual_simplex_solve(end_simplex_tableau, basic_variable_idxs)
        solution = np.zeros(end_simplex_tableau.shape[1] - 1)
        for i, basic_variable_idx in enumerate(basic_variable_idxs):
            solution[basic_variable_idx] = end_simplex_tableau[i, -1]
        best_value = end_simplex_tableau[-1, -1] * (-1 if self.mode == "max" else 1)
        print("最优解为：", solution, "\n最优值为：", best_value, "\n")
