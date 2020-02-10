import gtoolsmod as gt

scoresCount = int(gt.validFloatInputRequest("How many days of scores?", "(greater than 0): ", lambda x: x > 0))

accumulator = 0
for score in range(1, scoresCount + 1):
    accumulator += int(gt.validFloatInputRequest("Enter score for day %s: " % str(score)))

print("The total score of the %s days is %s" % (scoresCount, accumulator))
