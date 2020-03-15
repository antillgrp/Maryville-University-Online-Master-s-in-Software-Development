# SINGLETON
gameObjects = {}


def retrieveOrCrateObject(
        # basic props
        name, descr="no description",
        # self props
        grabbable=False, breakable=False, killable=False, talks=False,
        opens=False, closed=False, locked=False, accepts=False,
        # interaction with other objects props
        brakes=False,  # breakable objects
        unlocks=False,  # locked objects
        kills=False,  # killable objects
        canBeGiven=False,  # accepts objects
):
    if not name in gameObjects.keys():
        gameObjects[name] = {
            "name": name,
            "desc": descr,
            # self props
            "grabbable": grabbable, "breakable": breakable, "killable": killable,
            "talks": talks, "opens": opens, "closed": closed, "accepts": accepts, "locked": locked,
            # interaction with other objects props
            "brakes": brakes, "unlocks": unlocks, "kills": kills, "canBeGiven": canBeGiven
        }
    return gameObjects[name]


gameState = {
    "status": {
        "isWon": False,
        "isLost": False,
        "reason": ""
    },
    "player": {
        "name": "NoName",
        # The default stating location will be "the garden"
        # "location": "the sorcery room", "the lobby"
        "location": "the garden",
        "inventory": {}
    },
    "rooms": {
        # 0
        "the garden": {
            "accesses": [
                {
                    "dir": "North", "next-room": "the lobby",
                    "door": retrieveOrCrateObject(
                        "an oak door",
                        descr="The Oblemur's Mansion front door",
                        breakable=True,  # no ax at this point
                        opens=True,
                        closed=True,
                    )
                }
            ],
            "objects": {
                "an oak door": retrieveOrCrateObject("an oak door")
            }
        },
        # 1
        "the lobby": {
            "accesses": [
                {"dir": "North", "next-room": "the inner courtyard", "door": None},
                {"dir": "South", "next-room": "the garden", "door": retrieveOrCrateObject("an oak door")},
                {"dir": "East", "next-room": "the living room", "door": None},
            ],
            "objects": {
                "an oak door": retrieveOrCrateObject("an oak door"),
                "an inscription": retrieveOrCrateObject(
                    "an inscription",
                    descr="Reads: Be welcome to the Oblemur's Mansion. Be wise nothing is what it looks.",
                    breakable=True,
                ),
                "an ax": retrieveOrCrateObject(
                    "an ax",
                    descr="Just an ax to brake things or kill persons",
                    grabbable=True,
                    brakes=True,
                    kills=True,
                    canBeGiven=True  # if given to majordomo he kills you making you loose
                ),
            }
        },
        # 2
        "the living room": {
            "accesses": [
                {"dir": "West", "next-room": "the lobby", "door": None},
                {"dir": "East", "next-room": "the library", "door": None}
            ],
            "objects": {
                "a vase": retrieveOrCrateObject(
                    "a vase",
                    descr="A vase that can be filled out with water and pour water over other object",
                    grabbable=True,
                    # Break "a vase" makes you loose
                    breakable=True
                ),
                "an oil lamp": retrieveOrCrateObject(
                    "an oil lamp",
                    descr="A lamp to light up when is too dark.",
                    grabbable=True,
                    # Breaking it make you loose
                    breakable=True
                ),
            },
        },
        # 3
        "the library": {
            "accesses": [
                {"dir": "West", "next-room": "the living room", "door": None},
                # Shows up when the sorcery book is read in the sorcery room
                # {"dir": "North", "next-room": "the sorcery room", "closed": False}
            ],
            "objects": {
                "a bookshelf": retrieveOrCrateObject(
                    "a bookshelf",
                    descr="A bookshelf full of dusty books, its noticeable a thick blank from a missing book.",
                    breakable=True
                ),
                "a majordomo": retrieveOrCrateObject(
                    "a majordomo",
                    descr="A man with a sinister look, an empty cup of wine in one hand and an empty wine bottler in the other one.",
                    # Kill him makes you loose
                    killable=True,
                    talks=True,
                    accepts=True
                ),
            },
        },
        # 4
        "the inner courtyard": {
            "accesses": [
                {"dir": "South", "next-room": "the lobby", "door": None},
                {
                    "dir": "East", "next-room": "the red room",
                    "door": retrieveOrCrateObject(
                        "a red door",
                        descr="A blood red door with skulls and snakes decorations.",
                        opens=True,
                        closed=True
                    )
                }
            ],
            "objects": {
                "a red door": retrieveOrCrateObject("an red door"),
                "a fountain": retrieveOrCrateObject(
                    "a fountain",
                    descr="A water fountain with a daemon figure stepping on top of skulls and snakes.",
                    # Breaking it before grabbing the water makes you loose
                    breakable=True
                ),
                "water": retrieveOrCrateObject(
                    "water",
                    descr="Water that can be taken with a proper container.",
                    # You need to have the vase in your inventory
                    grabbable=True
                ),
            },
        },
        # 5
        "the red room": {
            "accesses": [
                # not visible until the majordomo reveals it for you after you give him the wine
                # {"dir": "North", "next-room": "the hidden room", "door": None}
                {"dir": "West", "next-room": "the inner courtyard", "door": retrieveOrCrateObject("a red door")},
                {
                    "dir": "East", "next-room": "the sorcery room",
                    "door": retrieveOrCrateObject(
                        "an iron door",
                        descr="A black iron door.",
                        opens=True,
                        closed=True
                    )
                }
            ],
            "objects": {
                "an iron door": retrieveOrCrateObject("an iron door"),
                "a bottle of wine": retrieveOrCrateObject(
                    "a bottle of wine",
                    descr="Just a bottle of wine",
                    # Breaking it makes you loose
                    grabbable=True,
                    breakable=True,
                    canBeGiven=True
                ),
                "a red bed": retrieveOrCrateObject(
                    "a red bed",
                    descr="A red bed that match with the decoration of whole room"
                ),
            },
        },
        # 6
        "the sorcery room": {
            "accesses": [
                {"dir": "North", "next-room": "the fireplace", "door": None},
                {"dir": "West", "next-room": "the red room", "door": retrieveOrCrateObject("an iron door")}
            ],
            "objects": {
                "an iron door": retrieveOrCrateObject("an iron door"),
                "a daemon statue": retrieveOrCrateObject(
                    "a daemon statue",
                    descr="A replica of the daemon figure seen earlier on the fountain.",
                    # Breaking it makes you loose
                    breakable=True
                ),
                "a fire": retrieveOrCrateObject(
                    "a fire",
                    descr="On the fireplace you see a big flames fire and a small stone object hanging in the wall right behind it.",
                    killable=True
                ),
                "an iron chest": retrieveOrCrateObject(
                    "an iron chest",
                    descr="A heavy iron chest locked with an stone lock with an engraving of a daemon face, totally dusty except for a rectangle of the size of a book free of dust.",
                    opens=True,
                    locked=True,
                    closed=True
                ),
            }
        },
        # 7
        "the hidden room": {
            "accesses": [
                # keeps open from this side there is no other way is or out
                {"dir": "South", "next-room": "the red room", "door": None}
            ],
            "objects": {
                "a sorcery book": retrieveOrCrateObject(
                    "a sorcery book",
                    descr="The most terrifying book ever seen. A bookmark is sticking out in a page with a big bold message of assorted words.",
                    grabbable=True,
                    # Breaking it make you loose
                    breakable=True,
                    # Opens the secret passage between the sorcery room and the library
                    opens=True,
                ),
            }

        },
        # 8
        "the fireplace": {
            "accesses": [
                {"dir": "South", "next-room": "the sorcery room", "door": None},
            ],
            "objects": {
                "an stone key": retrieveOrCrateObject(
                    "an stone key",
                    descr="An stone key with an engraving of the (fountain and statue) daemon's face.",
                    unlocks=True,
                    grabbable=True
                )
            }

        }
    },
}

