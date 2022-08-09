from time import *
from RPS_Func import *

print( 'Welcome to the Rock, Paper, Scissors Game!' )
sleep( 2 )
input( 'Press ENTER to begin...' )
print( 'Now loading, please wait...' )
sleep( 3 )

player = input( 'Please select rock, paper, or scissors: ' )
print( 'You have selected' , player )

sleep( 2 )
computer_player()

sleep( 2 )
if ( player == 'rock' ) :
    player_rock()

sleep( 2 )
if ( player == 'paper' ) :
    player_paper()

sleep( 2 )
if ( player == 'scissors' ) :
    player_scissors()





    
sleep( 2 )
print( 'This is the end of the game!' )
