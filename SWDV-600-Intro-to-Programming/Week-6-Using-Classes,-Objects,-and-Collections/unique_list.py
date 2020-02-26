class ListUniqueClassifier:

    def __init__(self):
        self.list = []

    def isUnique(self):
        # set --> Builds an unordered collection of unique elements.
        return len(set(self.list)) == len(self.list)


if __name__ == '__main__':
    listUniqueClassifier = ListUniqueClassifier()
    print("This program tests if the sequence of positive numbers you input are unique\nEnter -1 to quit")
    nextInt = int(input("First: "))
    while nextInt >= 0:
        listUniqueClassifier.list.append(nextInt)
        nextInt = int(input("Next: "))
    print("The sequence {} is {}".format(listUniqueClassifier.list, "unique!" if listUniqueClassifier.isUnique() else "NOT unique!"))

