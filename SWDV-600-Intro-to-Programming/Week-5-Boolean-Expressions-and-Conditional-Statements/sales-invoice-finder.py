with open('sales_data.csv', 'r') as csvFile:
    searchCol = ""
    while True:
        searchCol = input("Search by invoice id (id) or customer last name (lname)? ")
        if searchCol == "id" or searchCol == "lname":
            break
        else:
            print("ERROR: You must enter either 'id' for invoice id search or 'lname' for customer last name search")
    searchTerm = input("Enter your search term: ")
    csvLine = csvFile.readline()  # header
    csvLine = csvFile.readline()  # first
    records = 0
    while csvLine != "":
        row = csvLine.split(",")
        if (searchCol == "id" and searchTerm == row[0]) or (searchCol == "lname" and searchTerm == row[2]):
            print(csvLine, end="")
            records += 1
        csvLine = csvFile.readline()
    print(records, " records found")
