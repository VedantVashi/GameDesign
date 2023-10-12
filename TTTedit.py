
"""
Author: Vedant Vashi
Last edited: 2-2-2022
Purpose: This program creates a Tic Tac Toe program that allows the user to input in the square a X on first click and
O on the second click.
"""

from graphics import *


###FUNCTIONS###

def drawGrid(width, height, r, c, window):
    xcoor = 0
    # draw horizontal lines in grid
    for y in range(1, r * 2):
        ycoor = y * (height // r)  # Moves the lines down
        pt1 = Point(xcoor, ycoor)
        pt2 = Point(width, ycoor)
        line = Line(pt1, pt2)
        line.draw(window)
    # draw vertical lines in grid

    ycoor = 0
    for x in range(1, r * 2):
        xcoor = x * (width // c)  # Moves the Lines right
        pt1 = Point(xcoor, ycoor)
        pt2 = Point(xcoor, height)
        line = Line(pt1, pt2)
        line.draw(window)


def findRow(height, r, pt):
    deltaY = height // r
    rowNum = 1
    while rowNum <= r:
        MaxY = rowNum * deltaY
        ptY = pt.getY()
        if ptY > MaxY:
            rowNum += 1
        else:
            break
    return rowNum


def findCol(width, c, pt):
    deltaX = width // c
    colNum = 1
    while colNum <= c:
        MaxX = colNum * deltaX  # Moves it right if the point is not in the parameter
        ptX = pt.getX()
        if ptX > MaxX:
            colNum += 1  # Increases the column # if the point is not in the column.
        else:
            break
    return colNum


def createX(side, c, r, window, rownum, colnum):  # Creates X wiith a center at the center of a given square.

    maxYCoor = round(rownum * side // r) - 20
    minYCoor = round((rownum - 1) * side // r) + 20
    maxXCoor = round(colnum * side // c) - 20
    minXCoor = round((colnum - 1) * side // c) + 20

    line1 = Line(Point(maxXCoor, maxYCoor), Point(minXCoor, minYCoor))
    line1.setWidth(20)
    line1.setOutline('red')
    line1.draw(window)
    line2 = Line(Point(maxXCoor, minYCoor), Point(minXCoor, maxYCoor))
    line2.setWidth(20)
    line2.setOutline('red')
    line2.draw(window)


def createO(side, c, r, window, rownum,
            colnum):  # creates an O based on a preset size and location based on the Row and colnum
    centerX = round((colnum - .5) * side // c)
    centerY = round((rownum - .5) * side // r)
    centerPoint = Point(centerX, centerY)
    cir = Circle(centerPoint, (((side // c) - 30)) / 2)
    cir.setWidth(20)
    cir.setOutline('blue')
    cir.draw(window)


def checkBoardForWin(board, player):
    # player is either FILLED_X or FILLED_0
    # returns True if a winner, or False if not
    if checkRowsForWin(board, player) or checkColsForWin(board, player) or checkDiagsForWin(board, player):
        result = True
    else:
        result = False
    return result


def checkRowsForWin(board, player):
    # player is either FILLED_X or FILLED_0
    # returns True if a winner along a row, or False if not
    booleans = [0, 0, 0]
    result = False
    for i in range(len(board)):
        row = board[i]
        for j in range(len(row)):
            if row[j] == player:
                booleans[i] = True
            else:
                booleans[i] = False
                break

    if True in booleans:
        result = True
    else:
        result = False

    return result


def checkColsForWin(board, player):
    # player is either FILLED_X or FILLED_0
    # returns True if a winner along a col, or False if not
    booleans = [0, 0, 0]
    for j in range(len(board)):  # this will stay constant till the whole col is check j is the col num
        for i in range(len(board)):  # i is the row num where it will check the same col j
            row = board[i]
            if row[j] == player:
                booleans[j] = True
            else:
                booleans[j] = False
                break
    if True in booleans:
        result = True
    else:
        result = False

    return result


def checkDiagsForWin(board, player):
    # player is either FILLED_X or FILLED_0
    # returns True if a winner along a diag, or False if not
    booleans = [0, 0]
    # top Left to bottom right corner
    for i in range(len(board)):
        if board[i][i] == player:
            booleans[0] = True
        else:
            booleans[0] = False
            break
    # bottom left to top right
    for i in range(len(board)):
        if board[i][-(i + 1)] == player:
            booleans[1] = True
        else:
            booleans[1] = False
            break
    if True in booleans:
        result = True
    else:
        result = False
    return result

def Button(width, height, window, name):

    rectangle = Rectangle(Point((width/10), (height / 10)), Point((width /5), (height /5)))

    Truth = False
    rectangle.setFill("white")
    rectangle.draw(window)
    text = Text(Point((width / 6.66), (width / 6.66)), name)
    text.draw(window)

    clickPoint = window.getMouse()
    ul = rectangle.getP1()  # assume p1 is ll (lower left)
    lr = rectangle.getP2()  # assume p2 is ur (upper right)

    if lr.getX() > clickPoint.getX() > ul.getX() and lr.getY() > clickPoint.getY() > ul.getY():  # sees if button is within the rectangle
        Truth = True
    else:
        Truth = False

    text.undraw()
    rectangle.undraw()
    return Truth

def game():
    truth = True
    while truth is True:
        BLANK = 0
        FILLED_X = 1
        FILLED_O = 2

        r = 3
        c = 3
        board = [[BLANK, BLANK, BLANK], [BLANK, BLANK, BLANK], [BLANK, BLANK, BLANK]]
        side = 600
        window = GraphWin("Tic Tac Toe", side, side)
        img = Image( Point(side/2, side/2), "Background.gif") # sets an image for the Background.
        img.draw(window)
        drawGrid(side, side, r, c, window)
        array = []
        while True:
            rownums = []
            colnums = []  # empty lists to be appended

            while True:
                pt = window.getMouse()
                rownum = findRow(side, r, pt)
                colnum = findCol(side, c, pt)
                colnums.append(colnum)  # appends the column numbers to a list
                rownums.append(rownum)  # appends the row numbers to the list
                if len(colnums) % 2 != 0 and board[rownum - 1][colnum - 1] == BLANK:  # if the length of the list is odd it means there needs to be a X
                    createX(side, c, r, window, rownum, colnum) # creates X in the column and row the user clicks in.
                    board[rownum - 1][colnum - 1] = FILLED_X # replaces a Blank for an X player to a 2d array to determine who is the winner.
                    array.append(FILLED_X) # adds the X player to a 1d array to serve as counter
                elif len(colnums) % 2 == 0 and board[rownum - 1][colnum - 1] == BLANK: # if the length of the list is odd it means there needs to be a X
                    createO(side, c, r, window, rownum, colnum) # creates O in the column and row the user clicks in.
                    board[rownum - 1][colnum - 1] = FILLED_O   # replaces a blank for  O player to a 2d array to determine who is the winner.
                    array.append(FILLED_O) # adds the O player to a 1d array to serve as counter
                else:
                    colnums = colnums[0:len(colnums)-1] # if the column is already occupied then the points information is deleted from the list.
                    rownums = rownums[0:len(rownums) - 1]
                isXWinner = checkBoardForWin(board, FILLED_X) # checks if X the winner
                isOWinner = checkBoardForWin(board, FILLED_O) #Checks if O is the winner

                if isXWinner is True: # If X wins it congratulates the player and ends the game.
                    text = "Congratulations, X you are a winner!"
                    label = Text(Point(side/2,side/2), text)
                    label.setSize(20)
                    label.setTextColor("green")
                    label.draw(window)

                    break
                elif isOWinner is True: # If O wins it congratulates the player and ends the game.
                    text = "Congratulations, O you are a winner!"
                    label = Text(Point(side/2, side/2), text)
                    label.setSize(20)
                    label.setTextColor("green")
                    label.draw(window)
                    break
                elif len(array) == 9: # if all the squares are filled and there is no winner it declares a tie.
                    text = "Tied"
                    label = Text(Point(side / 2, side / 2), text)
                    label.setSize(20)
                    label.setTextColor("green")
                    label.draw(window)
                    break

            restart = Button(side, side, window, "Restart") # once the game ends this single use button appears to ask the user if they want to play the game again. it desappears after user clicks it or on the board.
            if restart is True:
                window.close() #
                break
                # this ends the secondary nested loops while continuing the main loop
            else: # if the user doesn't  want then this gives them the option to close the window.
                quit = Button(side, side, window, "Close")
                if quit is True:
                    window.close()
                    truth = False # this terminates the main loop.
                    break
            window.wait_window()
            break

####################
game()