availableCommands = {
    # help, inventory, look
    "fixed-glb-cmds": {
        "help": "General information of the Game, also available <help cmd> that tells what the command does.",
        "inventory": "List the objects you carry on you at the time is called.",
        "look": "List the objects (with description) you can see in the room where you are.",
    },
    "room-only-cmds": {},  # commands that are generated on the scene you are
    "inventory-cmds": {},  # commands that are generated from the possible actions with your inventory objects
}


def generateRoomOnlyCmds():

    availableCommands["room-only-cmds"] = {}

    # "room-only-cmds" for "accesses"
    for access in getCurrentRoom()["accesses"]:
        hasDoor = not access["door"] is None
        if hasDoor and access["door"]["closed"] and access["door"]["opens"]:

            availableCommands["room-only-cmds"][
                "open {}".format(access["door"]["name"])
            ] = "opens {} letting you go to location: {}".format(access["door"]["name"], access["next-room"])

        else:

            availableCommands["room-only-cmds"][
                "go {}".format(access["dir"])
            ] = "Takes you in direction {} to location: {}".format(access["dir"], access["next-room"])

    # "room-only-cmds" for "objects"
    for entry in getCurrentRoom()["objects"].keys():

        if getCurrentRoom()["objects"][entry]['opens'] and getCurrentRoom()["objects"][entry]['closed']:
            if not "open {}".format(entry) in availableCommands["room-only-cmds"].keys():  # is not a door
                availableCommands["room-only-cmds"][
                    "open {}".format(entry)
                ] = "Opens {}, if locked you might need to carry (inventory) some other object.".format(entry)

        if getCurrentRoom()["objects"][entry]['talks']:
            availableCommands["room-only-cmds"][
                "talk-to {}".format(entry)
            ] = "{} might have something to say.".format(entry)

        if getCurrentRoom()["objects"][entry]['grabbable']:

            # It's dark if you don't see you can't grab anything
            youHaveOilLamp = "an oil lamp" in gameState["player"]["inventory"].keys()
            if gameState["player"]["location"] == "the hidden room" and not youHaveOilLamp:
                continue

            availableCommands["room-only-cmds"][
                "grab {}".format(entry)
            ] = "Moves {} to the inventory.".format(entry)


