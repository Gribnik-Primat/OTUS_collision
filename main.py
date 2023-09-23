class GameObject:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y


class CollisionDetector:
    def __init__(self):
        self.object_to_region = {}  # Словарь для отображения объектов на окрестности
        self.regions = []  # Список окрестностей

    def add_object(self, game_object):
        # Определение окрестности для объекта
        region = self.find_region(game_object)

        if region not in self.regions:
            self.regions.append(region)
            self.regions.sort(key=lambda r: r[0])  # Сортировка окрестностей по координате x

        if region in self.object_to_region:
            self.object_to_region[region].append(game_object)
        else:
            self.object_to_region[region] = [game_object]

    def find_region(self, game_object):
        # Пример разделения окрестностей - каждая окрестность представляет собой квадрат с центром в целых координатах
        region_x = int(game_object.x)
        region_y = int(game_object.y)
        return (region_x, region_y)

    def check_collisions(self):
        # Создаем макрокоманду для проверки коллизий в каждой окрестности
        macro_command = []
        for region in self.regions:
            if region in self.object_to_region:
                objects_in_region = self.object_to_region[region]
                for obj1 in objects_in_region:
                    for obj2 in objects_in_region:
                        if obj1 != obj2:
                            # Создаем команду проверки коллизии для obj1 и obj2 и добавляем ее в макрокоманду
                            macro_command.append(self.check_collision(obj1, obj2))

        return macro_command

    def check_collision(self, obj1, obj2):
        # Здесь должна быть реализация функции проверки коллизии между двумя объектами
        # В данном примере просто возвращаем их идентификаторы
        return f"Collision between objects {obj1.id} and {obj2.id}"


# Тесты для класса CollisionDetector
def test_collision_detection():
    detector = CollisionDetector()
    obj1 = GameObject(1, 2.0, 3.0)
    obj2 = GameObject(2, 2.5, 3.5)
    obj3 = GameObject(3, 5.0, 6.0)

    detector.add_object(obj1)
    detector.add_object(obj2)
    detector.add_object(obj3)

    macro_command = detector.check_collisions()

    # Проверка наличия команд в макрокоманде
    assert len(macro_command) == 3

    # Проверка команд на соответствие ожидаемому результату
    assert macro_command[0] == "Collision between objects 1 and 2"
    assert macro_command[1] == "Collision between objects 2 and 1"
    assert macro_command[2] == "Collision between objects 1 and 3"


if __name__ == "__main__":
    test_collision_detection()
