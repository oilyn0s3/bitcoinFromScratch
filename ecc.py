class FieldElement:
    def __init__(self, num, prime):
        if num >= prime or num < 0:  # because finite field element should be in range of 0 to prime - 1 or order - 1
            error = 'Num {} not in Finite Field range 0 to {}'.format(
                num, prime - 1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return "FieldElement_{}({})".format(self.prime, self.num)

    def __eq__(self, other):  # checks if two elements are equal
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):  # overriding != operator and 'other' is the right hand side operand
        return not (self == other)

    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError(
                "Two numbers from different Finite Fields cannot be added.")
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError(
                "Two numbers from different Finite Fields cannot be added.")
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError(
                "Two numbers from different Finite Fields cannot be added.")
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        # for making exponent positive
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError(
                "Two numbers from different Finite Fields cannot be added.")
        num = (self.num * (pow(other.num, self.prime-2, self.prime)) % self.prime)
        return self.__class__(num, self.prime)


class Point:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        if self.x is None and self.y is None:
            return
        if self.y**2 != self.x**3 + self.a * self.x + self.b:
            raise ValueError('({}, {}) is not on the curve.'.format(x, y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise ValueError(
                'Points {}, {} are not on the same curve.'.format(self, other))

        if self.x is None: # when x1 is infinity, return the other i.e. x2
            return other

        if other.x is None: # when x2 is infinity, return the self i.e. x1
            return self
        
        if self.x == other.x and self.y != other.y: # wehn x1 = x2
            return self.__class__(None, None, self.a, self.b)
        
        if self.x != other.x and self.y == other.y: # when x1 != x2
            s = (other.y - self.y) / (other.x - self.x)
            x = s**2 - self.x - other.x
            y = s * ( self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)