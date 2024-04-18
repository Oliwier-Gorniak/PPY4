import random as rand


class Car:
    def __init__(self, brand, year, price):
        self.brand = brand
        self.year = year
        self.price = price

    def __str__(self):
        return f"Brand: {self.brand}, Year: {self.year}, Price: {self.price}"


def print_cars(matrix: list[list[Car]]):
    oldest_price = max(matrix[i][j].price for i in range(len(matrix)) for j in range(len(matrix)) if j > i and j + i < len(matrix))
    for row in matrix:
        for car in row:
            if 'f' not in car.brand and 'z' not in car.brand and car.price < oldest_price:
                print(f"| Brand: {car.brand}, Year: {car.year}, Price: {car.price}", end=" ")
        print()


def increase_price(matrix: list[list[Car]]):
    youngest_price = min(matrix[i][j].price for i in range(len(matrix)) for j in range(len(matrix)) if
                         j != 0 and j != len(matrix) - 1 and i != 0 and i != len(matrix) - 1)
    for i in range(len(matrix)):
        while matrix[i][-1].price > matrix[i][0].price:
            for j in range(len(matrix) - 1):
                matrix[i][j].price += youngest_price
    return matrix


def increase_cheapest(matrix: list[list[Car]]):
    diagonal = [matrix[i][i] for i in range(len(matrix))]
    cheapest = sorted(diagonal, key=lambda x: x.price)[:2]
    for car in cheapest:
        car.price *= 1.15
    return matrix


def main():
    n = int(input("Enter the size of the matrix: "))
    matrix1 = [[Car("brand", int(rand.random() * 24 + 1970), i * j * 10000 + 10000) for i in range(n)] for j in range(n)]
    matrix2 = [[Car("brand", int(rand.random() * 24 + 1970), (n - i) * (n - j) * 10000 + 10000) for i in range(n)] for j in
               range(n)]

    for row in matrix1:
        for car in row:
            print(f"| {car.__str__()}", end=" ")
        print()
    print()
    matrix1 = increase_price(matrix1)
    for row in matrix1:
        for car in row:
            print(f"| {car.__str__()}", end=" ")
        print()
    print()
    print_cars(matrix1)
    print()
    matrix1 = increase_cheapest(matrix1)
    for row in matrix1:
        for car in row:
            print(f"| {car.__str__()}", end=" ")
        print()
    print()

    for row in matrix2:
        for car in row:
            print(f"| {car.__str__()}", end=" ")
        print()
    print()
    matrix2 = increase_price(matrix2)
    for row in matrix2:
        for car in row:
            print(f"| {car.__str__()}", end=" ")
        print()
    print()
    print_cars(matrix2)
    print()
    matrix2 = increase_cheapest(matrix2)
    for row in matrix2:
        for car in row:
            print(f"| {car.__str__()}", end=" ")
        print()
    print()


if __name__ == '__main__':
    main()
