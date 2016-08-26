class Fraction():
    def __init__(self, num, denum):
        self.num = num
        self.denum = denum

    def __str__(self):
        return str(self.num) + "/" + str(self.denum)

    def __add__(self, otherFraction):
        newNum = self.num * otherFraction.denum + otherFraction.num * self.denum
        newDenum = self.denum * otherFraction.denum
        common = self.gcd(newNum, newDenum)
        return str(newNum//common) + "/" + str(newDenum//common)

    def __eq__(self, other):
        firstnum = self.num * other.denum
        secondnum = other.num * self.denum
        return firstnum == secondnum

    def gcd(self, m, n):
        while m % n != 0:
            oldm = m
            oldn = n
            m = oldn
            n = oldm % oldn
        return n
