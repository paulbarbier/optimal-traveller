import pyomo.environ as pyo
from pyomo.opt import SolverFactory

class Exact:
    def __init__(self):
        pass

    def exact_method(self, weight, nb_cities):
        model = pyo.ConcreteModel()

        model.row = pyo.RangeSet(nb_cities)
        model.column = pyo.RangeSet(nb_cities)
        model.us = pyo.RangeSet(2, nb_cities)

        model.W = pyo.Param(model.row, model.column, initialize=lambda model,i,j: weight[i-1][j-1])

        model.X = pyo.Var(model.row, model.column, domain=pyo.Binary)
        model.u = pyo.Var(model.row, domain=pyo.NonNegativeIntegers, bounds=(0, nb_cities-1))

        def objective_expression(model):
            return sum(model.W[i,j]*model.X[i,j] for i in model.row for j in model.column)

        model.objective = pyo.Objective(rule=objective_expression, sense=pyo.minimize)

        def constr_x_line(model, column):
            return sum([model.X[i, column] for i in model.row if i!=column]) == 1

        def constr_x_column(model, row):
            return sum([model.X[row, j] for j in model.column if j!=row]) == 1

        def constr_u(model, row, column):
            if row != column:
                return model.u[row]-model.u[column] + model.X[row, column]*nb_cities <= nb_cities-1
            else:
                return model.u[row]-model.u[row] == 0

        model.XLineConstraint = pyo.Constraint(model.column, rule=constr_x_line)
        model.XColumnConstraint = pyo.Constraint(model.row, rule=constr_x_column)
        model.UConstraint = pyo.Constraint(model.us, model.column, rule=constr_u)

        solver = SolverFactory('glpk')
        exact_result = solver.solve(model)

        L = list(model.X.keys())
        solution = []
        for indice in L:
            if model.X[indice]() != 0:
                solution.append(indice[0])
        solution.append(solution[0])
        return solution
