import json


class InventoryItem:
    def __init__(self, itemName):
        self.name = itemName
        self.totalStocked = 0
        self.totalInStock = 0
        self.totalSlots = 0
        self.__price = float('nan')

    def setPriceIfIsNotSetYet(self, price):
        # set it just once
        if str(self.__price) == 'nan':
            self.__price = float(price)

    def getPrice(self):
        return self.__price

    def getTotalSales(self):
        return self.getNumberSold() * self.getPrice()

    def addToStocked(self, stockAmt):
        self.totalStocked = self.totalStocked + stockAmt

    def addToInStock(self, inStockAmt):
        self.totalInStock = self.totalInStock + inStockAmt

    def incrementSlots(self):
        self.totalSlots = self.totalSlots + 1

    def getNumberSold(self):
        return self.totalStocked - self.totalInStock

    def getSoldPct(self):
        return self.getNumberSold() / self.totalStocked

    def getStockNeed(self):
        return 8 * self.totalSlots - self.totalInStock

    def getName(self):
        return self.name

    def getNumberInStock(self):
        return self.totalInStock

    def __repr__(self):
        return '{} In Stock: {}, Stocked: {}, Slots: {}'.format(self.name, self.totalInStock, self.totalStocked,
                                                                self.totalSlots)


class MachineStatus:

    def __init__(self, inventoryFileName):
        self.__machineLabel = inventoryFileName[:7]
        self.__itemNameToItemDict = {}
        with open(inventoryFileName, 'r') as inventoryFile:
            inventory = json.loads(inventoryFile.read())['contents']
            for row in inventory:
                for slot in row['slots']:
                    itemName = slot['item_name']
                    inventoryItem = self.__itemNameToItemDict.get(itemName, InventoryItem(itemName))
                    inventoryItem.addToStocked(slot['last_stock'])
                    inventoryItem.addToStocked(slot['current_stock'])
                    inventoryItem.setPriceIfIsNotSetYet(slot['item_price'])
                    self.__itemNameToItemDict[itemName] = inventoryItem

    def __repr__(self):
        maxPossibleSalesTotal = 0  # Sum item[i].LastStock * item[i].price
        currentSalesTotal = 0  # Sum item[i].numberSold * item[i].price
        for inventoryItem in list(self.__itemNameToItemDict.values()):
            currentSalesTotal += inventoryItem.getNumberSold() * inventoryItem.getPrice()
            maxPossibleSalesTotal += currentSalesTotal + inventoryItem.getNumberInStock() * inventoryItem.getPrice()

        return '{:20} {:8.2f}%       ${:.2f}'.format(
            self.__machineLabel,
            (currentSalesTotal / maxPossibleSalesTotal) * 100,
            currentSalesTotal
        )


def main():
    inventoryFileNames = ["REID_1F_20171004.json", "REID_2F_20171004.json", "REID_3F_20171004.json"]

    prompt = ""
    while prompt != "m" and prompt != "i":
        prompt = input("Would you like the (m)achine report or the (i)nventory report? ")
        if prompt == "m":
            print('Label                   Pct_Sold     Sales_Total')
            for inventoryFileName in inventoryFileNames:
                print(MachineStatus(inventoryFileName))
            prompt = ""
            print()

    itemNameToInventoryItem = {}

    for inventoryFileName in inventoryFileNames:
        inventoryFile = open(inventoryFileName, 'r')

        inventoryData = json.loads(inventoryFile.read())

        contents = inventoryData['contents']
        for row in contents:
            for slot in row['slots']:
                itemName = slot['item_name']
                inventoryItem = itemNameToInventoryItem.get(itemName, InventoryItem(itemName))

                inventoryItem.addToStocked(slot['last_stock'])
                inventoryItem.addToInStock(slot['current_stock'])
                inventoryItem.incrementSlots()

                itemNameToInventoryItem[itemName] = inventoryItem

    sortChoice = ''
    inventoryItemsList = list(itemNameToInventoryItem.values())
    while sortChoice != 'q':
        sortChoice = input('Sort by (n)ame, (p)ct sold, (s)tocking need, or (q) to quit: ')
        if sortChoice == 'n':
            inventoryItemsList.sort(key=InventoryItem.getName)
        elif sortChoice == 'p':
            inventoryItemsList.sort(key=InventoryItem.getSoldPct)
            inventoryItemsList.reverse()
        elif sortChoice == 's':
            inventoryItemsList.sort(key=InventoryItem.getStockNeed)
            inventoryItemsList.reverse()

        print('Item Name            Sold     % Sold     In Stock Stock needs')
        for item in inventoryItemsList:
            print('{:20} {:8} {:8.2f}% {:8} {:8}'.format(item.getName(), item.getNumberSold(), item.getSoldPct() * 100,
                                                         item.getNumberInStock(), item.getStockNeed()))
        print()


main()
