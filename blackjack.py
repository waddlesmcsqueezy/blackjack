import json
import requests
import enum

link = "http://deckofcardsapi.com/api/deck"
game_type = ""

# Enum GameType
# 	Used for determining what game the user is playing

class GameType(Enum):
	BLACKJACK = "blackjack"
	
# Class Player
# 	

class Player:
	def __init__( self ):
		self.hand = None
		self.bet = 0

	def placeBet( ):
		
	def dealCard( ):
		

# Function createDecks
# 	Gets new deck(s) of 52 cards and stores them in variable decks
# Receives: amount of decks (int)
# Returns: n/a

def createDecks( deck_count ):
	decks = requests.get( link + "/new/shuffle/?deck_count=" + str( deck_count ) )

	decks = decks.json( )

# Function setGame:
# 	Edits the global string variable game_type to the appropriate type. 
# 	Prints error message if user_input is an invalid choice.
# Receives: user input (str)
# Returns: n/a

def setGameType( str( user_input ).lower( ) ):
	for game in GameType:
		if user_input == game:
			game = user_input
		else:
			raise Exception( '''Game type should correspond to available game types.\n
					    Allowed game types are:\n''' + [game for game in GameType])
# Function prompt
# Receives: optional string to be displayed before input prompt (str)
# Returns: user input (str)

def prompt( optional_string = "" ):
	if optional_string != "":
		print( optional_string )

	print( "Enter Command: " )

	user_input = input( )
	
	return user_input

def inputLoop( ):
	while user_input != "exit":
		prompt( )

def main( ):
	decks = createDecks( 6 )
	
	print( '''Welcome to Blackjack\n
		  Type /help for commands list''' )
	
	inputLoop( )
