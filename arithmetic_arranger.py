from optparse import OptParseError


def arithmetic_arranger(problems, answer=False):
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
        
# Deal with the upper operands
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

    upper_line = upper_line.rstrip() + "\n"
    # print(upper_line)

# Deal with the lower operands
    lower_line = ""
    additional_length = None
    for problem in problems:
      operand_one = problem.split()[0]
      math_symbol = problem.split()[1]
      operand_two = problem.split()[2]
      operand_one_length = len(operand_one)
      operand_two_length = len(operand_two)
      additional_length = operand_one_length - operand_two_length
      lower_line = lower_line + math_symbol
      
      while additional_length > 0:
        lower_line = lower_line + " "
        additional_length = additional_length - 1
      lower_line = lower_line + " " + operand_two + "    "

    lower_line = lower_line.rstrip() + "\n"  
    # print(lower_line)

# Deal with the dash separator
    dash_line = '--'
    for problem in problems:
      operand_one = problem.split()[0]
      operand_two = problem.split()[2]
      operand_one_length = len(operand_one)
      operand_two_length = len(operand_two)
      
      if operand_one_length >= operand_two_length:     
        while operand_one_length > 0:
          dash_line = dash_line + "-"
          operand_one_length = operand_one_length - 1
      elif operand_one_length < operand_two_length:
        while operand_two_length > 0:
          dash_line = dash_line + "-"
          operand_two_length = operand_two_length - 1
        
      dash_line = dash_line + '    --'
    
    dash_line = dash_line [:len(dash_line)-6]
    # print(dash_line)
    
    answer_not_required = upper_line + lower_line + dash_line
  
  # If answers are requested solve the problems
    answer_required = answer_not_required + "\n"
    for problem in problems:
      operand_one = int(problem.split()[0])
      math_symbol = problem.split()[1]
      operand_two = int(problem.split()[2])
      operand_one_length = len(problem.split()[0])
      operand_two_length = len(problem.split()[2])

      if operand_one_length >= operand_two_length: 
        longest_line = math_symbol + ' ' + str(operand_one)
        dash_length = len(longest_line)
      elif operand_one_length < operand_two_length:
        longest_line = math_symbol + ' ' + str(operand_two)
        dash_length = len(longest_line)
        
      if math_symbol == "+":
        solution = operand_one + operand_two
      elif math_symbol == "-":
        solution = operand_one - operand_two

      additional_spaces = dash_length - len(str(solution))
      spaces = ''
      while additional_spaces > 0:
        spaces = spaces + ' '
        additional_spaces = additional_spaces -1

      answer_required = answer_required + spaces + str(solution) + '    ' 
    answer_required = answer_required.rstrip()
      
    if answer == True:
      return answer_required
    elif answer == False:  
      return answer_not_required