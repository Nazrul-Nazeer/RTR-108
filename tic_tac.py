import random

players = []
players_wepon = []
progress = {}
progress_l = []
player_playing = ''
list_player1_moves = []
list_player2_moves = []
lis = list_player1_moves + list_player2_moves

def intialize():
	global players
	global players_wepon
	global player_playing
	
	print("Welcome to NON-GUI TIC-TAC-TOE")
	print("")
	print("\t    _ |    | _  ")
	print("\t   |_||    ||_| ")
	print("\t------------------")
	print("\t      |    |    ")
	print("\t      |    |    ")
	print("\t------------------")
	print("\t      | \/ |    ")
	print("\t      | /\ |    ")
	print("")
	print("")
	
	for i in range(0,2):
		players.insert(i, input("Player{} Enter your name : ".format(i + 1)))
		print("")
		if players[i] is "":
			players.pop(i)
			print("Please Enter a valid name!")
			players.insert(i, input("Player{} Enter your name : ".format(i + 1)))
		else:
			continue	
	i = 0
	while i < 2:
		players_wepon.insert(i, input("{} Select your wepon 'X' or 'O'! : ".format(players[i])))
		print("")
		if players_wepon[i] == 'X' or players_wepon[i] == 'O':
			if players_wepon[i] is "":
				players_wepon.pop(i)
				print("Please Enter Requested 'X' or 'O'!")
				continue
			else:
				i = i + 1
				continue
		else:
			print("Enter only required 'X' or 'O'!")
			players_wepon.pop(i)
			
	r = random.randrange(0,2,1)
	player_playing = players[r]

	print("\t   1 |  2 |  3 ")	
	print("\t---------------")
	print("\t   6 |  5 |  4 ")	
	print("\t---------------")
	print("\t   7 |  8 |  9 ")
	print("")
			

	return players, players_wepon, player_playing

def alternate_player():
	global players
	global player_playing 
	q = players.index(player_playing)
	if q == 1:
		player_playing = players[0]
	else:
		player_playing = players[1]
	register_input()
	return player_playing
	
	
def register_input():
	global players
	global player_playing
	global progress
	global progress_l
	
	move = input("{} make your move (1-9) : ".format(player_playing))
	if move == '1' or move == '2' or move == '3' or move == '4' or move == '5' or move == '6' or move == '7' or move == '8' or move == '9':
		if move in progress_l:
			print("Enter a diffrent number, That spot has aldready been taken!")
			return register_input()
		else:
			progress_l.append(move)
			progress[move] = player_playing
	else:
		print("Enter a number between 1 to 9!")
		return register_input()
	return progress

def prepare_check():
	global list_player1_moves
	global list_player2_moves
	global progress
	global player_playing
	global players
	
	for move,player in progress.items():
		if player == players[0]:
			if move in list_player1_moves:
				continue
			else:
				list_player1_moves.append(move)
		else:
			if move in list_player2_moves:
				continue
			else:
				list_player2_moves.append(move)
			
	return list_player1_moves,list_player2_moves

def sequence_check(seq, list_tc):
	for i in range(len(list_tc)-len(seq)+1):
		for j in range(len(seq)):
			if list_tc[i + j] != seq[j]:
				break
			else:
				return True
		return False
	
def win_loose():
	print_sceern()
	print("")
	global list_player1_moves
	global list_player2_moves
	global players
	
	result = ''
	result_1 = ''
	i = 0
	j = 3
	
	s = ''.join(str(i) for i in sorted(list_player1_moves))
	d = ''.join(str(o) for o in sorted(list_player2_moves))
	if '123' in s or '147' in s or '159' in s or '456' in s or '369' in s or '258' in s or '753' in s or '789' in s or '231' in s or '546' in s or '528' in s or '537' in s or '471' in s or '897' in s or '591' in s or '693' in s or '321' in s or '654' in s or '852' in s or '357' in s or '741' in s or '987' in s or '951' in s or '963' in s or '213' in s or '645' in s or '825' in s or '375' in s or '714' in s or '978' in s or '915' in s or '936' in s:
		print("Congratulation {} has won!".format(players[0]))
		exit()
	elif '123' in d or '147' in d or '159' in d or '456' in d or '369' in d or '258' in d or '753' in d or '789' in d or '231' in d or '546' in d or '528' in d or '537' in d or '471' in d or '897' in d or '591' in d or '693' in d or '321' in d or '654' in d or '852' in d or '357' in d or '741' in d or '987' in d or '951' in d or '963' in d or '213' in d or '645' in d or '825' in d or '375' in d or '714' in d or '978' in d or '915' in d or '936' in d:
		print("Congratulation {} has won!".format(players[1]))
		exit()
	else:
		return
	
	return
	
