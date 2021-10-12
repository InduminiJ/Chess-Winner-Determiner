#Prints the chessboard in a grid form
def gridprint(chessboard):
	for x in chessboard:
		print(*x, sep=' ')

#This function calculates the scores for the current chessboard and determines a winner
def findWinner(chessboard):
	counter1 = 0
	counter2 = 0
	countrow = -1
	countcol = 0
	
	#program checks each column in each row (every element in the list) to see if it is equal to the chesspieces. If it is equal, then the counter with the score increases accordingly.
	for row in (chessboard):
		countrow +=1
		for col in chessboard:
			while countcol <=7:
				if chessboard[countrow][countcol] == 'Q':
					counter1 +=10
				if chessboard[countrow][countcol] == 'R':
					counter1 +=5
				if chessboard[countrow][countcol] == 'N':
					counter1 +=3.5
				if chessboard[countrow][countcol] == 'B':
					counter1 +=3
				if chessboard[countrow][countcol] == 'P':
					counter1 +=1
				if chessboard[countrow][countcol] == 'q':
					counter2 +=10
				if chessboard[countrow][countcol] == 'r':
					counter2 +=5
				if chessboard[countrow][countcol] == 'n':
					counter2 +=3.5
				if chessboard[countrow][countcol] == 'b':
					counter2 +=3
				if chessboard[countrow][countcol] == 'p':
					counter2 +=1
				countcol += 1
		countcol = 0
			
	print("\nThe current score for Black is", counter1, "and the score for white is", counter2)
	#Checks which score is higher
	if counter1 > counter2:
		print("Black is the winner!")
	elif counter1 < counter2:
		print("White is the winner!")
	else:
		print("There is a tie!")

#This function asks the user if they want to move a piece, restart or quit the program
def final(chessboard):
	while True:
		finalq = int(input("\nDone! Would you like to \n1. Move a piece \n2. Create new board \n3. Quit \n"))
		if finalq == 1:
			move(chessboard)
		if finalq == 2:
			main()
		if finalq == 3:
			quit()
		else:
			print("This is not a valid answer")
			continue

#This function is responsible for moving the chess piece into the desired spot. It uses the chessboard (from main) as an argument and it outputs the final chessboard (after moving)
def move(chessboard):
	xold = (int(input("Which piece would you like to move?  \n'x' coordinate: "))-1)
	yold = (int(input("Which piece would you like to move? 'y' coordinate: "))-1)
	xnew = (int(input("Where would you like to move it?  \n'x' coordinate: "))-1)
	ynew = (int(input("Where would you like to move it? 'y' coordinate: "))-1)

	#Checks if the user is moving a real chess piece or an emtpy spot
	if chessboard[xold][yold] == '-':
		print("There is no piece there\n")
		move(chessboard)
	#takes the character in the old spot (the piece the user wants to move) and sets that to the new spot the user wishes to move it to. Then the old spot is replaces with a '-' to show that it is empty.	
	else:
		let = ord(chessboard[xold][yold])
		chessboard[xnew][ynew] = chr(let)
		chessboard[xold][yold] = '-'
		gridprint(chessboard)

def main():	
	valid = '''-kqbnrpKQBNRP'''
	#Checks if the user enters a chessboard that is over/shorter than 8 pieces
	while True:
		r1=input("Please enter your chessboard. Use CAPS for black pieces. Lowercase for white pieces. Valid chess pieces are (K)ing, (Q)ueen, (B)ishop, k(N)ight, (R)ook, and (P)awn. *Note: use '-' for empty spaces. Press enter to go to the next row.\n")
		if len(r1) != 8:
			print("Please enter a valid chessboard. (8x8!)\n")
			continue
		r2=input()
		if len(r2) != 8:
			print("Please enter a valid chessboard. (8x8!)\n")
			continue
		r3=input()
		if len(r3) != 8:
			print("Please enter a valid chessboard. (8x8!)\n")
			continue
		r4=input()
		if len(r4) != 8:
			print("Please enter a valid chessboard. (8x8!)\n")
			continue
		r5=input()
		if len(r5) != 8:
			print("Please enter a valid chessboard. (8x8!)\n")
			continue
		r6=input()
		if len(r6) != 8:
			print("Please enter a valid chessboard. (8x8!)\n")
			continue
		r7=input()
		if len(r7) != 8:
			print("Please enter a valid chessboard. (8x8!)\n")
			continue
		r8=input()
		if len(r8) != 8:
			print("Please enter a valid chessboard. (8x8!)\n")
			continue

		#This checks if the user enters a valid letter for the chesspiece.
		for char in r1:
			if char not in valid:
				print("Please enter a valid chesspiece\n")
				continue
		for char in r2:
			if char not in valid:
				print("Please enter a valid chesspiece\n")
				continue
		for char in r3:
			if char not in valid:
				print("Please enter a valid chesspiece\n")
				continue
		for char in r4:
			if char not in valid:
				print("Please enter a valid chesspiece\n")
				continue
		for char in r5:
			if char not in valid:
				print("Please enter a valid chesspiece\n")
				continue
		for char in r6:
			if char not in valid:
				print("Please enter a valid chesspiece\n")
				continue
		for char in r7:
			if char not in valid:
				print("Please enter a valid chesspiece\n")
				continue
		for char in r8:
			if char not in valid:
				print("Please enter a valid chesspiece\n")
		break

	row1 = []
	row2 = [] 
	row3 = []
	row4 = []
	row5 = []
	row6 = []
	row7 = []
	row8 = []
	col1 = []
	col2 = []
	col3 = []
	col4 = []
	col5 = []
	col6 = []
	col7 = []
	col8 = []
	chessboard = []

	#This sets the chesspieces the user enters into a (1D) list 
	for char in r1:
		row1.append(char)

	for char in r2:
		row2.append(char)

	for char in r3:
		row3.append(char)

	for char in r4:
		row4.append(char)

	for char in r5:
		row5.append(char)

	for char in r6:
		row6.append(char)

	for char in r7:
		row7.append(char)

	for char in r8:
		row8.append(char)

	#This sets makes the list 2D by making the columns a list of the row.
	chessboard = [row1, row2, row3, row4, row5, row6, row7, row8]
	row1 = [col1, col2, col3, col4, col5, col6, col7, col8]
	row2 = [col1, col2, col3, col4, col5, col6, col7, col8]
	row3 = [col1, col2, col3, col4, col5, col6, col7, col8]
	row4 = [col1, col2, col3, col4, col5, col6, col7, col8]
	row5 = [col1, col2, col3, col4, col5, col6, col7, col8]
	row6 = [col1, col2, col3, col4, col5, col6, col7, col8]
	row7 = [col1, col2, col3, col4, col5, col6, col7, col8]
	row8 = [col1, col2, col3, col4, col5, col6, col7, col8]
	
	print("\n Here is your chessboard")
	gridprint(chessboard)
	
	findWinner(chessboard)
	
	final(chessboard)
		
	
main()
