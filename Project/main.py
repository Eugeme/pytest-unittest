class Monomial:
    def __init__(self, value: str):
        self.value = value
        if not isinstance(self.value, str):
            raise TypeError

    def differentiate(self):
        mon = self.value
        if mon == 'x':
            return '1'
        elif mon == '-x':
            return '-1'
        if mon[0] == '-' and mon[1:].isdigit() == True or mon.isdigit() == True:
            return str(0)
        elif mon[-1] == 'x':
            return mon[:-1]
        else:
            degree = ''
            end = 0
            b = mon[::-1]
            for i in range(len(b)):
                if b[i] == '^':
                    end += i
                    break
                degree += b[i]
            degree = degree[::-1]
            coef = ''
            for i in range(len(mon)):
                if mon[i] == 'x':
                    end += i
                    break
                coef += mon[i]
            if coef == '-':
                res = str(-int(degree)) + mon[1:-len(degree)] + str(int(degree) - 1)
                if res[:-3:-1] == '1^':
                    return res[:-2]
                return res
            elif coef == '':
                res = str(int(degree)) + mon[:-len(degree)] + str(int(degree) - 1)
                if res[:-3:-1] == '1^':
                    return res[:-2]
                return res
            res = str(int(coef) * int(degree)) + mon[len(coef):-len(degree)] + str(int(degree) - 1)
            if res[:-3:-1] == '1^':
                return res[:-2]
            return res
