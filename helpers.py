import ast
import pandas as pd

df = pd.read_csv("Datasets/SVAMP_Sym.csv")

symbolic_problems = df["Symbolic Problem"]
variables = df["Variables"]
symbolic_equations = df["Symbolic Equation"]

def replace(replacements: list, index):
    problem = symbolic_problems[index]
    equation = symbolic_equations[index]
    vars = variables[index]
    vars = ast.literal_eval(vars)

    for i in range(len(vars)):
        var_index = problem.find(vars[i])
        while var_index != -1:
            if var_index != -1:
                for j in range(len(vars[i])):
                    problem = problem[:var_index] + problem[var_index+1:]
                problem = problem[:var_index] + replacements[i] + problem[var_index:]
            var_index = problem.find(vars[i])
        
        equation_index = equation.find(vars[i])
        if equation_index != -1:
            while equation_index != -1:
                for k in range(len(vars[i])):
                    equation = equation[:equation_index] + equation[equation_index+1:]
                equation = equation[:equation_index] + replacements[i] + equation[equation_index:]
                equation_index = equation.find(vars[i])
                if equation_index != -1:
                    equation_index += 1
    
    equation = equation.replace("<", "")

    return problem, equation

def get_len_problems() -> int:
    return len(variables)

def column_save(df, column_name, val, index):
    df[column_name][index] = val
    return