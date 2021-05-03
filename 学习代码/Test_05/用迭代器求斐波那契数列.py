class F:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.num1 = 1
        self.num2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        x = self.num1
        self.num1, self.num2 = self.num2, self.num1 + self.num2
        if self.count <= self.n:
            return x
        raise StopIteration


f = F(11)
for i in f:
    print(i)
