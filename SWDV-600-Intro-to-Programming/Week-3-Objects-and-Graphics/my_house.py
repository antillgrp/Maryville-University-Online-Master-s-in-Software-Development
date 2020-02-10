import sched
from random import randint

from graphics import *

win = GraphWin('Colorful House', 800, 600)
win.setBackground(color_rgb(102, 255, 255))
# infield circle
shape = Circle(Point(100, 500), 200)
shape.setFill(color_rgb(196, 153, 108))
shape.setOutline(color_rgb(196, 153, 108))
shape.draw(win)
shape = Circle(Point(300, 500), 200)
shape.setFill(color_rgb(196, 153, 108))
shape.setOutline(color_rgb(196, 153, 108))
shape.draw(win)
shape = Circle(Point(500, 500), 200)
shape.setFill(color_rgb(196, 153, 108))
shape.setOutline(color_rgb(196, 153, 108))
shape.draw(win)
shape = Circle(Point(700, 500), 200)
shape.setFill(color_rgb(196, 153, 108))
shape.setOutline(color_rgb(196, 153, 108))
shape.draw(win)
# left side front
shape = Polygon(
    Point(300, 320),
    Point(300, 480),
    Point(180, 460),
    Point(180, 300),
    Point(240, 200)
)
shape.setOutline(color_rgb(255, 255, 255))
shape.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
shape.draw(win)
# left side  window front
shape = Polygon(
    Point(280, 420),
    Point(200, 405),
    Point(200, 315),
    Point(280, 330)
).draw(win)
shape.setOutline(color_rgb(255, 255, 255))
shape.setWidth(5)
shape.setFill(color_rgb(153, 204, 255))
# window's bars
Line(Point(280, 360), Point(200, 345)).draw(win).setFill("white")
Line(Point(220, 321), Point(220, 411)).draw(win).setFill("white")
Line(Point(240, 323), Point(240, 413)).draw(win).setFill("white")
Line(Point(260, 325), Point(260, 415)).draw(win).setFill("white")
# left side side wall
shape = Polygon(
    Point(300, 320),
    Point(300, 480),
    Point(450, 460),
    Point(450, 310)
)
shape.setOutline(color_rgb(255, 255, 255))
shape.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
shape.draw(win)
# left side wall window
shape = Polygon(
    Point(330, 420),
    Point(420, 408),
    Point(420, 340),
    Point(330, 352)
).draw(win)
shape.setOutline(color_rgb(255, 255, 255))
shape.setFill(color_rgb(153, 204, 255))
shape.setWidth(5)
Line(Point(420, 370), Point(330, 382)).draw(win).setFill("white")
Line(Point(360, 347), Point(360, 415)).draw(win).setFill("white")
Line(Point(390, 343), Point(390, 412)).draw(win).setFill("white")
# left side wall circle window
shape = Circle(Point(240, 280), 25).draw(win)
shape.setOutline(color_rgb(255, 255, 255))
shape.setWidth(5)
shape.setFill(color_rgb(153, 204, 255))
# left side roof front
shape = Polygon(
    Point(240, 200),
    Point(310, 340),
    Point(320, 330),
    Point(240, 180),
    Point(160, 300),
    Point(175, 310)
)
shape.setOutline(color_rgb(255, 255, 255))
shape.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
shape.draw(win)
# left side roof
shape = Polygon(
    Point(240, 180),
    Point(500, 190),
    Point(560, 310),
    #
    Point(320, 330)
)
shape.setOutline(color_rgb(255, 255, 255))
shape.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
shape.draw(win)
# chimney
shape = Polygon(
    Point(360, 160),
    Point(360, 210),
    Point(375, 240),
    Point(400, 238),
    Point(400, 160),
    Point(375, 155)
)
shape.setOutline(color_rgb(255, 255, 255))
shape.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
shape.draw(win)
shape = Line(Point(375, 155), Point(375, 240))
shape.setOutline(color_rgb(255, 255, 255))
shape.draw(win)
# right side front
shape = Polygon(
    Point(585, 300),
    Point(585, 480),
    Point(660, 470),
    Point(660, 280),
    Point(620, 200)
)
shape.setOutline(color_rgb(255, 255, 255))
shape.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
shape.draw(win)
# left side wall circle window
shape = Circle(Point(625, 280), 25).draw(win)
shape.setOutline(color_rgb(255, 255, 255))
shape.setWidth(5)
shape.setFill(color_rgb(153, 204, 255))

