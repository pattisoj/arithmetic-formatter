from optparse import OptParseError


def arithmetic_arranger(problems):
# First handle the possible errors
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        if "*" in problem or "/" in problem:
            return "Error: Operator must be '+' or '-'."
        
        operand_one = problem.split()[0]
        operand_two = problem.split()[2]

        if operand_one.isnumeric() == False or operand_two.isnumeric() == False:
            return "Error: Numbers must only contain digits."

        if len(operand_one) > 4 or len(operand_two) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        

    return "Error Checking"