def generateInventoryCmds():

    availableCommands["inventory-cmds"] = {}

    for inventoryObject in gameState["player"]["inventory"].keys():

        availableCommands["inventory-cmds"][
            "drop {}".format(inventoryObject)
        ] = "drops {}. You need to grab it to put it back to inventory".format(inventoryObject)

        if gameState["player"]["inventory"][inventoryObject]["opens"]:
            availableCommands["inventory-cmds"][
                "open {}".format(inventoryObject)
            ] = "opens your object: {}".format(inventoryObject)

        if gameState["player"]["inventory"][inventoryObject]["brakes"]:
            for roomObject in getCurrentRoom()["objects"].keys():
                if getCurrentRoom()["objects"][roomObject]["breakable"]:

                    # It's dark if you don't see you can't grab anything
                    youHaveOilLamp = "an oil lamp" in gameState["player"]["inventory"].keys()
                    if gameState["player"]["location"] == "the hidden room" and not youHaveOilLamp:
                        continue

                    availableCommands["inventory-cmds"][
                        "break {}".format(roomObject)
                    ] = "breaks {} with your object: {}".format(roomObject, inventoryObject)

        if gameState["player"]["inventory"][inventoryObject]["kills"]:
            for roomObject in getCurrentRoom()["objects"].keys():
                if getCurrentRoom()["objects"][roomObject]["killable"]:
                    availableCommands["inventory-cmds"][
                        "kill {}".format(roomObject)
                    ] = "kills {} with your object: {}".format(roomObject, inventoryObject)

        if gameState["player"]["inventory"][inventoryObject]["unlocks"]:
            for roomObject in getCurrentRoom()["objects"].keys():
                if getCurrentRoom()["objects"][roomObject]["locked"]:
                    availableCommands["inventory-cmds"][
                        "unlock {}".format(roomObject)
                    ] = "unlocks {} with your object: {}".format(roomObject, inventoryObject)

        if gameState["player"]["inventory"][inventoryObject]["canBeGiven"]:
            for roomObject in getCurrentRoom()["objects"].keys():
                if getCurrentRoom()["objects"][roomObject]["accepts"]:
                    availableCommands["inventory-cmds"][
                        "give {} to {}".format(inventoryObject, roomObject)
                    ] = "is, you give object: {} to {}.".format(inventoryObject, roomObject)


def displayPlayerAndLocation():
    print("{}: your current location is: {}".format(gameState["player"]["name"], gameState["player"]["location"]))


def displayFlatCmdList(cmdList):
    if len(availableCommands[cmdList].keys()) < 1:
        return
    print(
        "{}: now you can type:{}".format(
            gameState["player"]["name"],
            ",".join(
                sorted(list(
                    map(
                        lambda command: " <{}>".format(command),
                        availableCommands[cmdList].keys()
                    )
                ))
            )
        )
    )


