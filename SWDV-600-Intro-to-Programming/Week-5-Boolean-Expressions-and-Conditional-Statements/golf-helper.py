print("Welcome to the Golf Club Helper!")
print("Tell me your situation, and I'll recommend a club")
hit = ""
while hit.lower() != 'y' and hit.lower() != 'n':
    hit = input("\nDid you hit it on the green (y/n)? ")
if hit == "y":
    print("\nI recommend using your Putter")
else:
    dist = int(input("How far is the ball from the hole?"))
    if dist > 200:
        print("\nI recommend using your Driver")
    elif 140 < dist <= 200:
        print("\nI recommend using your 5-Iron")
    elif 100 < dist <= 140:
        print("\nI recommend using your 9-Iron")
    else:
        print("\nI recommend using your Pitching Wedge")
