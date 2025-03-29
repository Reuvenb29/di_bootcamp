# --- Exercise 1 ---

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        # String representation
        if self.amount > 1:
            return f"{self.amount} {self.currency}s"
        else:
            return f"{self.amount} {self.currency}"

    def __int__(self):
        # Allows conversion to int
        return self.amount

    def __repr__(self):
        # Developer-friendly representation, here we'll keep it similar to __str__
        return self.__str__()

    def __add__(self, other):
        # Adding int or another Currency
        if isinstance(other, int):
            return self.amount + other
        if isinstance(other, Currency):
            if self.currency == other.currency:
                return self.amount + other.amount
            else:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
        return NotImplemented

    def __iadd__(self, other):
     # In-place add
     if __name__ == "__main__":
        c1 = Currency('dollar', 5)
        c2 = Currency('dollar', 10)
        c3 = Currency('shekel', 1)
        c4 = Currency('shekel', 10)

    print(str(c1))       # '5 dollars'
    print(int(c1))       # 5
    print(repr(c1))      # '5 dollars'
    print(c1 + 5)        # 10
    print(c1 + c2)       # 15
    print(c1)            # '5 dollars'

    c1 += 5
    print(c1)            # '10 dollars'
    c1 += c2
    print(c1)            # '20 dollars'

    # This will raise TypeError
    # c1 + c3

