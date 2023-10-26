class CalculatorException(Exception):
    def __init__(self, message="Expresia introdusa nu poate fi evaluata."):
        super().__init__(self, message)


class Calculator(object):
    def read(self) :
        '''read input from stdin'''
        return input('> ')


    def __isValidInput(self, string):
        isValid = True
        validOperators = ["+", "-", "*", "/", "(", ")"]
        paranthesisCount = {"(": 0, ")": 0}
        numbersOperatorsCount = {"numbers": 0, "operators": 0}

        for index, char in enumerate(string.strip()):
            if not char.isdigit() and not char.isspace() and char not in validOperators:
                isValid = False
            if char == "(":
                paranthesisCount["("] = paranthesisCount["("] + 1
            elif char == ")":
                paranthesisCount[")"] = paranthesisCount[")"] + 1
            if char.isdigit():
                if index != 0:
                    if string[index-1].isdigit():
                        pass
                    else:
                        numbersOperatorsCount["numbers"] = numbersOperatorsCount["numbers"] + 1
                else:
                    numbersOperatorsCount["numbers"] = numbersOperatorsCount["numbers"] + 1
            if char in ["+", "-", "*", "/"]:
                numbersOperatorsCount["operators"] = numbersOperatorsCount["operators"] + 1

        if paranthesisCount["("] != paranthesisCount[")"]:
            isValid = False

        if numbersOperatorsCount["numbers"] != numbersOperatorsCount["operators"] + 1:
            isValid = False

        if not isValid:
            raise CalculatorException()


    def __performOperation(self, number1, number2, operator):
        if operator == "+":
            return number1 + number2
        if operator == "-":
            return number1 - number2
        if operator == "*":
            return number1 * number2
        if operator == "/":
            return number1 // number2


    def eval(self, string) :
        '''evaluates an infix arithmetic expression '''

        string = string.strip()
        operatorPrecedence = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0, ")": 0}
        numbers = []
        operators = []

        for index, char in enumerate(string):
            if char.isdigit():
                if index != 0:
                    if string[index-1].isdigit():
                        numbers[-1] = numbers[-1] * 10 + int(char)
                    else:
                        numbers.append(int(char))
                else:
                    numbers.append(int(char))
            elif char.isspace():
                continue
            elif char == "(":
                operators.append(char)
            elif char == ")":
                while len(operators) != 0 and operators[-1] != "(":
                    number2 = numbers.pop()
                    number1 = numbers.pop()
                    operator = operators.pop()
                    result = self.__performOperation(number1, number2, operator)
                    numbers.append(result)
                operators.pop()
            else:
                while len(operators) != 0 and operatorPrecedence[operators[-1]] >= operatorPrecedence[char]:
                    number2 = numbers.pop()
                    number1 = numbers.pop()
                    operator = operators.pop()
                    result = self.__performOperation(number1, number2, operator)
                    numbers.append(result)
                operators.append(char)

        while len(operators) != 0:
            number2 = numbers.pop()
            number1 = numbers.pop()
            operator = operators.pop()
            result = self.__performOperation(number1, number2, operator)
            numbers.append(result)

        return(numbers[-1])

    def loop(self) :
        """read a line of input, evaluate and print it
        repeat the above until the user types 'quit'. """

        while True:
            line = self.read()

            if line.strip().lower() == "quit":
                break
            else:
                try:
                    self.__isValidInput(line)
                    result = self.eval(line)
                    print(result)
                except CalculatorException as calcException:
                    print(calcException)
                    print("Va rugam sa introduceti alta expresie")



if __name__ == '__main__':
    calc = Calculator()
    calc.loop()
