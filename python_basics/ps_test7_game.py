from random import randint


class GuessNumber:
    def __init__(self):
        print("I am construcor")

    def __del__(self):
        print("I am destructor")

    def get_random_number(self):
        return randint(1,1000)

    def guess_number(self,random):
        i = 1
        print(random)
        guess = self.get_number(i)
        while i < 10:
            if guess == random:
                print("Yeah!! You got the number")
                break
            elif guess > random:
                print("The guessed number is greater than the required number")
                i += 1
                guess = self.get_number(i)
                continue
            elif guess < random:
                print("The guessed number is lesser than the required number")
                i += 1
                guess = self.get_number(i)
                continue
            else:
                pass
        if i >= 10:
            print("Sorry!! You loose the game")

    def get_number(self, i):
        try:
            num = int(input("This is your {} attempt. Guess:".format(i)))
        except Exception as e:
            print(e)
        finally:
            pass
        return num

g = GuessNumber()
random = g.get_random_number()
g.guess_number(random)


