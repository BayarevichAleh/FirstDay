class Math:
    @classmethod
    def calculation(cls, arg1, arg2, operand):
        if operand == '+':
            return cls.add(arg1, arg2)
        elif operand == '-':
            return cls.sub(arg1, arg2)
        elif operand == '*':
            return cls.mul(arg1, arg2)
        elif operand == '/':
            return cls.div(arg1, arg2)

    @classmethod
    def add(arg1, arg2):
        return arg1 + arg2

    @classmethod
    def sub(arg1, arg2):
        return arg1 - arg2

    @classmethod
    def mul(arg1, arg2):
        return arg1 * arg2

    @classmethod
    def div(arg1, arg2):
        return arg1 / arg2