def displayInventory():
    for inventoryObject in gameState["player"]["inventory"].keys():
        print("(({})): {}".format(inventoryObject, gameState["player"]["inventory"][inventoryObject]["desc"]))


def displayLook():
    displayPlayerAndLocation()
    print("Here you can see:")

    youHaveOilLamp = "an oil lamp" in gameState["player"]["inventory"].keys()
    if gameState["player"]["location"] == "the hidden room" and not youHaveOilLamp:
        print("You are not able to see anything, it's too dark in here, try finding a lamp")
        return

    for roomObject in getCurrentRoom()["objects"].keys():
        print("(({})): {}".format(roomObject, getCurrentRoom()["objects"][roomObject]["desc"]))


def setGameLost(reason):
    gameState["status"]["isLost"] = True
    gameState["status"]["reason"] = reason


def setGameWon(reason):
    gameState["status"]["isWon"] = True
    gameState["status"]["reason"] = reason


def getCurrentRoom():
    return gameState["rooms"][gameState["player"]["location"]]


def goDir(direct):
    # Going North in "the sorcery room" make you loose if fire hasn't been killed
    fireNotKilled = "a fire" in getCurrentRoom()["objects"].keys()
    if gameState["player"]["location"] == "the sorcery room" and direct == "North" and fireNotKilled:
        gameState["status"]["isLost"] = True
        gameState["status"]["reason"] = "You've got burn, you needed firs to extinguish/kill the fire."

    # Going South in "the lobby" if you have the treasure you win
    youHaveTheTreasure = "a treasure" in gameState["player"]["inventory"].keys()
    if gameState["player"]["location"] == "the lobby" and direct == "South" and youHaveTheTreasure:
        gameState["status"]["isWon"] = True
        gameState["status"]["reason"] = "You made it out with the treasure."

    for access in getCurrentRoom()["accesses"]:
        if access["dir"] == direct:
            gameState["player"]["location"] = access["next-room"]
            print("You just walked to {}".format(gameState["player"]["location"]))
            break


def grabObject(obj):
    # To to grab water you need a vase inventory
    youHaveAVase = "a vase" in gameState["player"]["inventory"].keys()
    if obj == "water" and not youHaveAVase:
        print("To grab water you first need a vase. Please go find one.")
        return

    gameState["player"]["inventory"][obj] = getCurrentRoom()["objects"].pop(obj)
    print("(({})) has been successfully moved to your inventory, do <inventory>".format(obj))


def openObject(obj):

    # Opening "a sorcery book" in other than the sorcery room just close it back
    # Opening the sorcery book in the sorcery room adds an access to
    # the sorcery room: {"dir": "South", "next-room": "the library", "door": None}
    # the library : {"dir": "North", "next-room": "the sorcery room", "door": None}
    if obj == "a sorcery book":
        if gameState["player"]["location"] == "the sorcery room":
            gameObjects[obj]["closed"] = False
            print("(({})) has been successfully opened.".format(obj))
            gameState["rooms"]["the sorcery room"]["accesses"].append(
                {"dir": "South", "next-room": "the library", "door": None}
            )
            gameState["rooms"]["the library"]["accesses"].append(
                {"dir": "North", "next-room": "the sorcery room", "door": None}
            )
            print("Magic!!, a secret passage has got open, you now have a way out, do <help> to see how.")
        else:
            print("(({})) has been opened and closed back. Apparently nothing happened.")
        return

    # Opening an iron chest if don't have a sorcery book you loose reason: no way out
    if obj == "an iron chest" and gameObjects[obj]["closed"]:

        if gameObjects[obj]["locked"]:
            print("(({})) needs to be unlocked first. You might need a key to do so.".format(obj))
            return
        gameObjects[obj]["closed"] = False
        print("(({})) has been successfully opened.".format(obj))

        print("Suddenly, the black iron door behind you got close and locked. UUHHHmmm this is not good!\n")
        print("Also, see the hugest red sapphire seem ever inside the chest, you've finally found it !!")
        getCurrentRoom()["objects"]["an iron door"]["closed"] = True
        getCurrentRoom()["objects"]["an iron door"]["locked"] = True
        getCurrentRoom()["objects"]["a treasure"] = retrieveOrCrateObject(
            "a treasure", descr="The hugest red sapphire seem ever.", breakable=True, grabbable=True
        )

        if "a sorcery book" not in gameState["player"]["inventory"].keys():
            gameState["status"]["isLost"] = True
            gameState["status"]["reason"] = "You've got lock in the sorcery room, no possible way out."

        return

    if gameObjects[obj]["locked"]:
        print("(({})) is locked can't be opened.".format(obj))
    else:
        gameObjects[obj]["closed"] = False
        print("(({})) has been successfully opened.".format(obj))


