

class Permutation:
    def __init__(self, n):
        self.n = n - 1
        self.x = range(1, n + 1)
        pass

    def isLastConfiguration(self):
        for i in self.x:
            if self.x[i] < self.x[i+1]:
                return 0
        return 1

    def printConfiguration(self, count):
        print "{} {}".format(count, self.x)

    def nextConfiguration(self):
        i = self.n - 1
        while i > 0 and self.x[i] > self.x[i+1]:
            i = i - 1
        k = self.n
        while self.x[i] > self.x[k]:
            k = k -1

        # Swap 2 elements
        t = self.x[i]
        self.x[i] = self.x[k]
        self.x[k] = t
        left = i + 1
        right = self.n

        while left < right:
            t = self.x[left]
            self.x[left] = self.x[right]
            self.x[right] = t
            left = left + 1
            right = right -1


    def generate(self):
        count = 1
        self.printConfiguration(count)
        stop = self.isLastConfiguration()
        while not stop:
            self.nextConfiguration()
            count = count + 1
            self.printConfiguration(count)
            stop = self.isLastConfiguration()

permutation = Permutation(3)
permutation.generate()


