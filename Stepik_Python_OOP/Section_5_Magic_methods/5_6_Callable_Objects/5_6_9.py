
class Calculator:

    def __call__(self, a, b, operation):
        if isinstance(a and b, int|float):
            if operation == '+':
                return a + b
            elif operation == '-':
                return a - b
            elif operation == '*':
                return a * b
            elif operation == '/':
                if b == 0:
                    raise ValueError('Деление на ноль невозможно')
                return a / b





calculator = Calculator()

print(calculator(10, 0, '+'))
print(calculator(10, 0, '-'))
print(calculator(10, 0, '*'))


class Calculator:
    def __call__(self, a, b, operation):
        if operation == '/' and b == 0:
            raise ValueError('Деление на ноль невозможно')
        return eval(f'{a}{operation}{b}')



class Calculator:
    def __call__(self, a, b, operation):
        match operation:
            case '+':
                return a + b
            case '-':
                return a - b
            case '*':
                return a * b
            case '/':
                if b == 0:
                    raise ValueError('Деление на ноль невозможно')
                return a / b