def talkTo(person):
    # Assuming is a majordomo no validation needed
    print("{} says: I've been living for 300 years in this mansion. I know all it's secrets.".format(person))
    print("But all I wish I have now is one more wine sip. Then I might share some.")


def breakObject(obj):
    # Break "a bottle of wine" makes you loose reason: It was supposed to be given not broken
    if obj == "a bottle of wine":
        setGameLost("You needed a bottle of wine to find the treasure.")

    fireIsAlive = "a fire" in gameState["rooms"]["the sorcery room"]["objects"].keys()
    youHaveWater = "water" in gameState["player"]["inventory"].keys()
    if fireIsAlive and not youHaveWater:
        # Break "a vase" makes you loose reason: It is needed to grab water
        if obj == "a vase":
            setGameLost("The vase should not be broken, you need to carry water.")
        # Break "a fountain" if water is not in inventory makes you loose, reason: water
        if obj == "a fountain":
            setGameLost("Water comes from the fountain, and you need water to find the treasure")

    # Break "a demon statue" makes you loose reason: no exit of the sorcery room will be found
    if obj == "a demon statue" or obj == "a sorcery book":
        setGameLost("A malefic magic got you locked inside the Oblemu's mansion")

    # Break "an oil lamp" makes you loose reason: It is needed to light up a dark room
    if "a sorcery book" not in gameState["player"]["inventory"].keys():
        if obj == "an oil lamp":
            setGameLost("A room needed to be light up with an oil lamp")

    if "water" not in gameState["player"]["inventory"].keys():
        if obj == "a fountain":
            setGameLost("The vase should not be broken, you need to carry water.")

    getCurrentRoom()["objects"].pop(obj)
    print("You have broken {}, it will be no longer available.".format(obj))


def dropObject(obj):
    # both need to be dropped
    if obj == "water" or obj == "a vase":
        if "water" in gameState["player"]["inventory"].keys():
            getCurrentRoom()["objects"]["water"] = gameState["player"]["inventory"].pop("water")
        if "a vase" in gameState["player"]["inventory"].keys():
            getCurrentRoom()["objects"]["a vase"] = gameState["player"]["inventory"].pop("a vase")
    else:
        getCurrentRoom()["objects"][obj] = gameState["player"]["inventory"].pop(obj)

    print("{} has been dropped in {}.".format(obj, gameState["player"]["location"]))


def giveObject(obj, receiver):
    # Give an ax to a majordomo makes you loose reason: he will kill you to protect the treasure
    # Give a wine bottle to a majordomo makes him talk and open accesses
    # "the red room": {"dir": "North", "next-room": "the hidden room", "door": None}
    if obj == "an ax":
        setGameLost("You should've not trust on {} and give him {}. He has killed you.".format(receiver, obj))
    else:
        dropObject(obj)
        gameState["rooms"]["the red room"]["accesses"].append(
            {"dir": "North", "next-room": "the hidden room", "door": None}
        )
        print("{} says: Thanks a lot for giving me {}. I'll help you find what you came for.".format(receiver, obj))
        print("Go find the red room and you will find in there a clue of what you're looking for.")
        print("The light be with you.")


def killObject(obj):
    # Kill "a majordomo" makes you loose reason: He talks giving you clues
    if obj == "a majordomo":
        setGameLost("{} has important clues to find the treasure. He shouldn't have been killed.")

    # Kill "a fire" needs water in the inventory
    if obj == "a fire" and "water" not in gameState["player"]["inventory"].keys():
        print("The fire could not be extinguished, you need water do so")
    else:
        getCurrentRoom()["objects"].pop(obj)
        print("{} has been killed/extinguished successfully, do <help> or <look>".format(obj))


