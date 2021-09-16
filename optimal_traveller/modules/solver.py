import pyomo.environ as pyo


class Solver:
    def __init__(self):
        pass

    def get_data_for_pyomo(self, data):
        pyomo_data = open('pyomo_data.txt', 'w+')

        n = len(data['cities'])
        pyomo_data.write("param n := ", n, " ;\n\n")

        pyomo_data.write("param W :=\n")
        for i in range(n):
            for j in range(n):
                pyomo_data.write(" ", data['weight_matrix'][i][j])
            pyomo_data.write("\n")
        pyomo_data.write(" ;\n")

        pyomo_data.close()

    def exact_method(self, pyomo_format_data):
        model = pyo.AbstractModel()

        model.n = pyo.Param(within=pyo.NonNegativeIntegers)

        model.I = pyo.RangeSet(1, model.n)
        model.J = pyo.RangeSet(1, model.n)

        model.W = pyo.Param(model.I, model.J, domain=pyo.NonNegativeReals)

        # variables
        model.X = pyo.Var(model.I, model.J, domain=pyo.Binary)
        model.u = pyo.Var(model.I, domain=pyo.NonNegativeReals)

        # objective function
        def objective_expression(m):
            return pyo.summation(m.W, m.X)

        model.OBJ = pyo.Objective(rule=objective_expression)

        # constraints
        def constr_x_line(m, j):
            return sum(m.X[i, j] for i in m.I) == 1

        def constr_x_column(m, i):
            return sum(m.X[i, j] for j in m.J) == 1

        def constr_x_diag(m, i):
            return m.X[i, i] == 0

        def constr_u_range(m, i):
            return 2 <= m.u[i] <= m.n

        def constr_u(m, i, j):
            return (m.u[i]-m.u[j]) <= (m.n - m.X[i, j]*(m.n + 1))

        model.XLineConstraint = pyo.Constraint(model.J, rule=constr_x_line)
        model.XColumnConstraint = pyo.Constraint(model.I, rule=constr_x_column)
        model.XDiagConstraint = pyo.Constraint(model.I, rule=constr_x_diag)
        model.URangeConstraint = pyo.Constraint(model.I, rule=constr_u_range)
        model.UConstraint = pyo.Constraint(model.I, model.J, rule=constr_u)
