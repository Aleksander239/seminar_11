class Calculator:
    @staticmethod
    def calculate(expression):
        try:
            result = eval(expression)
            return result
        except Exception as e:
            raise ValueError(f"Ошибка вычисления: {e}")
