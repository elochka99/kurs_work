def Dijkstra(N, S, matr):
        valid = [True]*N        
        weight = [1000000]*N
        weight[S] = 0
        pred = {}
        for i in range(N):
                pred[i + 1] = []
        for i in range(N):
                min_weight = 1000001
                ID_min_weight = -1
                for j in range(len(weight)):
                        if valid[j] and weight[j] < min_weight:
                                min_weight = weight[j]
                                ID_min_weight = j
                for j in range(N):
                        if weight[ID_min_weight] + matrix[ID_min_weight][j] < weight[j]:
                                weight[j] = weight[ID_min_weight] + matrix[ID_min_weight][j]
                                pred[j + 1].append(ID_min_weight + 1)
                valid[ID_min_weight] = False
        return [weight, pred]

def main():
        while True:
                try:
                        number = int(input("Введите количество вершин: "))
                except ValueError:
                        print("Ошибка ввода попробуйте еще раз")
                else:
                        break
        
        """Ввод Матрицы"""
        matrix = []
        print("Ввод матрицы")
        for i in range(number):
                matrix.append([])
                for j in range(number):
                        while True:
                                try:
                                        matrix[i].append(float(input("MATRIX[%d][%d]: " % (i + 1, j + 1))))
                                except ValueError:
                                        print("Ошибка ввода попробуйте еще раз")
                                else:
                                        break

        print("Ваш масив:")
        print('   ', end='')
        for i in range(number):
                print('%d  ' % (i + 1), end='')
        print()
        for i in range(number):
                print('%d  ' % (i + 1), end='')
                for j in range(number):
                        print('%.2f  ' % (matrix[i][j]), end='')
                print()
        while True:
                try:
                        vershina = int(input("З якої вершиини розпочати обхід: "))
                except ValueError:
                        print("Ошибка ввода попробуйте еще раз")
                else:
                        if vershina <= 0 or vershina > number:
                                print("вершина має бути від 1 до %i" %(number))
                        else:
                                break
        print("Результат роботи алгоритму Дейкстри:")
        print(Dijkstra(number, vershina - 1, matrix))

if __name__ == '__main__':
        main()
