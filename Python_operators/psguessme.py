from random import randint


class GuessMe:
    def __init__(self, max_chance=10):
        self.rand_value = randint(1, 1000)
        self.max_chance = max_chance
        self.__play()

    def __play(self):
        chance = 1

        while chance <= self.max_chance:
            try:
                prompt = "Chance : {}\nenter the nubmer :".format(chance)
                user_value = int(input(prompt))
            except ValueError as err:
                print(err)
                print()
                continue

            if user_value == self.rand_value:
                print('you won !!!!!!')
                break
            elif user_value < self.rand_value:
                print(user_value, ': lesser')
            else:
                print(user_value, ': greater')
            chance += 1
            print()
        else:
            print('you lost')


GuessMe()
