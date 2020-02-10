from graphics import *

win = GraphWin('Gradient Bar', 400, 230)


# win.setBackground(color_rgb(102, 255, 255))

def pointIsInsideCircle(point, circle):
    dx = abs(point.getX() - circle.getCenter().getX())
    if dx > circle.getRadius():
        return False
    dy = abs(point.getY() - circle.getCenter().getY())
    if dy > circle.getRadius():
        return False
    if dx + dy <= circle.getRadius():
        return True
    return dx ** 2 + dy ** 2 <= circle.getRadius() ** 2


def drawLabel(text, locationPoint):
    return Text(locationPoint, text).draw(win)


def drawSubButton(locationPoint):
    subButtonCl = Circle(locationPoint, 8).draw(win)
    subButtonCl.setFill("darkgrey")
    subButtonCl.setOutline("gray")
    subButtonTx = Text(Point(locationPoint.getX(), locationPoint.getY() - 1), '-').draw(win)
    subButtonTx.setSize(13)
    subButtonTx.setStyle("bold")
    return subButtonCl


def drawAddButton(locationPoint):
    addButtonCl = Circle(locationPoint, 8).draw(win)
    addButtonCl.setFill("darkgrey")
    addButtonCl.setOutline("gray")
    addButtonTx = Text(locationPoint, '+').draw(win)
    addButtonTx.setSize(13)
    addButtonTx.setStyle("bold")
    return addButtonCl


def drawFieldRect(locationPoint, width, height=18):
    fieldRect = Rectangle(
        Point(locationPoint.getX() - width // 2, locationPoint.getY() - height // 2),
        Point(locationPoint.getX() + width // 2, locationPoint.getY() + height // 2)
    ).draw(win)
    fieldRectTx = Text(locationPoint, "").draw(win)
    fieldRectTx.setSize(13)
    fieldRectTx.setStyle("bold")
    return fieldRectTx


def drawGradientBars(barsCount, red, green, blue):
    rectWide = 400 / barsCount
    # colorStep = 255 // barsCount
    for i in range(barsCount):
        rect = Rectangle(Point(rectWide * i, 28), Point(rectWide * (i + 1), 230)).draw(win)
        rect.setFill(color_rgb(red // barsCount * i, green // barsCount * i, blue // barsCount * i))
        rect.setOutline(color_rgb(red // barsCount * i, green // barsCount * i, blue // barsCount * i))


labelBars = drawLabel('Bars:', Point(21, 15))
subBtBars = drawSubButton(Point(21 + 28, 15))
fldTxBars = drawFieldRect(Point(21 + 28 + 8 + 2 + 20, 15), 40)
addBtBars = drawAddButton(Point(21 + 28 + 8 + 2 + 40 + 2 + 8, 15))

labelR = drawLabel('R:', Point(21 + 28 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5, 15))
subBtR = drawSubButton(Point(21 + 28 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8, 15))
fldTxR = drawFieldRect(Point(21 + 28 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8 + 8 + 2 + 20, 15), 40)
addBtR = drawAddButton(Point(21 + 28 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8 + 8 + 2 + 40 + 2 + 8, 15))

labelG = drawLabel('G:', Point(21 + 28 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5, 15))
subBtG = drawSubButton(
    Point(21 + 28 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8, 15))
fldTxG = drawFieldRect(
    Point(21 + 28 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8 + 8 + 2 + 20, 15),
    40)
addBtG = drawAddButton(Point(
    21 + 28 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8 + 8 + 2 + 40 + 2 + 8, 15))

labelB = drawLabel('B:', Point(
    21 + 28 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5,
    15))
subBtB = drawSubButton(Point(
    21 + 28 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8,
    15))
fldTxB = drawFieldRect(Point(
    21 + 28 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8 + 8 + 2 + 20,
    15), 40)
addBtB = drawAddButton(Point(
    21 + 28 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8 + 8 + 2 + 40 + 2 + 8 + 8 + 8.5 + 8.5 + 8 + 8 + 2 + 40 + 2 + 8,
    15))

barsDelta = 1
r = 255
g = 0
b = 0
fldTxBars.setText(barsDelta * 6)
fldTxR.setText(r)
fldTxR.setTextColor("red")
fldTxG.setText(g)
fldTxG.setTextColor("green")
fldTxB.setText(b)
fldTxB.setTextColor("blue")
drawGradientBars(barsDelta * 6, r, g, b)

while True:
    clickPoint = win.getMouse()
    if pointIsInsideCircle(clickPoint, subBtBars):
        barsDelta = barsDelta - 1 if 1 <= barsDelta - 1 <= 42 else 1
    if pointIsInsideCircle(clickPoint, addBtBars):
        barsDelta = barsDelta + 1 if 1 <= barsDelta + 1 <= 42 else 42
    if pointIsInsideCircle(clickPoint, subBtR):
        r = r - 5 if 0 <= r - 5 <= 255 else 0
    if pointIsInsideCircle(clickPoint, addBtR):
        r = r + 5 if 0 <= r + 5 <= 255 else 255
    if pointIsInsideCircle(clickPoint, subBtG):
        g = g - 5 if 0 <= g - 5 <= 255 else 0
    if pointIsInsideCircle(clickPoint, addBtG):
        g = g + 5 if 0 <= g + 5 <= 255 else 255
    if pointIsInsideCircle(clickPoint, subBtB):
        b = b - 5 if 0 <= b - 5 <= 255 else 0
    if pointIsInsideCircle(clickPoint, addBtB):
        b = b + 5 if 0 <= b + 5 <= 255 else 255
    fldTxBars.setText(barsDelta * 6)
    fldTxR.setText(r)
    fldTxG.setText(g)
    fldTxB.setText(b)
    drawGradientBars(barsDelta * 6, r, g, b)
