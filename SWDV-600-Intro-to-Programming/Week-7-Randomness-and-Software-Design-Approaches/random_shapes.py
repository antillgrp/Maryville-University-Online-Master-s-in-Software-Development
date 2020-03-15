from random import randint


class RandShapesGenIter:

    def __init__(self, count=1, winWidth=500, winHeight=500):
        if count <= 0:
            raise ValueError("count must be higher than 0")
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        # Stop iteration if limit is reached
        if self.count == 0:
            raise StopIteration
        self.count -= 1
        shape = "{};".format(["Circle", "Rectangle"][randint(0, 3000) % 2])
        props = ""
        if shape == "Circle;":
            centerX = randint(0, self.winWidth)
            centerY = randint(0, self.winHeight)
            props += "{}, {}; {};".format(
                centerX,
                centerY,
                randint(1, max(1, min(centerX, self.winWidth - centerX, centerY, self.winHeight - centerY)))
            )
        else:
            props += "{}, {}; {}, {};".format(
                randint(0, self.winWidth),
                randint(0, self.winHeight),
                randint(0, self.winWidth),
                randint(0, self.winHeight)
            )
        color = "{}, {}, {}".format(randint(100, 200), randint(100, 200), randint(100, 200))
        return "{} {} {}".format(shape, props, color)


def main():
    with open(input("Enter the drawing file name to create: "), 'w') as shapesFile:
        for shape in RandShapesGenIter(int(input("Enter the number of shapes to make: "))):
            print(shape)
            shapesFile.write(shape + "\n")


main()
