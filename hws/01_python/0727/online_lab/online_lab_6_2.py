class dog:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, dog_name, dog_breed):
        self.name = dog_name
        self.breed = dog_breed
        dog.num_of_dogs += 1
        dog.birth_of_dogs += 1

    def bark(self):
        print("왈왈!")

    def __del__(self):
        dog.birth_of_dogs -= 1

    @classmethod
    def get_status(cls):
        print(f'현재 강아지는 총 {cls.num_of_dogs}마리이며 태어난 강아지는 총 {cls.birth_of_dogs}마리입니다')
