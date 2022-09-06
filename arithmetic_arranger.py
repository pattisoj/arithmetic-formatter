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
        
# Deal with the upper operand
    upper_line = "  "
    additional_length = None
    for problem in problems:
      
      operand_one = problem.split()[0]
      operand_two = problem.split()[2]
      operand_one_length = len(operand_one)
      operand_two_length = len(operand_two)
      additional_length = operand_two_length - operand_one_length
          
      while additional_length > 0:
        upper_line = upper_line + " "
        additional_length = additional_length - 1

      upper_line = upper_line + operand_one + '      '

    upper_line = upper_line.rstrip() + "/n"
    print(upper_line)

    return "Top Line Complete"