# https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/

from functools import reduce

with open('17-oct-sales.txt', 'r') as inputFile:

    listFromMap = lambda *args: list(map(*args))

    writerLines = listFromMap(
        lambda floatSeq: listFromMap(lambda _float: "${:8.2f}".format(_float), floatSeq),
        listFromMap(
            lambda floatSeq: floatSeq + [reduce(lambda a, b: a + b, floatSeq)],
            listFromMap(
                lambda dollarSeq: listFromMap(lambda dollar: float(dollar[1:]), dollarSeq),
                listFromMap(
                    lambda row: row[:-1].split(' '),
                    inputFile.readlines()
                )
            )
        )
    )

    # comprehensive
    # writerLines = inputFile.readlines()
    # writerLines = listFromMap(lambda row: row.split('\n')[0].split(' '), writerLines)
    # writerLines = listFromMap(lambda dollarSeq: listFromMap(lambda dollar: float(dollar.split('$')[1]), dollarSeq), writerLines)
    # writerLines = listFromMap(lambda floatSeq: floatSeq + [reduce(lambda a, b: a + b, floatSeq)], writerLines)
    # writerLines = listFromMap(lambda floatSeq: listFromMap(lambda _float: "${:8.2f}".format(_float), floatSeq), writerLines)

    with open('17-oct-totals.txt', 'w') as outputFile:
        for strSeq in writerLines:
            outputFile.write('  '.join(strSeq) + '\n')
            print('  '.join(strSeq))