def unlockObject(obj):
    # To unlock "an iron chest" you need "a stone key" in the inventory
    if obj == "an iron chest":
        if "an stone key" in gameState["player"]["inventory"].keys():
            getCurrentRoom()["objects"]["an iron chest"]["locked"] = False
            print("{} has been successfully unlocked, do <help> for more options.".format(obj))
        else:
            print("{} could not be unlocked, you need a key to do so".format(obj))
    else:
        print("There is no way to unlock {}, find another way out.".format(obj))


print("\nWelcome to the text adventure game The Oblemur's Mansion.\n")

gameState["player"]["name"] = input("\nBy what name shalt thou be called?\n> ")
print("Be welcome {}\n".format(gameState["player"]["name"]))


print("\n")
print("- The goal is to find a treasure and take it out of the Mansion.")
print("- Command are shown in <>s but are used with out them. Ex. <help> will be written as: > help")
print("- Any time you get lost or don't know what to do find clues with the <help> command.")
print("- Also you can do <help command>, it tells you what <command> does")
print("- Enjoy and good look. The light be with you.")
print("\n")

while not gameState["status"]["isWon"] and not gameState["status"]["isLost"]:

    print()
    displayPlayerAndLocation()
    generateRoomOnlyCmds()
    generateInventoryCmds()

    cmd = input("> ").strip()

    # HELP COMMAND
    if "help" == cmd[:4]:
        # just help
        if len(cmd) == 4:
            displayPlayerAndLocation()
            displayFlatCmdList("fixed-glb-cmds")
            displayFlatCmdList("room-only-cmds")
            displayFlatCmdList("inventory-cmds")
        # asking help for a command
        elif cmd[:5] == "help ":
            subCmd = cmd[5:].strip()
            if subCmd in availableCommands["fixed-glb-cmds"].keys():
                print("<{}>: {}".format(subCmd, availableCommands["fixed-glb-cmds"][subCmd]))
            elif subCmd in availableCommands["room-only-cmds"].keys():
                print("<{}>: {}".format(subCmd, availableCommands["room-only-cmds"][subCmd]))
            elif subCmd in availableCommands["inventory-cmds"].keys():
                print("<{}>: {}".format(subCmd, availableCommands["inventory-cmds"][subCmd]))
            else:
                print("Your instruction hasn't been recognized, please try <help> or something else.")
        else:
            print("Your instruction hasn't been recognized, please try <help> or something else.")
        continue

    # INVENTORY AND LOOK COMMANDS
    if cmd in availableCommands["fixed-glb-cmds"].keys():

        # <help> is done earlier
        if "inventory" == cmd:
            displayInventory()
        if "look" == cmd:
            displayLook()

    elif cmd in availableCommands["room-only-cmds"].keys():

        # No validation is necessary due to commands are pre-generated

        if len(cmd) > 2 and "go " == cmd[:3]:
            goDir(cmd[3:].strip())

        if len(cmd) > 4 and "grab " == cmd[:5]:
            grabObject(cmd[5:].strip())

        if len(cmd) > 4 and "open " == cmd[:5]:
            openObject(cmd[5:].strip())

        if len(cmd) > 7 and "talk-to " == cmd[:8]:
            talkTo(cmd[8:].strip())

    elif cmd in availableCommands["inventory-cmds"].keys():

        # No validation is necessary due to commands are pre-generated

        if len(cmd) > 5 and "break " == cmd[:6]:
            breakObject(cmd[6:].strip())

        if len(cmd) > 4 and "drop " == cmd[:5]:
            dropObject(cmd[5:].strip())

        if len(cmd) > 4 and "give " == cmd[:5]:
            giveObject(cmd[5:cmd.index("to")].strip(), cmd[cmd.index("to") + 2:].strip())

        if len(cmd) > 4 and "kill " == cmd[:5]:
            killObject(cmd[5:].strip())

        if len(cmd) > 6 and "unlock " == cmd[:7]:
            unlockObject(cmd[7:].strip())

        if len(cmd) > 4 and "open " == cmd[:5]:
            openObject(cmd[5:].strip())

    else:
        print("Your instruction hasn't been recognized or couldn't be executed, please try <help> or something else.")


if gameState["status"]["isWon"]:
    print("Congratulations you Won")
    print(gameState["status"]["reason"])


if gameState["status"]["isLost"]:
    print("Sorry, you have lost.")
    print(gameState["status"]["reason"])
