# MyLPSolver
这是最优化课程的课程实践，基于numpy实现了几个线性规划的求解算法，如：
- 对偶单纯形法
- 两阶段法
- 大M法

还有灵敏度分析，包括：
- 改A
- 改b
- 改c
- 增加约束

程序会把计算过程输出出来，所以可以用这个抄(划掉)做作业

# Example
## 求解
```
from inequality import *
from lp import LP

if __name__ == "__main__":
    # 定义变量，要定义几个变量就写几个，记得都要添加到下面的 variables 里面
    x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    
    # 定义线性规划问题
    linear_programming = LP(
        inequalities=[  # 填写不等式组，注意只支持 ">="，"<=" 和 "="，其他符号都视作 "="
            Inequality(x1, "<=", 4),
            Inequality(x2, "<=", 6),
            Inequality(3 * x1 + 2 * x2, "<=", 18)
        ],
        mode="max",                          # 最大化还是最小化
        obj_fn=Polynomial(3 * x1 + 5 * x2),  # 目标函数
        variables=[x1, x2]                   # 照抄变量
    )
    
    # 选择你想用的算法来求解，有
    # 对偶单纯形法 .dual_solve()
    # 两阶段法     .two_phase_solve()
    # 大M法        .big_m_solve()
    solution, best_value, end_simplex_tableau, basic_variable_idxs = linear_programming.two_phase_solve()
    
    # 结果：
    # solution：           最优解
    # best_value：         最优值
    # end_simplex_tableau：最终的单纯性表
    # basic_variable_idxs：基变量的下标
```
输出计算步骤：
```
创建LP问题：
max z = 3·x1 +5·x2 
s.t.
	1·x1 <= 4
	1·x2 <= 6
	3·x1 +2·x2 <= 18
 
添加松弛变量：
max z = 3·x1 +5·x2 
s.t.
	1·x1 +1·s0 = 4
	1·x2 +1·s1 = 6
	3·x1 +2·x2 +1·s2 = 18
 
等号右边变为正数:
max z = 3·x1 +5·x2 
s.t.
	1·x1 +1·s0 = 4
	1·x2 +1·s1 = 6
	3·x1 +2·x2 +1·s2 = 18
 
添加人工变量：
max z = 3·x1 +5·x2 
s.t.
	1·x1 +1·s0 = 4
	1·x2 +1·s1 = 6
	3·x1 +2·x2 +1·s2 = 18
 
无人工变量, 开始求解第二阶段：
[[      1.0000       0.0000       1.0000       0.0000       0.0000
        4.0000]
 [      0.0000       1.0000       0.0000       1.0000       0.0000
        6.0000]
 [      3.0000       2.0000       0.0000       0.0000       1.0000
       18.0000]
 [      3.0000       5.0000       0.0000       0.0000       0.0000
        0.0000]]
基变量： [2, 3, 4]
选中： 1 行 1 列
[[      1.0000       0.0000       1.0000       0.0000       0.0000
        4.0000]
 [      0.0000       1.0000       0.0000       1.0000       0.0000
        6.0000]
 [      3.0000       0.0000       0.0000      -2.0000       1.0000
        6.0000]
 [      3.0000       0.0000       0.0000      -5.0000       0.0000
      -30.0000]]
基变量： [2, 1, 4]
选中： 2 行 0 列
[[      0.0000       0.0000       1.0000       0.6667      -0.3333
        2.0000]
 [      0.0000       1.0000       0.0000       1.0000       0.0000
        6.0000]
 [      1.0000       0.0000       0.0000      -0.6667       0.3333
        2.0000]
 [      0.0000       0.0000       0.0000      -3.0000      -1.0000
      -36.0000]]
基变量： [2, 1, 0]
最优解为： [      2.0000       6.0000       2.0000       0.0000       0.0000] 
最优值为： 36.0 
```

## 灵敏度分析
```
from inequality import *
from lp import LP

linear_programming = LP(...)
solution, best_value, end_simplex_tableau, basic_variable_idxs = linear_programming.xx_solve()

# 改A
linear_programming.modify_A(
    end_simplex_tableau, 
    basic_variable_idxs, 
    variable=x1, 
    new_p=[[0], [5]]
)

# 改b
linear_programming.modify_b(
    end_simplex_tableau,
    basic_variable_idxs,
    new_b=[
        [4],
        [6],
        [6]
    ]
)

# 改c
lp.modify_c(end_simplex_tableau, basic_variable_idxs, variable=x3, param=6)

# 添加约束
lp.modify_by_adding_constraints(
    end_simplex_tableau, 
    basic_variable_idxs, 
    Inequality(2 * x1 + 3 * x2 + 5 * x3, "<=", 50)
)
```