# right side side wall
shape = Polygon(
    Point(450, 310),
    Point(450, 460),
    Point(585, 480),
    Point(585, 300)
)
shape.setOutline(color_rgb(255, 255, 255))
shape.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
shape.draw(win)
# right side side wall door
shape = Polygon(
    Point(490, 465),
    Point(550, 475),
    Point(550, 343),
    Point(490, 340)
)
shape.setOutline(color_rgb(255, 255, 255))
shape.setWidth(5)
shape.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
shape.draw(win)
Circle(Point(500, 400), 4).draw(win).setFill("black")
# right side roof
shape = Polygon(
    Point(440, 210),
    Point(620, 180),
    Point(570, 300),
    #
    Point(420, 300)
)
shape.setOutline(color_rgb(255, 255, 255))
shape.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
shape.draw(win)
# right side roof front
shape = Polygon(
    Point(570, 300),
    Point(580, 310),
    Point(620, 200),
    #
    Point(670, 300),
    Point(680, 290),
    Point(620, 180)
)
shape.setOutline(color_rgb(255, 255, 255))
shape.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
shape.draw(win)
# right side roof edge
shape = Polygon(
    Point(580, 310),
    Point(430, 310),
    Point(420, 300),
    Point(570, 300)
)
shape.setOutline(color_rgb(255, 255, 255))
shape.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
shape.draw(win)

# SUN
# left side wall circle window
sun = Circle(Point(30, 30), 50).draw(win)
sun.setOutline(color_rgb(255, 255, 0))
sun.setWidth(5)
sun.setFill(color_rgb(255, 255, 0))


def create_bush(point, winObj):
    # Main circle
    circles = [
        Circle(Point(point.getX() - 25, point.getY() + 5), 20),
        Circle(point, 25),
        Circle(Point(point.getX() + 25, point.getY() + 5), 20)
    ]
    for circle in circles:
        circle.setOutline(color_rgb(0, 76, 0))
        circle.setFill(color_rgb(0, 76, 0))
        circle.draw(winObj)


create_bush(Point(90, 370), win)
create_bush(Point(230, 470), win)
create_bush(Point(730, 300), win)
create_bush(Point(390, 460), win)

shape = Text(Point(410, 520), "Welcome to my colorful house").draw(win)
shape.setSize(36)
shape.setStyle("bold")
shape = Text(Point(410, 570), "Touch the sun to animate").draw(win)
shape.setSize(20)
shape.setStyle("bold")


class Sky:
    def __init__(self, window):
        self.win = window
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.setup_sky()

    def create_cloud(self, point):
        # Main circle
        circles = [
            Circle(Point(point.getX() - 25, point.getY()), 20),
            Circle(point, 25),
            Circle(Point(point.getX() + 25, point.getY()), 20)
        ]
        for circle in circles:
            circle.setOutline(color_rgb(204, 255, 255))
            circle.setFill(color_rgb(204, 255, 255))
            circle.draw(self.win)
        return circles

    def setup_sky(self):
        # https://stackoverflow.com/a/8731246
        self.scheduler.enter(0.3, 1, self.animate_cloud,
                             argument=(self.create_cloud(Point(randint(100, 250), randint(30, 70))), self.scheduler))
        self.scheduler.enter(0.3, 1, self.animate_cloud,
                             argument=(self.create_cloud(Point(randint(350, 450), randint(30, 70))), self.scheduler))
        self.scheduler.enter(0.3, 1, self.animate_cloud,
                             argument=(self.create_cloud(Point(randint(600, 750), randint(30, 70))), self.scheduler))

    def animate_cloud(self, cloud, scheduler):
        if cloud[1].getCenter().getX() + 25 + 20 >= 0:
            # print(cloud)
            for circle in cloud:
                circle.move(-3, 0)
            scheduler.enter(0.3, 1, self.animate_cloud, argument=(cloud, scheduler))
        else:
            dy = randint(10, 30)
            dx = randint(0, 20)
            for circle in cloud:
                circle.move(800 + 45 + dx, dy if circle.getCenter().getY() + dy < 100 else dy * -1)
            scheduler.enter(0.3, 1, self.animate_cloud, argument=(cloud, scheduler))

    def animate_sky(self):
        self.scheduler.run()

    def stop_animation(self):
        self.scheduler.queue.clear()


# for x in range(0, 800, 10):
#     Line(Point(x, 0), Point(x, 600)).draw(win)
#     if x % 40 == 0:
#         Text(Point(x, 10), x).draw(win)
# for y in range(0, 600, 10):
#     Line(Point(0, y), Point(800, y)).draw(win)
#     if y % 40 == 0:
#         Text(Point(10, y), y).draw(win)


# for clickCount in range(10):
#     clickPoint = win.getMouse()
#     Text(clickPoint, clickPoint).draw(win)
#     Text(clickPoint, "X").draw(win)


# int inline inCircle( int x, int y ){  // 19.1, 19.1, 19.1
#   int dx = ABS(x-xo);
#   if (    dx >  R ) return FALSE;
#   int dy = ABS(y-yo);
#   if (    dy >  R ) return FALSE;
#   if ( dx+dy <= R ) return TRUE;
#   return ( dx*dx + dy*dy <= R*R );
# }

# https://stackoverflow.com/a/7227057
def pointInsideSun(point):
    dx = abs(point.getX() - sun.getCenter().getX())
    if dx > sun.getRadius():
        return False
    dy = abs(point.getY() - sun.getCenter().getY())
    if dy > sun.getRadius():
        return False
    if dx + dy <= sun.getRadius():
        return True
    return dx ** 2 + dy ** 2 <= sun.getRadius() ** 2


sky = Sky(win)  # .animate_sky()

while not pointInsideSun(win.getMouse()):
    pass

sky.animate_sky()


