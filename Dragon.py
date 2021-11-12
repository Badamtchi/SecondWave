class Dragon:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def is_alive(self):
        return self.health > 0

    def get_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def talk(self):
        print(self.name, 'Health', self.health, '. Beat Me!')


def main():
    dragon_list = [Dragon('Smog'), Dragon('Alpha')]
    finish = False
    while not finish:
        dragon = dragon_list[0]
        dragon.talk()
        damage = int(input('>>> '))
        dragon.get_damage(damage)
        if not dragon.is_alive():  # remove from the list the dead dragon
            dragon_list.pop(0)
        if not dragon_list:
            finish = True
            print('You WON')


main()