def print_sceern():
	global players
	global players_wepon
	global list_player1_moves
	global list_player2_moves
	player1_wepon = players_wepon[0]
	player2_wepon = players_wepon[1]

	pre_1 = 0
	pre_2 = 0
	pre_3 = 0
	pre_4 = 0
	pre_5 = 0
	pre_6 = 0
	pre_7 = 0
	pre_8 = 0
	pre_9 = 0
	pre_11 = 0
	pre_22 = 0
	pre_33 = 0
	pre_44 = 0
	pre_55 = 0
	pre_66 = 0
	pre_77 = 0
	pre_88 = 0
	pre_99 = 0
	sre_1 = " "
	sre_2 = " "
	sre_3 = " "
	sre_4 = " "
	sre_5 = " "
	sre_6 = " "
	sre_7 = " "
	sre_8 = " "
	sre_9 = " "
	
	if '1' in list_player1_moves:
		pre_1 = 1
	if '2' in list_player1_moves:
		pre_2 = 2
	if '3' in list_player1_moves:
		pre_3 = 3
	if '4' in list_player1_moves:
		pre_4 = 4
	if '5' in list_player1_moves:
		pre_5 = 5
	if '6' in list_player1_moves:
		pre_6 = 6
	if '7' in list_player1_moves:
		pre_7 = 7
	if '8' in list_player1_moves:
		pre_8 = 8
	if '9' in list_player1_moves:
		pre_9 = 9
		
	if '1' in list_player2_moves:
		pre_11 = 1
	if '2' in list_player2_moves:
		pre_22 = 2
	if '3' in list_player2_moves:
		pre_33 = 3
	if '4' in list_player2_moves:
		pre_44 = 4
	if '5' in list_player2_moves:
		pre_55 = 5
	if '6' in list_player2_moves:
		pre_66 = 6
	if '7' in list_player2_moves:
		pre_77 = 7
	if '8' in list_player2_moves:
		pre_88 = 8
	if '9' in list_player2_moves:
		pre_99 = 9
		
	if pre_1 == 1 and pre_11 == 0:
		sre_1 = player1_wepon
	elif pre_11 == 1 and pre_1 == 0:
		sre_1 = player2_wepon
	else:
		sre_1 = " "
		
	if pre_2 == 2 and pre_22 == 0:
		sre_2 = player1_wepon
	elif pre_22 == 2 and pre_2 == 0:
		sre_2 = player2_wepon
	else:
		sre_2 = " "
		
	if pre_3 == 3 and pre_33 == 0:
		sre_3 = player1_wepon
	elif pre_33 == 3 and pre_3 == 0:
		sre_3 = player2_wepon
	else:
		sre_3 = " "
		
	if pre_4 == 4 and pre_44 == 0:
		sre_4 = player1_wepon
	elif pre_44 == 4 and pre_4 == 0:
		sre_4 = player2_wepon
	else:
		sre_4 = " "
		
	if pre_5 == 5 and pre_55 == 0:
		sre_5 = player1_wepon
	elif pre_55 == 5 and pre_5 == 0:
		sre_5 = player2_wepon
	else:
		sre_5 = " "
		
	if pre_6 == 6 and pre_66 == 0:
		sre_6 = player1_wepon
	elif pre_66 == 6 and pre_6 == 0:
		sre_6 = player2_wepon
	else:
		sre_6 = " "
		
	if pre_7 == 7 and pre_77 == 0:
		sre_7 = player1_wepon
	elif pre_77 == 7 and pre_7 == 0:
		sre_7 = player2_wepon
	else:
		sre_7 = " "
		
	if pre_8 == 8 and pre_88 == 0:
		sre_8 = player1_wepon
	elif pre_88 == 8 and pre_8 == 0:
		sre_8 = player2_wepon
	else:
		sre_8 = " "
		
	if pre_9 == 9 and pre_99 == 0:
		sre_9 = player1_wepon
	elif pre_99 == 9 and pre_9 == 0:
		sre_9 = player2_wepon
	else:
		sre_9 = " "
		
		
	print("\t  {} | {} | {} ".format(sre_1,sre_2,sre_3))	
	print("\t------------- ")
	print("\t  {} | {} | {} ".format(sre_4,sre_5,sre_6))	
	print("\t------------- ")
	print("\t  {} | {} | {} ".format(sre_7,sre_8,sre_9))
		
	
	return


intialize()
for n in range(0,9):
	alternate_player()
	prepare_check()
	if n == 8:
		print("\nThe game is a Tie")
		print_sceern()
		exit()
	win_loose()
