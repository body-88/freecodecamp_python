def arithmetic_arranger(problems, result=False):
    first = ''
    second = ''
    dashes = ''
    result_string = ''
    string = ''
    
    dash= "-"
    space = " "
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        first_number = problem.split(" ")[0]
        operator_sign = problem.split(" ")[1]
        second_number = problem.split(" ")[2]
        
        if  operator_sign not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if first_number.isdigit() == False or second_number.isdigit() == False:
            return "Error: Numbers must only contain digits."
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        answer = ""
        if operator_sign == "+":
            answer = str(int(first_number) + int(second_number))
        elif operator_sign == '-':
            answer = str(int(first_number) - int(second_number))
        
        longest_problem = max(len(first_number), len(second_number)) +2
        first_line=str(first_number).rjust(longest_problem)
        second_line=operator_sign + str(second_number).rjust(longest_problem-1)
        third_line = ""
        fourth_line = str(answer).rjust(longest_problem)
        for var in range(longest_problem):
            third_line += dash
        
        if problem != problems[-1]:    
            first += first_line + space*4
            second += second_line + space*4
            dashes += third_line + space*4
            result_string += fourth_line + space*4
        else:
            first += first_line
            second += second_line
            dashes += third_line
            result_string += fourth_line
    if result:
        string = first +"\n" + second + "\n" + dashes + "\n" + result_string
    else:            
        string = first + "\n" + second + "\n" + dashes
    return string
