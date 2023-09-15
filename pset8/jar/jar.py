class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size


    def __str__(self):
        return "🍪" * self.size


    def deposit(self, n):
        if n > (self.capacity - self.size):
            raise ValueError("Too many cookies")
        self.size += n


    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Cannot withdraw more than the deposited cookies")
        self.size -= n


    @property
    def capacity(self):
        return self._capacity


    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) < 0:
            raise ValueError("Not a non-negative integer")
        self._capacity = capacity



    @property
    def size(self):
        return self._size


    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError
        self._size = size


def main():
    cookies = Jar()
    cookies.deposit(10)
    cookies.withdraw(5)
    print(cookies)


if __name__ == "__main__":
    main()