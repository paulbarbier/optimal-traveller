import pyomo.environ as pyo

class Solver:
    def __init__(self):
        pass

exact_method = pyo.AbstractModel()

exact_method.n = pyo.Param(within=pyo.NonNegativeIntegers)

exact_method.I = pyo.RangeSet(1, exact_method.n)
exact_method.J = pyo.RangeSet(1, exact_method.n)

exact_method.W = pyo.Param(exact_method.I, exact_method.J, domain=pyo.NonNegativeReals)

# variables
exact_method.X = pyo.Var(exact_method.I, exact_method.J, domain=pyo.Binary)
exact_method.u = pyo.Var(exact_method.I, domain=pyo.NonNegativeReals)


# objective function
def objective_expression(model):
    return pyo.summation(model.W, model.X)


exact_method.OBJ = pyo.Objective(rule=objective_expression)


# constraints
def constr_x_line(model, j):
    return sum(model.X[i, j] for i in model.I) == 1


def constr_x_column(model, i):
    return sum(model.X[i, j] for j in model.J) == 1


def constr_x_diag(model, i):
    return model.X[i, i] == 0


def constr_u_range(model, i):
    return 2 <= model.u[i] <= model.n


def constr_u(model, i, j):
    return (model.u[i]-model.u[j]) <= (model.n - model.X[i, j]*(model.n + 1))


exact_method.XLineConstraint = pyo.Constraint(exact_method.J, rule=constr_x_line)
exact_method.XColumnConstraint = pyo.Constraint(exact_method.I, rule=constr_x_column)
exact_method.XDiagConstraint = pyo.Constraint(exact_method.I, rule=constr_x_diag)
exact_method.URangeConstraint = pyo.Constraint(exact_method.I, rule=constr_u_range)
exact_method.UConstraint = pyo.Constraint(exact_method.I, exact_method.J, rule=constr_u)
