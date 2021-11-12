
def dragon_create():
    global health
    health = 100


def dragon_is_alive():
    return health > 0


def dragon_get_damage(damage):
    global health
    health -= damage
    if health < 0:
        health = 0


def dragon_talk():
    print('My Health', health, '. Beat Me!')


def main():
    dragon_create()
    finish = False
    while not finish:
        dragon_talk()
        damage = int(input('>>> '))
        dragon_get_damage(damage)
        if not dragon_is_alive():
            finish = True
            print('You WON')

main()