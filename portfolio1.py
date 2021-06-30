import random
import os
import time
from random import randint

#Game 1
#Game of rock paper scissors in the terminal
#By Marlon C.

def rocks_game():
    computerChoice = ""

    dod = random.randint(1, 4)
    your_score = 0
    computer_score = 0

    if dod == 1:
        computerChoice = "rock"
    elif dod == 2:
        computerChoice = "paper"
    elif dod == 3:
        computerChoice = "scissors"
        

    while your_score != 10 or computer_score != 10:
        userInput = str(input("Please enter your choise (Type Stop to stop the game): "))
        
        if userInput == computerChoice:
            print("This game is a tie.")
            print(f"You chose {userInput}")
            print(f"The computer chose {computerChoice}")
        elif userInput == "rock" and computerChoice == "paper":
            print("The computer won.")
            computer_score += 1
            print(f"You chose {userInput}")
            print(f"The computer chose {computerChoice}")
        elif userInput == "paper" and computerChoice == "rock":
            print("You won")
            your_score += 1
            print(f"You chose {userInput}")
            print(f"The computer chose {computerChoice}")
        elif userInput == "paper" and computerChoice == "scissors":
            print("The computer won.")
            computer_score += 1
            print(f"You chose {userInput}")
            print(f"The computer chose {computerChoice}")
        elif userInput == "scissors" and computerChoice == "paper":
            print("You won")
            your_score += 1
            print(f"You chose {userInput}")
            print(f"The computer chose {computerChoice}")
        elif userInput == "scissors" and computerChoice == "rock":
            print("The computer won.")
            computer_score += 1
            print(f"You chose {userInput}")
            print(f"The computer chose {computerChoice}")
        elif userInput == "rock" and computerChoice == "scissors":
            print("You won")
            your_score += 1
            print(f"You chose {userInput}")
            print(f"The computer chose {computerChoice}")
        elif userInput == "Stop":
            break
            
        print(f"You have : {your_score} points.")
        print(f"The computer has {computer_score} points.")
        input("Press a key to continue")
        
        os.system('clear')

#Game 2
#Game of Connect4 in the terminal
#By Marlon C.

def Connect4():
    board = [] 
    label = []
    whos_turn = 0b10
    winner = False
    last = 0
    column = 0
    boardheight = 6
    boardwidth = 7

    #generate empty board
    def generate_board(boardheight, boardwidth):
        for i in range(8):
            if i < boardheight:
                board.append(["_"] * boardwidth)
            elif i < boardwidth:
                board.append(["^"] * boardwidth)
            else:
                for j in range(boardwidth):
                    label.append(str(j+1))
                board.append(label)

    def start():
        print ("Let's play Connect Four!")
        start_seq = ["3",".",".","2",".",".","1",".","."]
        for i in start_seq:
            time.sleep(0.333)
            print(i)

    def print_board(board):
        print("\n")
        for row in board:
            print(" ".join(row))
        print("\n")
            
    def toggle(turn):
        mask = 0b11
        turn = turn ^ mask
        print("It is player %s's turn." % turn)
        return turn

    def mark_board(last, column):
        if whos_turn == 0b01:
            board[last][column] = "1"
        else:
            board[last][column] = "2"
        print_board(board)

    def play():
        while True:
            try:
                column = int(input("Pick a column (1-7): ")) - 1
                if column >= 1 and column <= boardwidth:
                    for i in range(6):
                        if board[i][column] == "_":
                            last = i
                    mark_board(last, column)
                else:
                    raise "You picked a column outside the board!"
                break
            except:
                print("Not a valid number! Please try again...")

    def check_winner(board, player):
        #check horizontal spaces
        for y in range(boardheight):
            for x in range(boardwidth - 3):
                if board[x][y] == player and board[x+1][y] == player and board[x+2][y] == player and board[x+3][y] == player:
                    return True

        #check vertical spaces
        for x in range(boardwidth):
            for y in range(boardheight - 3):
                if board[x][y] == player and board[x][y+1] == player and board[x][y+2] == player and board[x][y+3] == player:
                    return True

        #check / diagonal spaces
        for x in range(boardwidth - 3):
            for y in range(3, boardheight):
                if board[x][y] == player and board[x+1][y-1] == player and board[x+2][y-2] == player and board[x+3][y-3] == player:
                    return True

        #check \ diagonal spaces
        for x in range(boardwidth - 3):
            for y in range(boardheight - 3):
                if board[x][y] == player and board[x+1][y+1] == player and board[x+2][y+2] == player and board[x+3][y+3] == player:
                    return True

        return False
        
    start()
    generate_board(boardheight, boardwidth)
    print_board(board)

    while winner == False:
        whos_turn = toggle(whos_turn)
        play()
        winner = check_winner(board, str(whos_turn))
        
    if winner == True:
        print("Player " + str(whos_turn) + " wins!")



#Game 3
#This is a Tic-Tac-Toe game for the terminal
#You play against an ai
#Marlon C.

