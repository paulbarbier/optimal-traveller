import pyomo.environ as pyo
from pyomo.opt import SolverFactory


class Exact:
    def __init__(self, weight_matrix):
        self.weight_matrix = weight_matrix
        self.number_cities = len(weight_matrix)
        self.resulting_path = []

    def objective_expression(self, model):
        return pyo.summation(model.weight_matrix, model.paths)

    def constr_x_line(self, model, column):
        return sum([model.paths[row, column] for row in model.rows if row != column]) == 1

    def constr_x_column(self, model, row):
        return sum([model.paths[row, column] for column in model.columns if column != row]) == 1

    def constr_u(self, model, row, column):
        if row != column and row >= 2:
            return model.u[row] - model.u[column] + model.paths[row, column] * self.number_cities <= self.number_cities-1
        else:
            return pyo.Constraint.Feasible

    def solve(self):
        model = pyo.ConcreteModel()

        model.rows = pyo.RangeSet(self.number_cities)
        model.columns = pyo.RangeSet(self.number_cities)
        model.us = pyo.RangeSet(2, self.number_cities)

        model.weight_matrix = pyo.Param(model.rows, model.columns,
                                        initialize=lambda model, row, column: self.weight_matrix[row-1][column-1])

        model.paths = pyo.Var(model.rows, model.columns, domain=pyo.Binary)

        model.objective = pyo.Objective(rule=self.objective_expression, sense=pyo.minimize)

        model.u = pyo.Var(model.rows, domain=pyo.NonNegativeIntegers, bounds=(0, self.number_cities-1))

        model.XLineConstraint = pyo.Constraint(model.columns, rule=self.constr_x_line)
        model.XColumnConstraint = pyo.Constraint(model.rows, rule=self.constr_x_column)
        model.UConstraint = pyo.Constraint(model.us, model.columns, rule=self.constr_u)

        solver = SolverFactory("glpk")
        solver.solve(model)

        first_point, last_point = 1, 2
        self.resulting_path.append(first_point-1)
        while True:
            while model.paths[(first_point, last_point)]() != 1:
                last_point += 1

            self.resulting_path.append(last_point-1)

            first_point, last_point = last_point, 1

            if first_point == 1:
                break
