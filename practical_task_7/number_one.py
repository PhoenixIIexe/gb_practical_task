class Matrix:
    def __init__(self, list_matrix):
        self.list_matrix = list_matrix

    def __str__(self):
        for i in self.list_matrix:
            for g in i:
                print(f"{g:4}", end="")
            print()


    def __add__(self, other):
        print('Матрица: ')
        for i in range(len(self.list_matrix)):
            for g in range(len(other.list_matrix[i])):
                self.list_matrix[i][g] += other.list_matrix[i][g]
        return Matrix.__str__(self)


matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_matrix = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

matrix.__add__(new_matrix)