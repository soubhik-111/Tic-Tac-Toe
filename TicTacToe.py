def printboard():
    print(f"{str(boardList[0])} | {str(boardList[1])} | {str(boardList[2])}")
    print("---------")
    print(f"{str(boardList[3])} | {str(boardList[4])} | {str(boardList[5])}")
    print("---------")
    print(f"{str(boardList[6])} | {str(boardList[7])} | {str(boardList[8])}")
    

boardList = [0,1,2,3,4,5,6,7,8]
def win(e):
    # Horizontal
    if(boardList[0]==e and boardList[1]==e and boardList[2]==e):
        return 1
    elif(boardList[3]==e and boardList[4]==e and boardList[5]==e):
        return 1
    elif(boardList[6]==e and boardList[7]==e and boardList[8]==e):
        return 1
    # Vertical
    elif(boardList[0]==e and boardList[3]==e and boardList[6]==e):
        return 1
    elif(boardList[1]==e and boardList[4]==e and boardList[7]==e):
        return 1
    elif(boardList[2]==e and boardList[5]==e and boardList[8]==e):
        return 1
    # Diagonally
    elif(boardList[0]==e and boardList[4]==e and boardList[8]==e):
        return 1
    elif(boardList[2]==e and boardList[4]==e and boardList[6]==e):
        return 1
    return -1

for i in range(9):
    printboard()
    if (not (i % 2)):
        xValue = int(input("Enter the slot number (X's Chance) :- "))
        boardList[xValue] = 'X'
    else:
        oValue = int(input("Enter the slot number (O's Chance) :- "))
        boardList[oValue] = 'O'
    print("\n")
    if(i>=5):
        xWinValue = win('X')
        oWinValue = win('Y')
        if(xWinValue==1):
            printboard()
            text = "Congrations 'X' has won the match"
            print(text.center(100))
            break
        if(oWinValue==1):
            printboard()
            text = "Congrations 'Y' has won the match"
            print(text.center(100))
            break
