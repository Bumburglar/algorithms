class Fraction():
    def __init__(self, num, denum):
        self.num = num
        self.denum = denum

    def __str__(self):
        return str(self.num) + "/" + str(self.denum)

    def __add__(self, otherFraction):
        newNum = self.num + otherFraction.num
        newDenum = self.denum + otherFraction.denum
        return str(newNum) + "/" + str(newDenum)
