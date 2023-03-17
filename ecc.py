class FieldElement:
    def __init__(self, num, prime):
        if num >= prime or num < 0: # because finite field element should be in range of 0 to prime - 1 or order - 1  
            error = 'Num {} not in Finite Field range 0 to {}'.format(num, prime - 1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return "FieldElement_{}({})".format(self.prime, self.num)
    
    def __eq__(self, other):  #checks if two elements are equal 
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other): #overriding != operator and 'other' is the right hand side operand
        return not (self == other)
    
    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError("Two numbers from different Finite Fields cannot be added.")
        num = ( self.num + other.num ) % self.prime
        return self.__class__(num, self.prime)
    
    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError("Two numbers from different Finite Fields cannot be added.")
        num = ( self.num - other.num ) % self.prime
        return self.__class__(num, self.prime) 
    
    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError("Two numbers from different Finite Fields cannot be added.")
        num = ( self.num * other.num ) % self.prime
        return self.__class__(num, self.prime)
    
    def __pow__(self, exponent): 
        # for making exponent positive 
        n  = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)
    
    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError("Two numbers from different Finite Fields cannot be added.")
        num = (self.num * (pow(other.num, self.prime-2, self.prime)) % self.prime )
        return self.__class__(num, self.prime)
    