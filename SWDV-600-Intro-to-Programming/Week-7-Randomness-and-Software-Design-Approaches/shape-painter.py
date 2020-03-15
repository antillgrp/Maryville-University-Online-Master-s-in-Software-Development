from graphics import *


def getColor(colorString):
    tokens = colorString.split(',')
    if len(tokens) == 3:
        return color_rgb(int(tokens[0]), int(tokens[1]), int(tokens[2]))
    elif len(colorString) > 0:
        return colorString.strip()
    else:
        return 'white'


def getPoint(pointString):
    x, y = pointString.split(',')
    return Point(int(x), int(y))


def getRadius(radiusString):
    return int(radiusString)


def parseRectangleLine(line):
    shapeStr, ulPtStr, lrPtStr, colorStr = line.split(';')
    ulPt = getPoint(ulPtStr)
    lrPt = getPoint(lrPtStr)
    color = getColor(colorStr)

    rectangle = Rectangle(ulPt, lrPt)
    rectangle.setFill(color)

    return rectangle


def parseCircleLine(line):
    shapeStr, centerPtStr, radiusStr, colorStr = line.split(';')
    centerPt = getPoint(centerPtStr)
    radius = getRadius(radiusStr)
    color = getColor(colorStr)

    circle = Circle(centerPt, radius)
    circle.setFill(color)

    return circle


def getShapeName(line):
    tokens = line.split(';')
    return tokens[0]


def getShapes(drawingFile):
    shapes = []
    lineNumber = 0
    for line in drawingFile:
        lineNumber = lineNumber + 1
        shapeName = getShapeName(line)
        shape = None
        if shapeName.casefold() == 'circle'.casefold():
            shape = parseCircleLine(line)
        elif shapeName.casefold() == 'rectangle'.casefold():
            shape = parseRectangleLine(line)
        else:
            raise ValueError('ERROR on line {0}: Invalid shape {1}'.format(lineNumber, shapeName))

        shapes.append(shape)
    return shapes


def drawShapes(shapes):
    win = GraphWin("Drawing", 500, 500)

    for shape in shapes:
        shape.draw(win)

    clickPoint = win.getMouse()


def main():
    # get file name
    fileName = input("Enter the drawing file name: ")

    # open the file
    drawingFile = open(fileName, 'r')

    # get the shapes
    shapes = getShapes(drawingFile)

    # draw the shapes
    drawShapes(shapes)


main()
