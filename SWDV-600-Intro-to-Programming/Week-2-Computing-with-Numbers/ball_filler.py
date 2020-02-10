import math
import gtoolsmod as gt

# can vary from 8.4 to 8.6 inches
intended_diameter = gt.validFloatInputRequest("What is the diameter of each ball in inches?\n",
                                              "Please enter a number between 8.4 trough 8.6: ",
                                              lambda x: 8.4 <= x <= 8.6)

core_volume = gt.validFloatInputRequest("What is the core volume in inches cubed?\n",
                                        "Please enter a number greater than 0: ",
                                        lambda x: x > 0)

numberOfBalls = int(gt.validFloatInputRequest("How many bowling balls will be manufactured?\n",
                                              "Please enter a number greater than 0: ",
                                              lambda x: x > 0))

oneBallFillerVol = 4 * math.pi * (intended_diameter / 2) ** 3 / 3 - core_volume

print("You will need %s inches cubed of filler" % (oneBallFillerVol * numberOfBalls))
