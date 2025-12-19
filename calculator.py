def add(num1, num2):
    return round(num1 + num2,2)


def multiply(num1, num2):
    return round(num1 * num2,2)


def division(num1, num2):
    return round(num1 / num2,2)


def sqrt(num1):
    return round(num1**0.5,2)


def power(num1, num2):
    return round(num1**num2,2)


def calculation(operand1,internal_operator,operand2):
    if internal_operator == "+":
        return add(float(operand1),float(operand2))
    elif internal_operator == "-":
        return mines(float(operand1),float(operand2))
    elif internal_operator == "*":
        return multiply(float(operand1),float(operand2))
    elif internal_operator == "/":
        return division(float(operand1),float(operand2))
    elif internal_operator == "**":
        return power(float(operand1),float(operand2))
    elif internal_operator == "√":
        return sqrt(float(operand1))



def calculate_exp(exp):
    operand_list = []
    operator__list = []
    current = ""

    for i, char in enumerate(exp):
        if char.isdigit() or char == ".":
            current += char

        elif char in "+-*/√":
            if char == "-" and (i == 0 or exp[i-1] in "+-*/√"):
                current += char
            elif char == "√" and (i == 0 or exp[i-1] in "+-*/√"):
                operator__list.append(char)
            else:
                if current != "":
                    operand_list.append(current)
                    current = ""
                operator__list.append(char)
        elif char == " ":
            continue
        else:
            continue

    if current != "":
        operand_list.append(current)

    return operand_list, operator__list


def token(exp):
    internal_phrase = operator = str()
    internal_list = list()
    operator_list = list()
    parenthesis = False
    for char in exp:
        if char == "(":
            parenthesis = True
            internal_phrase = str()
        elif char == ")":
            if parenthesis:
                internal_list.append(internal_phrase)
            parenthesis = False
        elif parenthesis:
            internal_phrase += char
        else:
            operator += char
            operator_list.append(operator)
            operator = str()
    return internal_list, operator_list



def inner_result(exp):
    paren_answers = list()
    math_symbols = list()
    expressions, operators = token(exp)
    for ans in expressions:
        values, symbol = calculate_exp(ans)
        answer_phrase = calculation(float(values[0]), symbol[0], float(values[1]))
        paren_answers.append(answer_phrase)

    for op in operators:
        math_symbols.append(op)

    for MultDiv in ["*", "/"]:
        if MultDiv in math_symbols:
            i = math_symbols.index(MultDiv)
            result = calculation(float(paren_answers[i]), math_symbols[i], float(paren_answers[i + 1]))
            paren_answers[i] = result
            paren_answers.pop(i + 1)
            math_symbols.pop(i)

    while len(math_symbols) > 0:
        for symbol in math_symbols:
            i = math_symbols.index(symbol)
            result = calculation(float(paren_answers[i]), math_symbols[i], float(paren_answers[i + 1]))
            paren_answers[i] = result
            paren_answers.pop(i + 1)
            math_symbols.pop(i)
    for res in paren_answers:
        return res


def without_parenthesis(exp):
    values, symbols = calculate_exp(exp)

    i = 0
    while i < len(symbols):
        op = symbols[i]
        if op in ("*", "/"):
            result = calculation(values[i], op, values[i + 1])
            values[i:i + 2] = [result]
            symbols.pop(i)
        else:
            i += 1

    i = 0
    while i < len(symbols):
        op = symbols[i]
        result = calculation(values[i], op, values[i + 1])
        values[i:i + 2] = [result]
        symbols.pop(i)

    return float(values[0])


def main():
     print("Hello. This is a simple calculator\n\nPlease select your calculation type:\n\t1.Simple(Without Parentheses)\n\t2.Complex(With parentheses)\n\t3.Exit")
     while True:
         type = input("Enter your type: ")
         if type == "1":
             while True:
                 expression = input("Write your simple mathematical expression: ").replace(" ", "")
                 if expression.lower() == "leave":
                     break
                 print(without_parenthesis(expression))
                 break

         elif type == "2":
             while True:
                 expression = input("Write your complex mathematical expression: ").replace(" ", "")
                 if expression.lower() == "leave":
                     break
                 print(inner_result(expression))
                 break

         else:
             print("Have a good time:)")
             break

main()