variables = ["__1__", "__2__", "__3__", "__4__"]

easy_fill_in_blank = '''__1__ is a standardized system for tagging __2__ 
files to achieve font, color, graphic, and hyperlink effects on web pages. __3__ 
style sheets are used to format the __4__ of web pages. Source: Dictionary.com'''

medium_fill_in_blank = '''__1__ is an object-oriented computer __2__ language commonly 
used to create interactive effects within web browsers. This language is influenced by __3__ 
and the syntax is more similar to __4__. Source: Dictionary.com'''
hard_fill_in_blank = '''__1__ was first released in 1991 by Guido van __2__. Like __3__ and __4__, Python is used for creating web apps and dynamic web content. Source: Google'''

easy_fib_answers = ["html", "text", "css", "layout"]
medium_fib_answers = ["javascript", "programming", "java", "c"]
hard_fib_answers = ["python", "Rossum", "ruby", "perl"]

###################################
# welcome to the game #
###################################

def welcome(user_name):

	# this will show player and fill in the blank game information
	# inputs include user name and output includes the welcome

    print "\nWelcome, " + user_name + ". The goal of the game is to fill-in-the-blanks appropriately to test your coding knowledge. Please choose your level of difficulty by entering a number from 1 to 3. 1 being easy. 3 being hard."

###################################
# game levels defined #
###################################

def setup(difficulty_level):

	# groups fill in the blanks and answers together
	# input will include difficulty level
	# output include the specified fill in the blank statement

	if difficulty_level == "1":
		print "\nThanks for choosing level 1, easy. Let's begin!\n"
		return easy_fill_in_blank, easy_fib_answers

	elif difficulty_level == "2":
		print "\nThanks for choosing level 2, medium. Let's begin!\n"
		return medium_fill_in_blank, medium_fib_answers

	else:
		print "\nThanks for choosing level 3, hard. Let's begin!\n"
		return hard_fill_in_blank, hard_fib_answers


###################################
# replacing variables #
###################################

def replace_variables(fill_in_the_blank_split, player_response, idx):

# this will replace blank with answer
# input includes variables list replacing the fill int he blank if applicable
# output correctly replaced fill in the blank

    fill_in_the_blank_split[idx] = player_response

    return fill_in_the_blank_split

###################################
# filling in the answers #
###################################

def fill_answers(fill_in_the_blank_split, player_response, index):

# this will replace each variable with the correct answer
# input from variable from difficulty level, variable list the replaced fill in the blank that has the correct answer thus far .. and outputs will correctly replace fill in the blank

    for idx, word in enumerate(fill_in_the_blank_split):
        if word == variables[index]:
            replaced = replace_variables(fill_in_the_blank_split, player_response, idx)
            break

    replaced = " ".join(replaced)
    head, sep, tail = replaced.partition("Google") # getting rid of replacements that are added onto fill in blank
    replaced = head + sep
    return replaced

###################################
# getting answers #
###################################

def get_answers(difficulty_level, fill_in_blank, answers):

	# to collect users answers
	# input current level, fill in the blank and answers
	# output the updated replaced fill in the blank, index of each answer

    fill_in_the_blank_split = fill_in_blank.split()

    player_response = ""
    
    index = 0
    for variable in variables: 

	# q and a get's stated

        question = "\nWhat's the answer for " + variable + "?"
        print question
        player_response = raw_input("Type right here: ")
        player_response = player_response.lower()

        while player_response != answers[index]:
                print "\nWrong Answer. Try again.\n"
                player_response = raw_input("Please type your answer again.")
                player_response = player_response.lower()

        print "\nGreat, 10/10. This is correct!\n"

        replaced = fill_answers(fill_in_the_blank_split, player_response, index)
        print replaced

        index += 1

    return replaced, index

###################################
# let's play here !!! #
###################################

def play_fill_in_blank():

	# the whole program or game will but output

	user_name = raw_input("What's the current users' name?")  # type: str
	welcome(user_name)

	difficulty_level = raw_input("\nEasy = 1, Medium = 2, Hard = 3")

	if difficulty_level == "1" or difficulty_level == "2" or difficulty_level == "3":
		fill_in_the_blank, answers = setup(difficulty_level)
		print fill_in_the_blank

		replaced = get_answers(difficulty_level, fill_in_the_blank, answers)

		print "\nGreat Job, " + user_name + ", CONGRATS! YOU WON!!!\n"

	else:

		print "\nYour answer is wrong. Please pick a level, " + user_name + ". The game will restart.\n"
		play_fill_in_blank()

play_fill_in_blank()
