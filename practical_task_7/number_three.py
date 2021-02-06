class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)


    def __add__(self, other):
        return self.quantity + other.quantity


    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return sub if sub > 0 else 'Клетка исчезла'


    def __truediv__(self, other):
        return self.quantity // other.quantity


    def __mul__(self, other):
        return self.quantity * other.quantity


    def make_order(self, g):
        res = ''
        for i in range(int(self.quantity / g)):
            res += '*' * g + '\n'
        res += '*' * (self.quantity % g) + '\n'
        return res


cell = Cell(int(input()))
cell_two = Cell(int(input()))
print(cell + cell_two)
print(cell - cell_two)
print(cell * cell_two)
print(cell / cell_two)
print(cell.make_order(int(input("Количество ячеек в ряду: "))))