def TicTacToe():
    square = []
    square = [" " for x in range(10)] 
    pos = 0
    isUserTurn = True
    positions = [1,2,3,4,5,6,7,8,9] #this is gloal because we need the list to be updated throughout the game, and not reset everytime PCTurn is called

    #functions
    def DrawBoard():
        #Draws the game bard on the terminal
        print(' ',square[7],'  |  ',square[8],'  |  ',square[9],' ')
        print("------|-------|------")
        print(' ',square[4],'  |  ',square[5],'  |  ' ,square[6],' ')
        print("------|-------|------")
        print(' ',square[1],'  |  ',square[2],'  |  ' ,square[3],' ')

    def UpdateBoard(typeChar,pos):
        #Updates the game board with new moves

        #print("UpdateBoard pointers contain: typeChar: ", typeChar, "pos: ", pos)#DEBUGGING LINE
        square[int(pos)] = typeChar
        DrawBoard()

    def UserInput():
        #Takes the users input and only accepts input between 1 and 9 and it has to be an integer
        pos=0
        while True:
            try:
                while not int(pos) in range(1,10):
                    pos = int(input("Enter a position value 1-9: "))      
            except ValueError:
                print("Not an integer between 1-9. Try again.")
                continue
            else:
                return pos
                break 
        #chara = chara.upper()
        
        #print("Charachter: ", chara)
        #print("Columns number: ", pos) 
        #print() 
        return pos

    def CheckTurn(UserTurn):
        #Will toggle between whos turn it is each time this is called. The main difference between this function and
        #XOTOGGLE is that ChekTurn deals with the boolean values and not the actual team characters 'X' and 'O' them selves.
        #Do not call this unless you mean to switch the teams. There are other ways to0 find out what team's turn it is without calling this.
        if UserTurn == True:
            UserTurn = False
        else:
            UserTurn = True
        return UserTurn
        
    def XOToggle():
        #Everytime this is called the game switches teams  and returns which teams turn it is. Do not call this unless
        # you mean to switch the teams. There are other ways to0 find out what team's turn it is without calling this.
        #Same thing with CheckTurn.
        if isUserTurn == True:
            return "X"
        else:
            return "O"

    def isBoardFull():
        #Checks if board is full
        #print("Square Count: " ,square.count(" "))#DEBUGGING LINE
        if square.count(" ") <= 1:
            return True
        return False
    def IsBoardEmpoty():
        #Checks if board is empty
        if square.count(" ")>= 9:
            return True
        return False
        
    def WinningSequences():
        winner = ""
        gameInSession = True
        #diagonal wins for team X 
        if square[1] == 'X' and square[5] == 'X' and square[9] == 'X': winner = "X"
        elif square[3] == 'X' and square[5] == 'X' and square[7] == 'X': winner = "X"
        #Stright Horizontal Win for Team X
        elif square[1] == 'X' and square[2] == 'X' and square[3] == 'X': winner = "X"
        elif square[4] == 'X' and square[5] == 'X' and square[6] == 'X': winner = "X"
        elif square[7] == 'X' and square[8] == 'X' and square[9] == 'X': winner = "X"
        #Straight Win Verticle for Tem X
        elif square[1] == 'X' and square[4] == 'X' and square[7] == 'X': winner = "X"
        elif square[2] == 'X' and square[5] == 'X' and square[8] == 'X': winner = "X"
        elif square[3] == 'X' and square[6] == 'X' and square[9] == 'X': winner = "X"
        #Team O Victory
        elif square[1] == 'O' and square[5] == 'O' and square[9] == 'O': winner = "O"
        elif square[3] == 'O' and square[5] == 'O' and square[7] == 'O': winner = "O"
        #Stright Horizontal Win for Team X
        elif square[1] == 'O' and square[2] == 'O' and square[3] == 'O': winner = "O"
        elif square[4] == 'O' and square[5] == 'O' and square[6] == 'O': winner = "O"
        elif square[7] == 'O' and square[8] == 'O' and square[9] == 'O': winner = "O"
        #Straight Win Verticle for Tem X
        elif square[1] == 'O' and square[4] == 'O' and square[7] == 'O': winner = "O"
        elif square[2] == 'O' and square[5] == 'O' and square[8] == 'O': winner = "O"
        elif square[3] == 'O' and square[6] == 'O' and square[9] == 'O': winner = "O"
        #Draw game
        elif isBoardFull() == True:
            print("Draw! Game over")
            gameInSession = False
            return gameInSession
        
        if winner == "O":
            print(" O Wins!!")
            gameInSession = False
            return gameInSession
        elif winner == "X":
            print("X Wins!!")
            gameInSession = False
            return gameInSession
        else:
            gameInSession = True
            return gameInSession
            
    def SqaureIsTaken (chk):
        #checks if the square is taken by either team characters
        location = pos 
        newPos = 0 
        
        if chk == True:
            while square[location] == "X" or square[location] == "O":
                print ("This square was already taken. Please choose a different square.") 
                newPos = UserInput () 
                if square[newPos] == " ":
                    chk = False 
                    break
        return newPos

    def ChooseRandomSquare():
        #Updates the Pc with a new random square becuase no other possible choices where available for a vicotry or defense
        newMove = random.choice(positions)
        positions.remove(newMove)
        # UpdateBoard('O',newMove)#DEBUGGING

        return newMove
    def PCTurn(playerPos):
        positions.remove(playerPos) #takes the players last move and removes it from the list of possible positions
        '''=================================Offensive moves================================================='''
        '''====================== Seek Bottom Row Victory==========================='''
        if (square[1] == 'O' and square[2] == 'O') or (square[9] == 'O' and square[6] == 'O') or (square[7] == 'O' and square[5]=='O'):
            if 3 in positions:
                newMove = 3
                positions.remove(newMove)#every instance in offensive and  deffensive moves we have to update the list by
                # removing the computers choice
                return newMove
            else:
                return ChooseRandomSquare()
        elif (square[1] == 'O' and square[3]=='O') or (square[8] == 'O' and square[5] == 'O'):
            if 2 in positions:
                newMove = 2
                positions.remove(newMove)
                return newMove
            else:
                return ChooseRandomSquare()
        elif (square[2] == 'O' and square[3] == 'O') or (square[4] == 'O' and square[7] == 'O') or (square[5] == 'O' and square[9] == 'O'):
            if 1 in positions:
                newMove = 1
                positions.remove(newMove)
                return  newMove
            else:
                return ChooseRandomSquare()
            '''===================== Seek Mid Row Victories==================================='''
        elif (square[7] == 'O' and square[1] == 'O') or (square[5] == 'O' and square[6]) == 'O':
            if 4 in positions:
                newMove = 4
                positions.remove(newMove)
                return  newMove
            else:
                return ChooseRandomSquare()
        elif ((square[4] == 'O' and square[6] == 'O') or (square[8] == 'O' and square[2] == 'O') or
            (square[9] == 'O' and square[1] == 'O') or (square[7] == 'O' and square[3] == 'O')):
            if 5 in positions:
                newMove = 5
                positions.remove(newMove)
                return newMove
            else:
                return ChooseRandomSquare()
        elif (square[3] == 'O' and square[9] == 'O') or (square[4] == 'O' and square[5] == 'O'):
            if 6 in positions:
                newMove = 6
                positions.remove(newMove)
                return newMove
            else:
                return ChooseRandomSquare()
            '''===========================Seek Top row Victories==================================='''
        elif (square[1] == 'O' and square[4] == 'O') or (square[8] == 'O' and square[9] == 'O') or (
                square[5] == 'O' and square[3] == 'O'):
            if 7 in positions:
                newMove = 7
                positions.remove(newMove)
                return newMove
            else:
                return ChooseRandomSquare()
        elif (square[2] == 'O' and square[5] == 'O') or (square[7] == 'O' and square[9] == 'O'):
            if 8 in positions:
                newMove = 8
                positions.remove(newMove)
                return newMove
            else:
                return ChooseRandomSquare()
        elif (square[3] == 'O' and square[6] == 'O') or (square[7] == 'O' and square[8] == 'O') or (
                square[5] == 'O' and square[1] == 'O'):
            if 9 in positions:
                newMove = 9
                positions.remove(newMove)
                return newMove
            else:
                return ChooseRandomSquare()




            '''=======================================Defensive Moves ==================================='''
            '''====================== Seek Bottom Row defense==========================='''
        elif (square[1] == 'O' and square[2] == 'X') or (square[9] == 'X' and square[6] == 'X') or (
                square[7] == 'X' and square[5] == 'X'):
            if 3 in positions:
                newMove = 3
                positions.remove(newMove)
                return newMove
            else:
                return ChooseRandomSquare()
        elif (square[1] == 'X' and square[3] == 'X') or (square[8] == 'X' and square[5] == 'X'):
            if 2 in positions:
                newMove = 2
                positions.remove(newMove)
                return newMove
            else:
                return ChooseRandomSquare()
        elif (square[2] == 'X' and square[3] == 'X') or (square[4] == 'X' and square[7] == 'X') or (
                square[5] == 'X' and square[9] == 'X'):
            if 1 in positions:
                newMove = 1
                positions.remove(newMove)
                return newMove
            else:
                return ChooseRandomSquare()
            '''===================== Seek Mid Row Defense ==================================='''
        elif (square[7] == 'X' and square[1] == 'X') or (square[5] == 'X' and square[6]) == 'X':
            if 4 in positions:
                newMove = 4
                positions.remove(newMove)
                return newMove
            else:
                return ChooseRandomSquare()
        elif ((square[4] == 'X' and square[6] == 'X') or (square[8] == 'X' and square[2] == 'X') or
            (square[9] == 'X' and square[1] == 'X') or (square[7] == 'X' and square[3] == 'X')):
            if 5 in positions:
                newMove = 5
                positions.remove(newMove)
                return newMove
            else:
                return ChooseRandomSquare()
        elif (square[3] == 'X' and square[9] == 'X') or (square[4] == 'X' and square[5] == 'X'):
            if 6 in positions:
                newMove = 6
                positions.remove(newMove)
                return newMove
            else:
                return ChooseRandomSquare()
            '''===========================Seek Top row Defense ==================================='''
        elif (square[1] == 'X' and square[4] == 'X') or (square[8] == 'X' and square[9] == 'X') or (
                square[5] == 'X' and square[3] == 'X'):
            if 7 in positions:
                newMove = 7
                positions.remove(newMove)
                return newMove
            else:
                return ChooseRandomSquare()
        elif (square[2] == 'X' and square[5] == 'X') or (square[7] == 'X' and square[9] == 'X'):
            if 8 in positions:
                newMove = 8
                positions.remove(newMove)
                return newMove
            else:
                return ChooseRandomSquare()
        elif (square[3] == 'X' and square[6] == 'X') or (square[7] == 'X' and square[8] == 'X') or (
                square[5] == 'X' and square[1] == 'X'):
            if 9 in positions:
                newMove = 9
                positions.remove(newMove)
                return newMove
            else:
                return ChooseRandomSquare()
            '''===========================default move============================================'''
        else:
            return ChooseRandomSquare()


    #main
    '''Init section'''
    DrawBoard()
    pos = 0
    userPos = 0
    #print(WinningSequences())
    while WinningSequences() == True:
        if isUserTurn == True:
            #take user input
            #print("Main section output ",UserInput()) #DEBUGGING LINE
            userPos = UserInput()
            pos = userPos
            #update the game
            #print("Main section output, UserInput returns : ", typeChar, " ", pos) #DEBUGGING LINE
            if square[pos] == "X" or square[pos] == "O":
                pos = SqaureIsTaken(True)

        if isUserTurn == False:
            PCpos = PCTurn(pos)
            pos = PCpos
        #print(pos)#DEBUGLine
        UpdateBoard(XOToggle(),pos)
        WinningSequences()
        isUserTurn = CheckTurn(isUserTurn)
        print(XOToggle(), "'s turn...")
        #print(positions) #DEBBUGGINGLINE


