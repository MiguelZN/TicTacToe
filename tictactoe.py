import random
import time, os
from tkinter import *

#file path of folder
path = os.path.dirname(os.path.realpath(sys.argv[0]))

iconpath = path+r"\tictactoeicon.ico"



testrow = ""
testcolumn = ""   
randomcolors = ["red", "blue", "green", "yellow", "orange"]

class blankboard():
    
    def __init__(self):
        self.createBoard() #initializes 'E' 2dBoard
        
        
    def createBoard(self):
        board = []
        for i in range(3):
            row = []
            for k in range(3):
                row = row+[" "]
                
            board.append(row)
            
        self.emptyboard = board
        
    def getBoard(self):
        return self.emptyboard
    
  
class gameCPU():
    def __init__(self):
        self.player = ""
        self.computer = ""
        
        self.board = blankboard()
        self.appointroles()
        self.playerwins = 0
        self.computerwins = 0
        self.numberofgames = 0
        
    def getBoard(self):
        return self.board
    def getNumberofgames(self):
        return self.numberofgames
    def getPlayerwins(self):
        return self.playerwins
    def getComputerwins(self):
        return self.computerwins
    def getCurrent(self):
        return self.currentturn
    def getPlayer(self):
        return self.player
    def getComputer(self):
        return self.computer


    
    
    def setBoard(self, board):
        self.board = board
    def setNumberofgames(self, amount):
        self.numberofgames = amount
    def setPlayerwins(self, amount):
        self.playerwins = amount
    def setComputerwins(self, amount):
        self.computerwins = amount
        
    def incrementGames(self):
        self.setNumberofgames(self.getNumberofgames()+1)    
        
    def resetBoard(self):
        self.setBoard(blankboard())
    
    def appointroles(self):
        self.player= random.choice(["X","O"])
        self.currentturn = random.choice(["X","O"])
        
        #assigns random symbol to player and computer 
        """
        if(self.player=="X"):
            self.computer = "O"
            
        else:
            self.computer = "O"
            self.player = "X"
        """
        
        self.player = "X"
        self.computer = "O"
        
        #assigns who goes first based on a random pick at beginning of game
        if(self.player == self.currentturn):
            self.currentturn = "player"
        else:
            self.currentturn = "computer"  
            
    def newturn(self):
     
        if (self.currentturn == "player"):
            self.currentturn = "computer"
        elif(self.currentturn == "computer"):
            self.currentturn = "player"
        else:
            print("error")
            
    
    def Playerturn(self, row, column):
        if (self.getCurrent() == "player" and self.board.getBoard()[row][column].isspace()):
            self.board.getBoard()[row][column] = self.getPlayer()
            self.newturn()
            
    def CPUturn(self):
        randomrow = random.randrange(0,len(game.board.getBoard()))
        randomcolumn = random.randrange(0,len(game.board.getBoard()[0]))
        CPUpicked = game.board.getBoard()[randomrow][randomcolumn]     
        if (CPUpicked.isalpha()==False): #if it is an empty spot
            testrow = randomrow
            testcolumn = randomcolumn
            print(randomrow)
            print(randomcolumn)
            game.board.getBoard()[randomrow][randomcolumn] = self.getComputer()
        else:
            self.CPUturn()             
    
        
     
        
def checkwinner(board, AI, player):
    if (board[0][0]+board[0][1]+board[0][2] == AI*3) or (board[1][0]+board[1][1]+board[1][2] ==AI*3) or (board[2][0]+board[2][1]+board[2][2] == AI*3) or (board[0][0]+board[1][0]+board[2][0] == AI*3) or (board[0][1]+board[1][1]+board[2][1]==AI*3) or (board[0][2]+board[1][2]+board[2][2] == AI*3) or (board[0][0]+board[1][1]+board[2][2] == AI*3) or (board[2][0]+board[1][1]+board[0][2] ==AI*3):
        return "computer"
    elif (board[0][0]+board[0][1]+board[0][2] == player*3) or (board[1][0]+board[1][1]+board[1][2] ==player*3) or (board[2][0]+board[2][1]+board[2][2] == player*3) or (board[0][0]+board[1][0]+board[2][0] == player*3) or (board[0][1]+board[1][1]+board[2][1]==player*3) or (board[0][2]+board[1][2]+board[2][2] == player*3) or (board[0][0]+board[1][1]+board[2][2] == player*3) or (board[2][0]+board[1][1]+board[0][2] ==player*3):
        return "player"
    else:
        return "None"
    
            

game = gameCPU()

 

