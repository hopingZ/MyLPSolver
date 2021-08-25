class NonMinusVariable:
    def __init__(self, name, is_integer=False):
        self.name = name
        self.is_integer = is_integer

    def __add__(self, other):
        if type(other) == NonMinusVariable:
            return [[1, self], [1, other]]
        if type(other) == list:
            return other + [[1, self]]

    def __radd__(self, other):
        if type(other) == NonMinusVariable:
            return [[1, self], [1, other]]
        if type(other) == list:
            return other + [[1, self]]

    def __sub__(self, other):
        if type(other) == NonMinusVariable:
            return [[1, self], [-1, other]]
        if type(other) == list:
            return other + [[-1, self]]

    def __rsub__(self, other):
        if type(other) == NonMinusVariable:
            return [[1, self], [-1, other]]
        if type(other) == list:
            return other + [[-1, self]]

    def __mul__(self, other):
        return [[other, self]]

    def __rmul__(self, other):
        return [[other, self]]

    def __neg__(self):
        return [[-1, self]]

    def __str__(self):
        return self.name


class Polynomial:
    def __init__(self, items):
        self.items = []
        if type(items) == NonMinusVariable:
            self.variable_num = 1
            self.items.append([1, items])
        if type(items) == list:
            self.variable_num = len(items)
            for item in items:
                self.items.append(item)

    def __str__(self):
        string = ""
        for i, item in enumerate(self.items):
            coefficient = item[0]
            variable = item[1].name
            if coefficient > 0 and i != 0:
                string += '+'
            string += str(coefficient)
            string += "·"
            string += variable
            string += ' '
        return string

    def __getitem__(self, item):
        return self.items[item]

    def add_items(self, items):
        if type(items) == NonMinusVariable:
            self.variable_num += 1
            self.items.append([1, items])
        if type(items) == list:
            for item in items:
                self.variable_num += 1
                self.items.append(item)

    def get_coefficient(self, variable):
        for item in self.items:
            if variable == item[1]:
                return item[0]
        return 0


class Inequality:
    def __init__(self, LHS, inequality_type, RHS):
        self.LHS = Polynomial(LHS)
        self.RHS = RHS
        if inequality_type == ">=":
            self.type = ">="
        elif inequality_type == "<=":
            self.type = "<="
        else:
            self.type = "="

    def __str__(self):
        return str(self.LHS) + self.type + " " + str(self.RHS)
