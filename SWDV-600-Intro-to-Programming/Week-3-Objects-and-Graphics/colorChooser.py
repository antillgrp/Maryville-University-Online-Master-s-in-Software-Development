import graphics as g
from graphics import *

win = g.GraphWin('Click to update the background color', 640, 320)

Text(Point(40, 40), 'Red').draw(win)
Text(Point(40, 80), 'Green').draw(win)
Text(Point(40, 120), 'Blue').draw(win)

redEntry = Entry(Point(80, 40), 3)
greenEntry = Entry(Point(80, 80), 3)
blueEntry = Entry(Point(80, 120), 3)

redEntry.setText(255)
greenEntry.setText(255)
blueEntry.setText(255)

redEntry.draw(win)
greenEntry.draw(win)
blueEntry.draw(win)

for clickCount in range(50):
    clickPoint = win.getMouse()
    win.setBackground(g.color_rgb(int(redEntry.getText()), int(greenEntry.getText()), int(blueEntry.getText())))