class tictactoegui(Frame):
    def __init__(self, root, rootx, rooty):
        #tictactoe game
        
        
        super().__init__(root)
        self.grid(row = 1, column = 1, padx = int(rootx/20))
        self.listofnumbers = []
        self.buttonlist = []
        self.scalex = int(rootx/25)
        self.scaley = int(rooty/50)
        self.scaley2 = int(self.scaley/2)+1
        self.gamestate = "Game#:\n"+ str(game.getNumberofgames())+"\n\n\nPlayer wins:\n"+str(game.getPlayerwins())+"\nComputer wins:\n"+str(game.getComputerwins())+"\n\n\n\n\n\nCurrent Turn:\n"+str(game.getCurrent().title())
        
        self.createButtons() #self.buttonlist
        self.buttonlist[0][0]["command"] = self.Button00
        self.buttonlist[0][1]["command"] = self.Button01
        self.buttonlist[0][2]["command"] = self.Button02
        self.buttonlist[1][0]["command"] = self.Button10
        self.buttonlist[1][1]["command"] = self.Button11
        self.buttonlist[1][2]["command"] = self.Button12
        self.buttonlist[2][0]["command"] = self.Button20
        self.buttonlist[2][1]["command"] = self.Button21
        self.buttonlist[2][2]["command"] = self.Button22
        #createLabel(root, 1,0,"Game#:\n\n\nPlayer1 wins:\n\nPlayer2 wins:\n\n\n\n\n\n\nCurrent Turn:", rooty)
        self.stateLabel = Label(root, text = self.gamestate, font = rooty)
        self.stateLabel.grid(row = 1, column = 0, padx = 5)
        
        self.colorButton = Button(root, text = "Color", font =rooty)
        self.colorButton["command"]= changecolor
        self.colorButton.grid(row = 2, column = 0 , pady =5)
        #resetButton = createButton(root, 0,0,"Reset Game", rooty) 
        self.resetButton = Button(root, text= "Reset Game", font = rooty)
        self.resetButton.grid(row = 0, column = 0, pady =5)
        self.resetButton["command"] = self.newBoard
        self.run()
        #self.startButton = Button(root, text= "Start", font = rooty)
        #self.startButton.grid(row = 2, column = 0)
    

    def newBoard(self):
        game.resetBoard()
        self.updateStateLabel("Game#:\n"+ str(game.getNumberofgames())+"\n\n\nPlayer wins:\n"+str(game.getPlayerwins())+"\nComputer wins:\n"+str(game.getComputerwins())+"\n\n\n\n\n\nCurrent Turn:\n"+str(game.getCurrent().title()))
        self.updateButtons()     
        
    def newGameCPU(self):
        game.incrementGames()
        self.newBoard()
        #self.newGameCPU()
        self.iswon()
        self.updateStateLabel("Game#:\n"+ str(game.getNumberofgames())+"\n\n\nPlayer wins:\n"+str(game.getPlayerwins())+"\nComputer wins:\n"+str(game.getComputerwins())+"\n\n\n\n\n\nCurrent Turn:\n"+str(game.getCurrent().title()))               
    
    def iswon(self):
        if((checkwinner(game.board.getBoard(), game.getComputer(),game.getPlayer())== "computer") 
            or (checkwinner(game.board.getBoard(), game.getComputer(),game.getPlayer())== "player")):
            
            if(checkwinner(game.board.getBoard(), game.getComputer(),game.getPlayer())== "computer"):
                game.setComputerwins(game.getComputerwins()+1)
            if(checkwinner(game.board.getBoard(), game.getComputer(),game.getPlayer())== "player"):
                game.setPlayerwins(game.getPlayerwins()+1)
            self.newGameCPU()
            self.updateStateLabel("Game#:\n"+ str(game.getNumberofgames())+"\n\n\nPlayer wins:\n"+str(game.getPlayerwins())+"\nComputer wins:\n"+str(game.getComputerwins())+"\n\n\n\n\n\nCurrent Turn:\n"+str(game.getCurrent().title()))        
    def run(self):
      
                
        if game.getCurrent() == "player":
            print("")
            
        elif game.getCurrent() == "computer":
            game.CPUturn()
            print(game.getCurrent())
            self.iswon()
            game.newturn()
            self.updateStateLabel("Game#:\n"+ str(game.getNumberofgames())+"\n\n\nPlayer wins:\n"+str(game.getPlayerwins())+"\nComputer wins:\n"+str(game.getComputerwins())+"\n\n\n\n\n\nCurrent Turn:\n"+str(game.getCurrent().title()))
            self.updateButtons()
            
    def Button00(self):
        self.iswon()
        game.Playerturn(0,0)
        self.updateStateLabel("Game#:\n"+ str(game.getNumberofgames())+"\n\n\nPlayer wins:\n"+str(game.getPlayerwins())+"\nComputer wins:\n"+str(game.getComputerwins())+"\n\n\n\n\n\nCurrent Turn:\n"+str(game.getCurrent().title()))
        self.updateButtons()
        self.run()
    def Button01(self):
        self.iswon()
        game.Playerturn(0,1)
        self.updateStateLabel("Game#:\n"+ str(game.getNumberofgames())+"\n\n\nPlayer wins:\n"+str(game.getPlayerwins())+"\nComputer wins:\n"+str(game.getComputerwins())+"\n\n\n\n\n\nCurrent Turn:\n"+str(game.getCurrent().title()))
        self.updateButtons() 
        self.run()
    def Button02(self):
        self.iswon()
        game.Playerturn(0,2)
        self.updateStateLabel("Game#:\n"+ str(game.getNumberofgames())+"\n\n\nPlayer wins:\n"+str(game.getPlayerwins())+"\nComputer wins:\n"+str(game.getComputerwins())+"\n\n\n\n\n\nCurrent Turn:\n"+str(game.getCurrent().title()))
        self.updateButtons()    
        self.run()
    def Button10(self):
        self.iswon()
        game.Playerturn(1,0)
        self.updateStateLabel("Game#:\n"+ str(game.getNumberofgames())+"\n\n\nPlayer wins:\n"+str(game.getPlayerwins())+"\nComputer wins:\n"+str(game.getComputerwins())+"\n\n\n\n\n\nCurrent Turn:\n"+str(game.getCurrent().title()))
        self.updateButtons()   
        self.run()
    def Button11(self):
        self.iswon()
        game.Playerturn(1,1)
        self.updateStateLabel("Game#:\n"+ str(game.getNumberofgames())+"\n\n\nPlayer wins:\n"+str(game.getPlayerwins())+"\nComputer wins:\n"+str(game.getComputerwins())+"\n\n\n\n\n\nCurrent Turn:\n"+str(game.getCurrent().title()))
        self.updateButtons() 
        self.run()
    def Button12(self):
        self.iswon()
        game.Playerturn(1,2)
        self.updateStateLabel("Game#:\n"+ str(game.getNumberofgames())+"\n\n\nPlayer wins:\n"+str(game.getPlayerwins())+"\nComputer wins:\n"+str(game.getComputerwins())+"\n\n\n\n\n\nCurrent Turn:\n"+str(game.getCurrent().title()))
        self.updateButtons()
        self.run()
    def Button20(self):
        self.iswon()
        game.Playerturn(2,0)
        self.updateStateLabel("Game#:\n"+ str(game.getNumberofgames())+"\n\n\nPlayer wins:\n"+str(game.getPlayerwins())+"\nComputer wins:\n"+str(game.getComputerwins())+"\n\n\n\n\n\nCurrent Turn:\n"+str(game.getCurrent().title()))
        self.updateButtons()
        self.run()
    def Button21(self):
        self.iswon()
        game.Playerturn(2,1)
        self.updateStateLabel("Game#:\n"+ str(game.getNumberofgames())+"\n\n\nPlayer wins:\n"+str(game.getPlayerwins())+"\nComputer wins:\n"+str(game.getComputerwins())+"\n\n\n\n\n\nCurrent Turn:\n"+str(game.getCurrent().title()))
        self.updateButtons()
        self.run()
    def Button22(self):
        self.iswon()
        game.Playerturn(2,2)
        self.updateStateLabel("Game#:\n"+ str(game.getNumberofgames())+"\n\n\nPlayer wins:\n"+str(game.getPlayerwins())+"\nComputer wins:\n"+str(game.getComputerwins())+"\n\n\n\n\n\nCurrent Turn:\n"+str(game.getCurrent().title()))
        self.updateButtons()
        self.run()

    def updateStateLabel(self, text):
        self.stateLabel["text"] = text

    def updateButtons(self):
        for i in range(3):
            for k in range (3):
                self.buttonlist[i][k]["text"] = game.board.getBoard()[i][k]
    
    def getScalex(self):
        return self.scalex
    
    def create2dlist(self):
        for i in list(range(3)):
            row = []
            for k in list(range(3)):
                row = row+ [i,k]
            self.listofnumbers.append(row)
        
    def createButtons(self):
        self.create2dlist()
        for i in range(3):
            row = []
            for k in range (3):
                x = Button(self, text = game.board.getBoard()[i][k], font = self.scalex, width= self.scaley, height = self.scaley2)
                x.grid(row = i, column = k)
                row = row+[x]
                
            self.buttonlist.append(row)
            
       
    def getButtonlist(self):
        return self.buttonlist
    
def createLabel(master, rowN, columnN, desc, scale):
    x = Label(master, text = desc, font = scale)
    x.grid(row = rowN, column = columnN)
    
def createButton(master, rowN, columnN, desc, scale):
    x = Button(master, text = desc, font = scale)
 #   x["command"] 
    x.grid(row = rowN, column = columnN)
    return x

def changecolor():
    root.config(background = random.choice(randomcolors))    

root = Tk()
root.title("TicTacToe- Miguel Zavala")
root.geometry(str(500)+"x"+str(500))
root.iconbitmap(r""+iconpath)
root.config(background= random.choice(randomcolors))
tictactoegui(root, 500,500)
root.mainloop()

    
        
