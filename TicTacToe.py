def check_win():
    if (a[0]==a[3] and a[0]==a[6]):
            if a[0]=="X":
                print "Player 1 Wins!!!"
                return True
            else:
                print "Player 2 Wins!!!"
                return True
    elif (a[0]==a[1] and a[0]==a[2]):
            if a[0]=="X":
                print "Player 1 Wins!!!"
                return True
            else:
                print "Player 2 Wins!!!"
                return True
## First Diagonal
    elif (a[0]==a[4] and a[0]==a[8]):
            if a[0]=="X":
                print "Player 1 Wins!!!"
                return True
            else:
                print "Player 2 Wins!!!"
                return True
## Second Diagonal
     elif (a[2]==a[4] and a[2]==a[6]):
            if a[0]=="X":
                print "Player 1 Wins!!!"
                return True
            else:
                print "Player 2 Wins!!!"
                return True

    elif (a[1]==a[4] and a[1]==a[7]):
            if a[1]=="X":
                    print "Player 1 Wins!!!"
            else:
                    print "Player 2 Wins!!!"
    elif (a[2]==a[5] and a[2]==a[8]):
            if a[3]=="X":
                print "Player 1 Wins!!!"
                return True
            else:
                print "Player 2 Wins!!!"
                return True
    elif (a[3]==a[4] and a[4]==a[5]):
            if a[3]=="X":
                print "Player 1 Wins!!!"
                return True
            else:
                print "Player 2 Wins!!!"
                return True
    elif (a[6]==a[7] and a[7]==a[8]):
            if a[6]=="X":
                print "Player 1 Wins!!!"
                return True
            else:
                print "Player 2 Wins!!!"
                return True
     

## Main Body of Game
from IPython.display import clear_output
print "Following is your board for play, please input your slot repectively:"
## Assign a matrix
a= [0,0,0,0,0,0,0,0,0]
for i in range(1,10):
    a[i-1]=i
## Print Matrix Function
def print_matrix():
    print "  ",a[0],"  |  ",a[1],"  |  ",a[2],"  "
    print "----------------------"
    print "  ",a[3],"  |  ",a[4],"  |  ",a[5],"  "
    print "----------------------"
    print "  ",a[6],"  |  ",a[7],"  |  ",a[8],"  "


## Take Input from Player
print_matrix()
for r in range(1,6):
    x = input("Player 1: Input Slot no. :")
    if (x<1) and (x>9):
        print "Non Valid Entry!!!"
        break
    else:
        a[x-1]="X"
    if check_win()==True:
        clear_output()
        print_matrix()
        break    
    y = input("Player 2: Input Slot no. :")
    if (y<1) and (y>9):
        print "Non Valid Entry!!!"
        break
    else:
        a[y-1]="O"
    clear_output()
    print_matrix()
    if check_win()==True:
        clear_output()
        print_matrix()
        break
