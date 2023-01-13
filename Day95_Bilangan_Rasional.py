class Rasional:
    def __init__(self, p, q):
        self.p = p
        self.q = q
    
    def __str__(self):
        return str(self.p) + '/' + str(self.q)
    
    def __add__(self, other):
        p = self.p * other.q + other.p * self.q
        q = self.q * other.q
        return Rasional(p, q)
    
    def __sub__(self, other):
        p = self.p * other.q - other.p * self.q
        q = self.q * other.q
        return Rasional(p, q)
    
    def __mul__(self, other):
        p = self.p * other.p
        q = self.q * other.q
        return Rasional(p, q)
    
    def __truediv__(self, other):
        p = self.p * other.q
        q = self.q * other.p
        return Rasional(p, q)
    
    def simplify(self):
        gcd = self.__gcd(self.p, self.q)
        self.p = self.p // gcd
        self.q = self.q // gcd
    
    def __gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.__gcd(b, a % b)

r1 = Rasional(3, 4)
r2 = Rasional(2, 3)
print(r1 + r2) # 11/12
print(r1 - r2) # 1/12
print(r1 * r2) # 1/2
print(r1 / r2) # 9/8

r1.simplify()
print(r1) # 3/4