#Game 4
#THis is the black jack
#Terminal version
#Marlon C.

def BlackJack():
    playing = True

    suits = ["Hearts", "Spades", "Diamonds" ,"Clubs"]
    ranks = ["Two" , "Three" ,"Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    values = {"Two": 2 , "Three":3 ,"Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10,
            "Jack":10, "Queen":10, "King":10, "Ace":11}

    # class for creating card
    class Card():
        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank

        def __str__(self):
            return self.rank+" of "+self.suit


    #class for creating deck, shuffling deck and giving random card
    class Deck():
        def __init__(self):
            self.deck = []
            for suit in suits:
                for rank in ranks:
                    self.deck.append(Card(suit, rank))
        def __str__(self):
            cards = " "
            for card in self.deck:
                cards +="\n"+card.__str__()
            return "We have deck as follows:" + cards

        def shuffle(self):
            random.shuffle(self.deck)

        def deal(self):
            return self.deck.pop()


    # for managing cards of dealer and player
    class Hand():
        def __init__(self):
            self.cards = []
            self.value = 0
            self.aces = 0

        def add_card(self, card):
            self.cards.append(card)
            self.value += values[card.rank]
            if card.rank == "Ace":
                self.aces +=1

        def adjust_for_ace(self):
            while self.aces and self.value > 21:
                self.value -= 10
                self.aces -= 1

    # for managing chips of player
    class Chips():
        def __init__(self):
            self.total = 100
            self.bet = 0
        def win_bet(self):
            self.total += self.bet
        def lose_bet(self):
            self.total -= self.bet

    # for takeing bets
    def take_bets(chips):
        while True:
            try:
                chips.bet = int(input("Please enter amount of bet : "))
            except ValueError:
                print("Please enter only integers")
            else:
                if chips.bet > chips.total:
                    print("sorry your bet can't exceed {}".format(chips.total))
                else:
                    break

    # for taking one card from deck
    def hit(deck, hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()

    # for asking player hit or stand
    def hit_or_stand(deck ,hand):

        global playing
        while True:
            i = input("Please enter 'h' for hit and 's' for stand ")

            if i[0].lower() == 'h':
                hit(deck, hand)

            elif i[0].lower() == 's':
                print("player stands. Dealer is playing")
                playing  = False

            else:
                print("Sorry please Try again ")
                print("Enter only 'h' for hit and 's' for stand ")
                continue
            break

    # for showing card's when dealer one card is hidden
    def show_some(player, dealer):
        print("\n\nDealer's Hand : ")
        print("<card hidden>")
        print(dealer.cards[1])
        print("\nPlayer's Hand : ", *player.cards, sep="\n")
        print("\n")

    # for showing card's when dealer card's are not hidden
    def show_all(player, dealer):
        print("\nDealer's Hand : " , *dealer.cards, sep="\n")
        print("     Dealer's Hand = ",dealer.value)
        print("\nPlayer's Hand : " , *player.cards, sep="\n")
        print("     Player's Hand = ",player.value)
        print("\n")

    # all conditions occuring in game of winning, losing and tie are managed by
    # below functions

    def player_bust(chips):
        print("Player Bust")
        chips.lose_bet()

    def player_win(chips):
        print("Player win's")
        chips.win_bet()

    def dealer_bust(chips):
        print("Dealer Bust")
        chips.win_bet()

    def dealer_win(chips):
        print("Dealer Win's")
        chips.lose_bet()

    def push():
        print("Dealer and Player tie! It's a push")

    while True:
        print("\n\n\nWelcome to blackjack ! \n Get as close to 21 as you can without going over.\n\
    Dealer hits until he reaches 17. Aces count as 1 or 11\n")

        # create deck of cards
        deck = Deck()
        # shuffle cards randomly
        deck.shuffle()

        # add 2 card's to player
        player = Hand()
        player.add_card(deck.deal())
        player.add_card(deck.deal())

        # add 2 card's to dealer
        dealer = Hand()
        dealer.add_card(deck.deal())
        dealer.add_card(deck.deal())

        # set chips for player
        player_chips = Chips()

        # take bet from player
        take_bets(player_chips)

        # show cards keeping one dealer card hidden
        show_some(player, dealer)

        while playing:

            # ask player for his move
            hit_or_stand(deck, player)

            # show cards keeping one dealer card hidden
            show_some(player, dealer)

            # if player has more than 21 value then he bust and loses
            if player.value > 21:
                player_bust(player_chips)
                break

        # we will come here if player is bust or he stand . if he stands dealer will play
        # until he reches 17 . we will remove player bust codition from here
        if player.value <= 21:

            while dealer.value < 17:
                hit(deck, dealer)

            show_all(player , dealer)

            # all other cases

            if dealer.value > 21:
                dealer_bust(player_chips)
            elif dealer.value > player.value:
                dealer_win(player_chips)
            elif dealer.value < player.value:
                player_win(player_chips)
            else:
                push()

        print("Player has Total chips : ", player_chips.total)

        i = input("Do you want to play game again 'y' for Yes and 'n' for NO ")

        if i[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thank you for playing")
            break

#Game 5
#THis is BattleShip
#Marlon C.

def BattleShip():
        board = []

        for x in range(6):
            board.append(["O"] * 6)

        def print_board(board):
            for row in board:
                print((" ").join(row))

        print("Let's play Battleship!")
        print_board(board)

        def random_row(board):
            return randint(0, len(board) - 1)
        def random_col(board):
            return randint(0, len(board[0]) - 1)

        ship_row = random_row(board)
        ship_col = random_col(board)

        for turn in range(9):
            print ("Turn"), turn
            guess_row = int(input("Guess Row:"))
            guess_col = int(
                input("Guess Col:"))

            if guess_row == ship_row and guess_col == ship_col:
                print("Congratulations! You sunk my battleship!")
                break
            else:
                if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
                    print("Oops, that's not even in the ocean.")
                elif(board[guess_row][guess_col] == "X"):
                    print("You guessed that one already.")
                else:
                    print("You missed my battleship!")
                    board[guess_row][guess_col] = "X"
            if turn == 8:
                print("Game Over")
            turn =+ 1
            print_board(board)


#Game 6
#The Game is Minesweeper
#The goal of Minesweeper is to uncover all the squares on a grid that do not contain mines without being "blown up"
#Marlon C.

def Mines():

    class Cell:
        def __init__(self, state, hidden, value, x, y):
            self.is_numbered = state #Boolean
            self.is_flag = False
            self.hidden = hidden # Boolean
            self.value = value
            self.x = x
            self.y = y

        def cell_to_string(self):
            if self.hidden:
                return "-"
            else:
                if self.is_flag:
                    return "F"

                if self.is_numbered:
                    return str(self.value)
                else:
                    return "M"

    class Minesweeper:
        def __init__(self, width, height):
            self.width = int(width)
            self.height = int(height)
            self.is_game_over = False
            self.flags = self.width*self.height//16
            self.adjacents = [(-1,-1),(0,-1),(1,-1),
                            (-1,0),			(1,0),
                            (-1,1),(0,1),(1,1)]

            self.board = [[Cell(True, True, 0, x, y) for x in range(width)] for y in range(self.height)]

        def __in_board_range(self, x, y):
            return x >= 0 and x < self.width and y >= 0 and y < self.height


        def __randomize_mines(self, first_x, first_y, mines):
            mines_left = mines

            while(mines_left > 0):
                x = random.choice(range(self.width))
                y = random.choice(range(self.height))

                if x == first_x or y == first_y:
                    # Can't have the first one be a mine
                    continue

                if self.board[x][y].is_numbered:
                    self.board[x][y].is_numbered = False # Now a mine
                    self.board[x][y].value = -1
                    mines_left -= 1
                else:
                    continue


        def __calculate_numbers(self):
            for y in range(self.height):
                for x in range(self.width):
                    if self.board[x][y].is_numbered:
                        # If not a mine, go through adjacents
                        for tuple in self.adjacents:
                            if self.__in_board_range(x + tuple[0],y + tuple[1]):
                                if not self.board[x + tuple[0]][y + tuple[1]].is_numbered:
                                    self.board[x][y].value += 1

        def reveal_cell(self, x, y, first=False):
            if first:
                self.__randomize_mines(x,y,(self.width*self.height)//16)
                self.__calculate_numbers()

            if self.__in_board_range(x,y):
                if not self.board[x][y].hidden:
                    print("---> Coordinate already uncovered, please choose another <---")
                else:
                    if not self.board[x][y].is_numbered:
                        self.is_game_over = True
                        self.board[x][y].hidden = False
                    else:
                        if not self.board[x][y].value > 0:
                            self.__uncover_blanks(x,y)
                        else:
                            self.board[x][y].hidden = False
            else:
                print("---> Please choose a coordinate pair within the board range! <---")

        def place_flag(self, x, y):
            if self.__in_board_range(x,y):
                if self.flags:
                    self.board[x][y].hidden = False
                    self.board[x][y].is_flag = True
                    self.flags -= 1
                else:
                    print("--> NO MORE FLAGS TO AVAILABLE - GOOD LUCK! <---")
            else:
                print("---> Please choose a coordinate pair within the board range! <---")



        def __uncover_blanks(self, x, y):
            if self.board[x][y].hidden:
                self.board[x][y].hidden = False
                for tuple in self.adjacents:
                    dx = tuple[0]
                    dy = tuple[1]
                    if self.__in_board_range(x + dx, y + dy):
                        if self.board[x + dx][y + dy].is_numbered:
                            if self.board[x + dx][y + dy].value == 0:
                                self.__uncover_blanks(x + dx, y + dy)
                            else:
                                self.board[x + dx][y + dy].hidden = False

        def game_over(self):
            return self.is_game_over

        def game_won(self):
            unhidden_cells = self.width * self.height
            for y in range(self.height):
                for x in range(self.width):
                    if not self.board[x][y].hidden:
                        unhidden_cells -= 1

            return unhidden_cells == 0

        def print_board(self):
            print("    " + "  ".join([str(x) for x in range(10)]) + "  " + " ".join([str(x) for x in range(10,self.width,1)]))
            print("    " + " ".join(["--" for x in range(self.width)]))
            for y in range(self.height):
                row_string = "  "
                print("%s | " % (y) + row_string.join([self.board[x][y].cell_to_string() for x in range(self.width)]))

            print("\n ###########################")
            print("Flags Left: %d" % self.flags)

    if __name__ == "__main__":

        print("---> WELCOME TO MINESWEEPER! <---")
        print("---> please choose the width and height of your board (up to 20) <---")
        width = input("width: ")
        height = input("height: ")
        board = Minesweeper(int(width),int(height))

        print("To start, choose an initial coordinate...")
        while True:
            first_x = int(input("first x: "))
            first_y = int(input("first y: "))
            if first_x < 0 or first_x > int(width):
                print("invalid x coordinate")
                continue
            if first_y < 0 or first_y > int(height):
                print("invalid y coordinate")
                continue
            board.reveal_cell(int(first_x),int(first_y),True)
            break

        board.print_board()

        while True:
            print("---> CHOICES <---")
            print("--> reveal")
            print("--> flag")
            print("--> exit")
            choice = input("?: ")

            if choice == "reveal":
                x = input("x: ")
                y = input("y: ")
                board.reveal_cell(int(x),int(y))
            elif choice == "flag":
                flag_x = input("flag_x: ")
                flag_y = input("flag_y: ")
                board.place_flag(int(flag_x),int(flag_y))
            elif choice == "exit":
                print("---> EXITED, GOODBYE! <---")
                break
            else:
                print("Invalid choice...")
                continue
            
            board.print_board()

            if board.game_over():
                print("---> GAME OVER <---")
                break

            if board.game_won():
                print("---> WINNER WINNER! <---")
                print("---> CONGRATULATIONS <---")
                break

#Game 7
#Who wants to be a Millionaire ?
#Marlon C.
def Millionaire():
    print("Welcome To Who Wants to be a Millionaire")
    print ("First Question: In the children's book series, where is Paddington Bear originally from?")
    print ("Choices: ")
    print ("------")
    print ("India")
    print ("Canada")
    print ("Peru")
    print ("Iceland")
    print ("-------")
    def keep_going():
        answer = input("What is your Choice?: ")
        if answer == "Peru":
            print("Right Answer! Good Luck in Next round!")
            print("Second Round!")
            print ("The Question is:What letter must appear at the beginning of the registration number of all non-military aircraft in the U.S.?")
            print ("Choices: ")
            print ("N")
            print ("A")
            print ("U")
            print ("L")
        answer2 = input("What is your Choice?: ")
        if answer2 == "N":
            print ("Right Answer Good luck in the third round!")
            print ("Welcome to the third round , u are fighting for 5000 dollars! please share applause for this guy!")
            print (" Ok , so back to the question")
            print (" The Question is: Who delivered the less famous two-hour speech that preceded Abraham Lincoln's two-minute Gettysburg Address?")
            print (" The Choices are: ")
            print (" Wenndell Phillips")
            print (" Daniel Webster")
            print ("Rober G. Ingersoll")
            print ("Edwart Everett")
        answer3 = input("What is your Choice?: ")
        if answer3 == "Edwart Everett":
            print ("is it right?")
            print ("Yes , it is! You are going to fourth round!")
            print ("Welcome to the Fourth Round")
            print (" You are Fighting for 10000 dollars")
            print (" Lets get right to the question!")
            print (" The question is: Nephelococcygia is the practice of doing what?")
            print (" Here are the choices: ")
            print (" Finding Shapes in clouds")
            print (" Sleeping with your eyes open")
            print (" Breaking glass with your voice")
            print (" Swimming in the Freezing water")
        answer4 = input("What is your Choice?: ")
        if answer4 == "Finding Shapes in clouds":
            print ("Well , it may be but what bout Breaking Glass with your voice?")
            print ("We'll reveal the answer in 5 seconds")
            print ("1")
            print ("2")
            print ("3")
            print ("4")
            print ("5")
            print (" You Got it Right! You got 10000 dollars on your account!")
            print (" Welcome to the Fifth Round!")
            print ("You are Fighting for 100000 dollars! this is the penultimate question!")
            print (" The Question is: Which insect shorted out an early supercomputer and inspired the term computer bug?")
            print (" The Choices are: ")
            print (" Moth ")
            print (" Roach ")
            print (" Fly ")
            print (" Japanese Beetle ")
        answer5 = input("What is your Choice?: ")
        if answer5 == "Moth":
            print ("You are GOING TO THE LAST ROUND TO FIGHT FOR MILLION DOLLARS!!")
            print (" Ladies and Gentlemen , this is the LAST ROUND OF WHO WANTS TO BE A MILLIONAIRE, WE ARE FIGHTING FOR ONE MILLION DOLLARS!")
            print  ("Are you ready? type yes when you're ready")
            answerforready = input("Am I?")
            if answerforready == "yes":
                print ("Ok so the last question is: Which of the following landlocked countries is entirely contained within another country?")
                print ("Here are the choices!: ")
                print (" Lesotho")
                print (" Burkina Faso")
                print (" Mongolia")
                print (" Luxembourg")
                print (" Are you ready to answer,type yes when you're ready")
            answerfoready2 = input("Am I?")
            if answerfoready2 == "yes":
                print ("Okay , Lets go, you've got 45 seconds, if you have problems you can still choose one of the final round helpers that are not that accurate but if you're lucky enough you will win with them")
            usejokers = input("Do i want to use helpers?")
            if usejokers == "yes":
                print ("The Right answer should be Lesotho but im not sure enough!")
            answer6 = input("What is your Choice?: ")
            if answer6 == "Lesotho":
                print ("YOU WON ONE MILLION DOLLARS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            copyrightclaim =input("Do you want to see who created the game?")
            if copyrightclaim == "yes":
                print("Marlon Copin - Creator")
                print(" 2017 ")
            else:
                print("Bad Answer !")
                print("Please Quit!")
    keep_going()


#Game 8
#Tarot Reading
#Marlon C.
def Tarot():
      
    tarot_cards = ["The Fool: Fresh hope, take chances, new paths and adventures await.",
    "The Magician: Focussed creativity, turning visions into reality, sudden solutions may appear.",
    "The High Priestess: Secrets and hidden circumstances stand in the way, trust yourself.", 
    "The Empress: A gentle almost unnoticed power, rarely opposed.", 
    "The Emperor: You're up against real power, respect its leadership.", 
    "The Hierophant: Dependency on approval from elevated dignity.", 
    "The Lovers: Deeply felt mutual attraction or partnership.", 
    "The Chariot: Triumph! but beware of its consequences.",
    "Strength: Strength of a kind that's superior because of clever application.", 
    "The Hermit: A lesson and reward, but also misfortune of solitude.", 
    "Wheel of Fortune: An uncertain outcome, with n aftermath to be considered.", 
    "Justice: Justice without blinfold is not always fair.", 
    "The Hanged Man: Great personal sacrifice that still doesn't hurt much.", 
    "Death: A costly loss, big changes to move on from and transform.", 
    "Temperance: Balance and harmony, self control is strong.", 
    "The Devil: The pain and delight of giving in to temptation.", 
    "The Tower: A spectacular ambition that ends with disaster.", 
    "The Star: Time to pause and reflect, contemplate what's precious and what's not.",
    "The Moon: Longing for the sake of longing, hoping for fulfillment.",
    "The sun: Great resources at your disposal, but constrain yourself, it's possible to have too much.",
    "Judgement: Ultimate judgement, whether we welcome it or not.",
    "The world: Success in anything worldy, but not for free."]

    intro = "Welcome to Marlon's Mystical Tarot Reading!"
    player_input = input("Please choose which area of your life you would like to learn about:\nFamily, Work, Romantic, Friendship, or anything else\n")
    loading_str = "...carefully choosing your cards..."
    ending = "Thank you for letting me read you, please take this information with care :)"

    def random_cards1():
        card_one = random.choice(tarot_cards)
        tarot_cards.remove(card_one)
        return card_one

    def random_cards2():
        card_two = random.choice(tarot_cards)
        tarot_cards.remove(card_two)
        return card_two

    def random_cards3():
        card_three = random.choice(tarot_cards)
        return card_three

    game_str = ("Your card representing your past is " + random_cards1() + "\nYour card representing your present is " + random_cards2() + "\nYour card representing your future is " + random_cards3())

    #the game
    print(intro)
    print("You chose "+ player_input + " as the area of your life you would like to be read on")
    print(loading_str)
    print(game_str)
    print(ending)

#Game 9
#Little Story
#Alan Shultz
def Story():
    answer = input("would you like to start the game? (yes/no) ")
    stage = 0
    inventory = 0
    counter = 0
    while answer.lower().strip() != "yes":
        answer = input("would you like to start the game? (yes/no) ")
    if answer.lower().strip() == "yes":
        print("\nType forward/back/left/right to move around each area")
        print(
            "\nYou wake up groggy in a small, dimly lit room. You can see broken \nwindows on all 4 walls and debris scattered all over the place. It's obvious that no one has been here \nin a very long time.")
        stage = 1
    else:
        print("Maybe another time")


    def room1(stage, inventory, answer):
        answer = input("-forward/back/left/right ")
        if answer.lower().strip() == "forward":
            if inventory == 1:
                print("\nYou try the key you found, the door opens with a distinct clicking sound.")
                stage = 2
                inventory = 2
            elif inventory == 0:
                print("\nYou walk up to a rusty metal door, it appears to be locked.")
                print("\nYou go back to the center of the room.")
            elif inventory >= 2:
                print("\nYou exit the room you woke up in, and enter the dimly lit hallway once again")
                stage = 3
        elif answer.lower().strip() == "left":
            print("\nYou see a broken window, but it's too high up to reach.")
            print("\nYou go back to the center of the room.")
        elif answer.lower().strip() == "right":
            print("\nYou see a broken window, but it's too high up to reach.")
            print("\nYou go back to the center of the room.")
        elif answer.lower().strip() == "back":
            if inventory == 0:
                answer = input("\nYou find an old wooden crate, what would you like to do with it? (leave it/open it) ")            
                if answer.lower().strip() == "open it":
                    inventory +=1
                    print("\nYou pry open the crate and find a key inside.")
                    print("\nYou go back to the center of the room.")
                else:
                    print("\nYou go back to the center of the room.")
            elif inventory > 0:
                print("\nYou look at the wooden crate you opened.")
                print("\nYou go back to the center of the room.")
        return inventory, stage


    def room2(stage):
        print("\nYou exit the room you were previously in and enter a long hallway, the light level is roughly the same except for\nthe light bulb furthest to the left, which is flickering.")
        stage = 3
        return stage

    
    def room3(stage, inventory, answer):
        answer = input("-forward/back/left/right ")
        if answer.lower().strip() == "forward":
            print("\nYou examine the wall in front of you but all you see are some creepy paintings")
        elif answer.lower().strip() == "back":
            print("you go back inside the room you woke up in, nothing seems to have changed.")
            stage = 1
        elif answer.lower().strip() == "left":
            if inventory == 2:
                answer = input("You walk left until you the reach the end of the hallway, the door there is ajar.\nWould you like to open it? (open it/go back)")
                if answer.lower().strip() == "open it":
                    stage = 4
                    inventory = 3
                else:
                    print("you go back to the middle of the hallway.")
            elif inventory >= 3:
                print("go from hallway into kitchen, no basic text")
                stage = 5
        elif answer.lower().strip() == "right":
            print("Go into the dining room")
            stage = 6
        return inventory, stage


    def room4(stage):
        print("You enter the kitchen, basic text")
        stage = 5
        return stage


    def room5(stage, inventory, answer):
        answer = input("-forward/back/left/right ")
        if answer.lower().strip() == "back":
            print("You exit the kitchen and go back into the hallway.")
            stage = 3
        elif answer.lower().strip() == "forward":
            print("whatever is at this side of kitchen")
        elif answer.lower().strip() == "left":
            print("Maybe something to help progress the story in a cabinet idk yet")
        elif answer.lower().strip() == "right":
            print("Whatever I decide goes here")
        return inventory, stage


    def room6(stage):
        print("You enter the dining room, basic text")
        stage = 7
        return stage


    def room7(inventory, stage, answer):
        answer = input("-forward/back/left/right ")
    
        return inventory, stage


    while True:
        if stage == 1:
            inventory, stage =room1(stage, inventory, answer)
            print("Log stage: {}, inventory:{}, counter:{}".format(stage, inventory, counter))
            counter +=1
        elif stage == 2:
            stage =room2(stage)
            print("Log stage: {}, inventory:{}, counter:{}".format(stage, inventory, counter))
            counter +=1
        elif stage == 3:
            inventory, stage =room3(stage, inventory, answer)
            print("Log stage: {}, inventory:{}, counter:{}".format(stage, inventory, counter))
            counter +=1
        elif stage == 4:
            stage =room4(stage)
            print("Log stage: {}, inventory:{}, counter:{}".format(stage, inventory, counter))
            counter +=1
        elif stage == 5:
            inventory, stage =room5(stage, inventory, answer)
            print("Log stage: {}, inventory:{}, counter:{}".format(stage, inventory, counter))
            counter +=1
        elif stage == 6:
            stage =room6(stage)
            print("Log stage: {}, inventory:{}, counter:{}".format(stage, inventory, counter))
            counter +=1
        elif stage == 7:
            inventory, stage =room7(stage, inventory, answer)
            print("Log stage: {}, inventory:{}, counter:{}".format(stage, inventory, counter))
            counter +=1
#Home Terminal Page
def Welcome():
    print("Welcome To Marlon's Casino" + "\n")
    print("""
    - Rock Papers Scissors
    - Connect4
    - TicTacToe
    - BlackJack
    - BattleShip
    - Minesweeper
    - Who wants to be a Millionaire ?
    - Tarot Reading
    -Aj's Story
    """)
    selection = input("Please Select A game : ")
    if selection == "Rock Papers Scissors":
        os.system("clear")
        rocks_game()
    elif selection == "Connect4":
        os.system("clear")
        Connect4()
    elif selection == "TicTacToe":
        os.system("clear")
        TicTacToe()
    elif selection == "BlackJack":
        os.system("clear")
        BlackJack()
    elif selection == "BattleShip":
        os.system("clear")
        BattleShip()
    elif selection == "Minesweeper":
        os.system("clear")
        Mines()
    elif selection == "Who wants to be a Millionaire ?":
        os.system("clear")
        Millionaire()
    elif selection == "Tarot Reading":
        os.system("clear")
        Tarot()
    elif selection == "Aj's Story":
        os.system("clear")
        Story()

Welcome()


