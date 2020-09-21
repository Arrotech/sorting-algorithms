class Algorithms:
    """Class Initialization."""

    def __init__(self, n=0):
        """Constructor."""
        super().__init__()
        self.n = n

    def check(self):
        """If else and elif statements."""
        if self.n % 2 == 0:
            print(f"{self.n} is an even number")
        elif self.n % 2 != 0 and self.n > 10:
            print(f"{self.n} is not an even number and it's greater than 10")
        else:
            print(f"{self.n} is not an even number and it's less than 10")

    def for_loops(self, y, m):
        """For loops."""
        for x in range(y, self.n, m):
            print(x)

    def for_loop_lists(self):
        """For loops and lists."""
        cars = ["hurrier", "rumion", "land cruiser", "pajero"]
        for x in cars:
            if x == "land cruiser":
                continue
            print(x)

    def while_loops(self):
        error = self.n
        while error > 5:
            error = error/2
            print(error)

    def algorithms(self):
        cars_tuple = ["hurrier", "rumion", "land cruiser", "pajero"]
        cars_tuple.sort()


def sortedData():
    cars_tuple = ["harun", "alex", "john",
                  "john", "jane", "aaron", "john", "jane"]
    cars_tuple.sort()
    print(cars_tuple)
    for i in set(cars_tuple):
        n = ((cars_tuple.count(i))/len(cars_tuple))* 100
        print(n,"%")
        if n > 5:
            return n
            



print(sortedData())
