import random , math

def computer_player() :
    if ( computer == 1 ) :
        print( 'Computer has selected rock!' )
    elif ( computer == 2 ) :
        print( 'Computer has selected paper!' )
    else  :
        print( 'Computer has selected scissors!' )


        
def player_rock() :
    if ( computer == 1 ) :
        print( 'Draw Game!' )
    elif ( computer == 2 ) :
        print( 'You lose!' )
    else  :
        print( 'You win!' )

def player_paper() :
    if ( computer == 2 ) :
        print( 'Draw Game!' )
    elif ( computer == 1  ) :
        print( 'You win!' )
    else  :
        print( 'You lose!' )

def player_scissors() :
    if ( computer == 2 ) :
        print( 'You win!' )
    elif ( computer == 1 ) :
        print( 'You lose!' )
    else  :
        print( 'Draw Game!' )

computer = math.ceil( random.random() * 3 )
