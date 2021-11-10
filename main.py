def main():
    x, y = 100, 100
    width, height = 200, 200

    draw_house(x, y, width, height)

def draw_house(x, y, width, height):
    """
    Function of Modeling House by Width and Height at coordination (x, y),
    which located in the centre of project.
    :param x: Coordination of X in the base middle of the project
    :param y: Coordination of Y in the base middle of the project
    :param width: Full width of pgroject
    :param height: Full height of the project
    :return: None
    """
    print('Typical Modeling of House @', x, y, width, height)
    foundation_height = 0.05 * height


    draw_house_foundation(x, y, width, height)
    draw_house_walls()
    draw_house_roof()




main()