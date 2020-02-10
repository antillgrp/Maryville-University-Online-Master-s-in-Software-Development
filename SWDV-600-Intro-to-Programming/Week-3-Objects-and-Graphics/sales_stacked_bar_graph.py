import graphics as g

TEXT_HEIGHT = 50
GRAPH_HEIGHT = 50

HORIZONTAL_MARGIN = 20
GRAPH_WIDTH = 3 * 128

BAR_INSET = 5

WINDOW_HEIGHT = GRAPH_HEIGHT + 2 * TEXT_HEIGHT

win = g.GraphWin("Sales Bar Grapher",
                 GRAPH_WIDTH + 2 * HORIZONTAL_MARGIN,
                 WINDOW_HEIGHT)

labelPoint = g.Point( 50, TEXT_HEIGHT / 2)
entryPoint = labelPoint.clone()
entryPoint.move( 75, 0 )

salesEntryLabel = g.Text( labelPoint, "Enter Sales:")
salesEntryLabel.draw( win )

salesEntry = g.Entry( entryPoint, 5 )
salesEntry.draw( win )

topAxisPoint = g.Point( HORIZONTAL_MARGIN, TEXT_HEIGHT )
bottomAxisPoint = g.Point( HORIZONTAL_MARGIN, WINDOW_HEIGHT - TEXT_HEIGHT )

axisLine = g.Line( topAxisPoint, bottomAxisPoint)
axisLine.draw( win )

totalSales = 0
for dayOfSales in range( 3 ):
    win.getMouse()
    nextSales = int(salesEntry.getText())
    
    topLeftRectPoint = topAxisPoint.clone()
    topLeftRectPoint.move( totalSales, BAR_INSET )

    bottomRightRectPoint = bottomAxisPoint.clone()
    bottomRightRectPoint.move( totalSales + nextSales, -BAR_INSET )

    salesRect = g.Rectangle( topLeftRectPoint, bottomRightRectPoint )
    salesRect.draw( win )

    salesTextPoint = topAxisPoint.clone()
    salesTextPoint.move( totalSales + nextSales / 2, GRAPH_HEIGHT / 2) 
    salesAmountText = g.Text( salesTextPoint, str( nextSales ))
    salesAmountText.draw( win )

    totalSales = totalSales + nextSales
    salesEntry.setText("")

totalTextPoint = g.Point( 50, WINDOW_HEIGHT - TEXT_HEIGHT / 2 )
totalText = g.Text( totalTextPoint, "Total: " + str( totalSales ))
totalText.draw( win )

averageTextPoint = totalTextPoint.clone()
averageTextPoint.move( 175, 0 )
averageText = g.Text( averageTextPoint, "Average: " + str( totalSales / 3 ))
averageText.draw( win )

