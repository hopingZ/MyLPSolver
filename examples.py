from inequality import *
from lp import LP

if __name__ == "__main__":
    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(3*x1 - x2 + 2*x3, "<=", 7)
    inequality2 = Inequality(-2*x1 + 4*x2, "<=", 12)
    inequality3 = Inequality(-4*x1 + 3*x2 + 8*x3, "<=", 10)
    obj_fn = Polynomial(-x1 + 3*x2 + x3)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="max",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(2 * x1 + x2 - x3, "<=", 5)
    inequality2 = Inequality(4 * x1 + 3 * x2 + x3, ">=", 3)
    inequality3 = Inequality(-x1 + x2 + x3, "=", 2)
    obj_fn = Polynomial(-3*x1 + 2*x2 - x3)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="max",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(2 * x1 - x2 - x3, ">=", 3)
    inequality2 = Inequality(x1 - x2 + x3, ">=", 2)
    obj_fn = Polynomial(2 * x1 + -3 * x2)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="max",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    x4 = NonMinusVariable("x4")
    variables = [x1, x2, x3, x4]
    inequality1 = Inequality(2 * x1 + -3 * x2 + x3, "=", 1)
    inequality2 = Inequality(2 * x1 + 3 * x2 - x4, "=", 8)
    obj_fn = Polynomial(3 * x1 + -2 * x2 + x3)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(x1 + -2 * x2 + x3, "<=", 11)
    inequality2 = Inequality(2 * x1 + x2 + -4 * x3, ">=", 3)
    inequality3 = Inequality(x1 + -2 * x3, "=", 1)
    obj_fn = Polynomial(x1 + x2 + -3 * x3)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(x1 + 2*x2 + x3, "=", 16)
    inequality2 = Inequality(2*x1 + x2, "=", 12)
    obj_fn = Polynomial(2*x1 + 5*x2)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="max",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(x1 + 3*x3, ">=", 3)
    inequality2 = Inequality(x2 + 2*x3, ">=", 5)
    obj_fn = Polynomial(4*x1 + 6*x2 + 18*x3)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    variables = [x1, x2]
    inequality1 = Inequality(x1 + x2, "<=", 5)
    inequality2 = Inequality(x1 - x2, ">=", 0)
    inequality3 = Inequality(6*x1 + 2*x2, "<=", 21)
    obj_fn = Polynomial(2*x1 + x2)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="max",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(-x1 + 2*x2 + 4*x3, "<=", 4)
    inequality2 = Inequality(x1 + x2 + 2*x3, "<=", 5)
    inequality3 = Inequality(-x1 + 2*x2 + x3, ">=", 1)
    obj_fn = Polynomial(3*x1 + (-5)*x2)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="max",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(x1 + x2 + x3, "<=", 9)
    inequality2 = Inequality(-x1 + 2*x2 - x3, ">=", 5)
    inequality3 = Inequality(2*x1 - x2, "<=", 7)
    obj_fn = Polynomial(2*x1 + (-3)*x2 + 4*x3)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    x4 = NonMinusVariable("x4")
    variables = [x1, x2, x3, x4]
    inequality1 = Inequality(x1 + 2*x2 + (-1)*x3 + x4, "=", 0)
    inequality2 = Inequality(x1 + (-1)*x2 + 2*x3 + (-1)*x4, "=", 6)
    inequality3 = Inequality(2*x1 + (-2)*x1 + 3*x3 + 3*x4, "=", 9)
    obj_fn = Polynomial(3*x1 - x2 + (-3)*x3 + x4)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="max",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    x4 = NonMinusVariable("x4")
    x5 = NonMinusVariable("x5")
    variables = [x1, x2, x3, x4, x5]
    inequality1 = Inequality(x1 + -2 * x2 + x3 + x4, "=", 11)
    inequality2 = Inequality(-4 * x1 + x2 + 2 * x3 + (-1) * x5, "=", 3)
    inequality3 = Inequality(-2 * x1 + x3, "=", 1)
    obj_fn = Polynomial(-3 * x1 + x2 + x3)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    variables = [x1, x2]
    inequality1 = Inequality(2*x1 + x2, "<=", 4)
    inequality2 = Inequality(x1 + 2*x2, ">=", 9)
    obj_fn = Polynomial(3 * x1 + 2 * x2)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="max",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    variables = [x1, x2]
    inequality1 = Inequality(x1 + x2, ">=", 1)
    inequality2 = Inequality(2*x1 - x2, ">=", 1)
    inequality3 = Inequality(3*x2, "<=", 2)
    obj_fn = Polynomial(6*x1 + 3*x2)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(2*x1 - x2 + x3, "=", 8)
    inequality2 = Inequality(2*x1 + x2, ">=", 2)
    inequality3 = Inequality(x1 + 2*x2, "<=", 10)
    obj_fn = Polynomial(x1 + (-3)*x2 + x3)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(-x1 + x2 + 3 * x3, "<=", 20)
    inequality2 = Inequality(12 * x1 + 4 * x2 + 10 * x3, "<=", 90)
    obj_fn = Polynomial(-5 * x1 + 5 * x2 + 13 * x3)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="max",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(x1 + 3*x3, ">=", 3)
    inequality2 = Inequality(x2 + 2*x3, ">=", 5)
    obj_fn = Polynomial(4*x1 + 6*x2 + 18*x3)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    x4 = NonMinusVariable("x4")
    variables = [x1, x2, x3, x4]
    inequality1 = Inequality(-2*x1 + 5*x2 + 3*x3 + (-5)*x4, "<=", 3)
    inequality2 = Inequality(x1 + 2*x2 + 5*x3 + 6*x4, ">=", 8)
    obj_fn = Polynomial(-3*x1 + (-2)*x2 + (-4)*x3 + (-8)*x4)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="max",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(x1 - x2 - x3, "=", 1)
    inequality2 = Inequality(x3, ">=", 2)
    obj_fn = Polynomial(x1 + x2)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="max",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    x4 = NonMinusVariable("x4")
    variables = [x1, x2, x3, x4]
    inequality1 = Inequality(x1 + x2 + (-2)*x3 + 3*x4, ">=", 5)
    inequality2 = Inequality(2*x1 - x2 + x3 - x4, ">=", 4)
    obj_fn = Polynomial(x1 + (-2)*x2 + (-3)*x3)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    x4 = NonMinusVariable("x4")
    variables = [x1, x2, x3, x4]
    inequality1 = Inequality(2*x1 + x2 + 4*x3, ">=", 2)
    inequality2 = Inequality(2*x1 + 2*x2 + 4*x4, ">=", 3)
    obj_fn = Polynomial(12*x1 + 8*x2 + 16*x3 + 12*x4)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(x1 + x2 + x3, ">=", 4)
    inequality2 = Inequality(x1 + 2*x2 + 2*x3, "<=", 6)
    obj_fn = Polynomial(-2*x1 + x2)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    x4 = NonMinusVariable("x4")
    x5 = NonMinusVariable("x5")
    x6 = NonMinusVariable("x6")
    x7 = NonMinusVariable("x7")
    x8 = NonMinusVariable("x8")
    variables = [x1, x2, x3, x4, x5, x6, x7, x8]
    inequality1 = Inequality(-2*x1 + x2 + x3 + x4 - x5 + x6, "=", -3)
    inequality2 = Inequality(x1 + x2 + (-3)*x3 + 2*x4 + (-2)*x5 + x8, "=", 4)
    inequality3 = Inequality(-x1 - x2 + x3 + x4 - x5 + x7, "=", -2)
    obj_fn = Polynomial(4*x1 + 3*x2 + 5*x3 + x4 + 2*x5)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    x4 = NonMinusVariable("x4")
    variables = [x1, x2, x3, x4]
    inequality1 = Inequality(x1 + x2 + x3, "=", 9)
    inequality2 = Inequality(-3*x1 + (-2)*x2 + x4, "=", -23)
    obj_fn = Polynomial(-4*x1 + 3*x2)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="max",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(x1 + x2 + 2 * x3, "<=", 6)
    inequality2 = Inequality(x1 + 4 * x2 - x3, "<=", 4)
    obj_fn = Polynomial(-2 * x1 - x2 + x3)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(x1 + x2 + 2 * x3, "<=", 9)
    inequality2 = Inequality(x1 + x2 - x3, "<=", 2)
    inequality3 = Inequality(-x1 + x2 + x3, "<=", 4)
    obj_fn = Polynomial(x1 + x2 + (-4) * x3)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(x1 + x2 + x3, "<=", 6)
    inequality2 = Inequality(2*x1 - x2, "<=", 4)
    obj_fn = Polynomial(-x1 + 2*x2 + x3)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="max",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(-x1 + x2 + 3 * x3, "<=", 20)
    inequality2 = Inequality(12 * x1 + 4 * x2 + 10 * x3, "<=", 90)
    obj_fn = Polynomial(-5 * x1 + 5 * x2 + 13 * x3)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="max",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(x1 + x2 + x3, "<=", 4)
    inequality2 = Inequality(x1, "<=", 2)
    inequality3 = Inequality(x3, "<=", 3)
    inequality4 = Inequality(3 * x2 + x3, "<=", 6)
    obj_fn = Polynomial(x1 + 5 * x2 + (-2) * x3)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3, inequality4],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(x1 - x2 + 6*x3, ">=", 2)
    inequality2 = Inequality(x1 + x2 + 2*x3, ">=", 1)
    obj_fn = Polynomial(5 * x1 + 21 * x3)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    x4 = NonMinusVariable("x4")
    variables = [x1, x2, x3, x4]
    inequality1 = Inequality(2*x1 - x2 + x3, "=", 4)
    inequality2 = Inequality(x1 + x2 + x3, "=", 6)
    inequality3 = Inequality(x1 + x4, "=", 2)
    inequality4 = Inequality(3*x1 + 2*x3, "=", 10)
    obj_fn = Polynomial(3 * x1 + x2 + (-2) * x3)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3, inequality4],
            mode="max",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    x4 = NonMinusVariable("x4")
    variables = [x1, x2, x3, x4]
    inequality1 = Inequality(x1 + 2*x2 + 3*x3, "=", 15)
    inequality2 = Inequality(2*x1 + x2 + 5*x3, "=", 20)
    inequality3 = Inequality(x1 + 2*x2 + 4*x3 + x4, "=", 26)
    obj_fn = Polynomial(5 * x1 + 2*x2 + 3 * x3 - x4)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="max",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    variables = [x1, x2]
    inequality1 = Inequality(x1 - x2, ">=", 1)
    inequality2 = Inequality(-x1 + 2*x2, ">=", 2)
    obj_fn = Polynomial(x1 + 2*x2)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    x4 = NonMinusVariable("x4")
    x5 = NonMinusVariable("x5")
    variables = [x1, x2, x3, x4, x5]
    inequality1 = Inequality(-3*x1 + x2 + x3 - x4 + 2*x5, "<=", 5)
    inequality2 = Inequality(2*x1 - x3 + x4 - x5, "<=", 6)
    inequality3 = Inequality(x2 + 2*x3 - x4 + x5, "<=", 3)
    obj_fn = Polynomial(2*x1 + x2 - x3 + (-3)*x4 + x5)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(x1 + x2 + x3, "<=", 8)
    inequality2 = Inequality(-x1 + x2 - x3, "<=", 2)
    inequality3 = Inequality(-x2 + 2*x3, "<=", 4)
    obj_fn = Polynomial(x1 - x2 + (-2)*x3)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    variables = [x1, x2]
    inequality1 = Inequality(3*x1 + x2, "<=", 2)
    inequality2 = Inequality(-x1 + 2*x2, "<=", 3)
    inequality3 = Inequality(x1 + (-3)*x2, "<=", 1)
    obj_fn = Polynomial(x1 + 2*x2)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="max",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    x4 = NonMinusVariable("x4")
    variables = [x1, x2, x3, x4]
    inequality1 = Inequality(2*x1 + x2 + 4*x3, ">=", 2)
    inequality2 = Inequality(2*x1 + 2*x2 + 4*x4, ">=", 3)
    obj_fn = Polynomial(12 * x1 + 8 * x2 + 16 * x3 + 12 * x4)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(x1 + x2 + x3, ">=", 4)
    inequality2 = Inequality(x1 + 2*x2 + 2*x3, "<=", 6)
    obj_fn = Polynomial(-2*x1 + x2)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    x4 = NonMinusVariable("x4")
    variables = [x1, x2, x3, x4]
    inequality1 = Inequality(x1 + x2 + (-2)*x3 + 3*x4, ">=", 5)
    inequality2 = Inequality(2*x1 - x2 + x3 - x4, ">=", 4)
    obj_fn = Polynomial(x1 + (-2)*x2 + (-3)*x3)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    x4 = NonMinusVariable("x4")
    x5 = NonMinusVariable("x5")
    x6 = NonMinusVariable("x6")
    x7 = NonMinusVariable("x7")
    variables = [x1, x2, x3, x4, x5, x6, x7]
    inequality1 = Inequality(-5 * x1 + 2 * x2 + 6 * x3 - x4 + x5 - x6, "=", 6)
    inequality2 = Inequality(2 * x1 + x2 + x3 + x4 + 2 * x5 - x7, "=", 3)
    obj_fn = Polynomial(-x1 + -3 * x2 + -7 * x3 + -4 * x4 + -6 * x5)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="max",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(x1 + x2 + 2 * x3, "=", 3)
    inequality2 = Inequality(2 * x1 + x2 + 3 * x3, "=", 5)
    obj_fn = Polynomial(2 * x1 + x2 + 4 * x3)
    linear_programming = LP(inequalities=[inequality1, inequality2],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    x4 = NonMinusVariable("x4")
    x5 = NonMinusVariable("x5")
    x6 = NonMinusVariable("x6")
    variables = [x1, x2, x3, x4, x5, x6]
    inequality1 = Inequality(x1 + x2 + x3, "=", 15)
    inequality2 = Inequality(x4 + x5 + x6, "=", 8)
    inequality3 = Inequality(x1 + x3 + x5, "=", 12)
    obj_fn = Polynomial(5*x1 + 2 * x2 + 3 * x3 + 7 * x4 + 9 * x5 + x6)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    x4 = NonMinusVariable("x4")
    x5 = NonMinusVariable("x5")
    x6 = NonMinusVariable("x6")
    variables = [x1, x2, x3, x4, x5, x6]
    inequality1 = Inequality(x1 + 3 * x2 + x3 + x4, "=", 15)
    inequality2 = Inequality(2 * x1 + 3 * x2 - x3 + x5, "=", 18)
    inequality3 = Inequality(x1 - x2 + x3 + x6, "=", 3)
    obj_fn = Polynomial(-2 * x1 + -3 * x2 - x3)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(x1 + x2 + x3, "<=", 9)
    inequality2 = Inequality(-x1 + 2*x2 - x3, ">=", 5)
    inequality3 = Inequality(2 * x1 - x2, "<=", 7)
    obj_fn = Polynomial(2 * x1 + -3* x2 + 4 * x3)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    x4 = NonMinusVariable("x4")
    x5 = NonMinusVariable("x5")
    x6 = NonMinusVariable("x6")
    x7 = NonMinusVariable("x7")
    x8 = NonMinusVariable("x8")
    variables = [x1, x2, x3, x4, x5, x6, x7, x8]
    inequality1 = Inequality(-2 * x1 + x2 + x3 + x4 - x5 + x6, "=", -3)
    inequality2 = Inequality(x1 + x2 + (-3) * x3 + 2 * x4 + (-2) * x5 + x8, "=", 4)
    inequality3 = Inequality(-x1 - x2 + x3 + x4 - x5 + x7, "=", -2)
    obj_fn = Polynomial(4 * x1 + 3 * x2 + 5 * x3 + x4 + 2 * x5)
    linear_programming = LP(inequalities=[inequality1, inequality2, inequality3],
            mode="min",
            obj_fn=obj_fn,
            variables=variables)'''

    '''x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    linear_programming = LP(
        inequalities=[
            Inequality(x1, "<=", 4),
            Inequality(x2, "<=", 6),
            Inequality(3 * x1 + 2 * x2, "<=", 18)
        ],
        mode="max",
        obj_fn=Polynomial(3 * x1 + 5 * x2),
        variables=[x1, x2]
    )'''

    x1 = NonMinusVariable("x1")
    x2 = NonMinusVariable("x2")
    x3 = NonMinusVariable("x3")
    variables = [x1, x2, x3]
    inequality1 = Inequality(x1 + 3*x3, ">=", 3)
    inequality2 = Inequality(x2 + 2*x3, ">=", 5)
    obj_fn = Polynomial(4 * x1 + 6 * x2 + 18 * x3)
    linear_programming = LP(inequalities=[inequality1, inequality2],
                            mode="min",
                            obj_fn=obj_fn,
                            variables=variables)

    # solution, best_value, end_simplex_tableau, basic_variable_idxs = linear_programming.dual_solve()
    # solution, best_value, end_simplex_tableau, basic_variable_idxs = linear_programming.two_phase_solve()
    solution, best_value, end_simplex_tableau, basic_variable_idxs = linear_programming.big_m_solve()

    # linear_programming.modify_c(end_simplex_tableau, basic_variable_idxs, x3, 6)
    '''linear_programming.modify_b(
        end_simplex_tableau,
        basic_variable_idxs,
        new_b=[
            [4],
            [6],
            [6]
        ]
    )'''
    # linear_programming.modify_A(end_simplex_tableau, basic_variable_idxs, x1, [[0], [5]])
    # new_inequality = Inequality(2 * x1 + 3 * x2 + 5 * x3, "<=", 50)
    # linear_programming.modify_by_adding_constraints(end_simplex_tableau, basic_variable_idxs, new_inequality)
