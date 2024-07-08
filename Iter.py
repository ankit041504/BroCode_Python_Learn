class Evenit:
 
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            if self.n % 2 ==0:
                result=self.n
                self.n += 1
                return result
            else:
                self.n += 1
                return 1
        else:
            raise StopIteration


# create an object
numbers = Evenit(10)

for i in numbers:
	print(i)