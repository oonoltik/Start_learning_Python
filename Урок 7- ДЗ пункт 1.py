class Matrix:
    def __init__(self, a):
        self.b = '\n'.join(['\t'.join([str(j) for j in i]) for i in a])
        List = []
        for i in a:
            List.append([j for j in i])
        self.a = List

    def __str__(self):
        self.c = str(self.b)
        return self.c

    def __add__(self, other):
        NumStr = len(self.a)
        NumCol = len(other.a[0])
        for i in range(NumStr):
            for j in range(NumCol):
                self.a[i][j] = self.a[i][j] + other.a[i][j]
            Result = self.a
        return Matrix(Result)

m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)

print("\nВариант без использования классов:")

m1= [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

m2= [[0, 1, 0], [20, 0, -1], [-1, -2, 0]]

result = [[0,0,0],[0,0,0],[0,0,0]]

# iterate through rows
for i in range(len(m1)):
    for j in range(len(m1[0])):
        result[i][j] = m1[i][j] + m2[i][j]


for r in result:
      # print("  ".join([str(elem) for elem in r]))
      print(''.join('\t'.join([str(elem) for elem in r])))

      # print('\n'.join(['\t'.join([str(j) for j in i]) for i in r])
# for row in a:
#     print(" ".join([str(elem) for elem in row]))