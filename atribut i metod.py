class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = 7

    def go_to(self, new_floor):
        new_floor = 8
        for i in range(1, new_floor):
            print(i)
        if new_floor > self.number_of_floors or self.number_of_floors < 1:
            print('Такого этажа не существует')


lil = House('ЖК Лилия', 7)
lil.go_to(5)
lil = House('ЖК Горский', 18)
lil.go_to(10)
