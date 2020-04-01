def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)  # top n - 1
        print("moving top disk from: ", fromPole, "to: ", toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


moveTower(3, "A", "B", "C")
