import random

class Player81:
	
	def __init__(self):
		pass

	def move(self,temp_board,temp_block,old_move,flag):
		for_corner = [0,2,3,5,6,8]

		blocks_allowed  = []

		if old_move[0] in for_corner and old_move[1] in for_corner:

			if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
				blocks_allowed = [0, 1, 3]
			elif old_move[0] % 3 == 0 and old_move[1] in [2, 5, 8]:
				blocks_allowed = [1,2,5]
			elif old_move[0] in [2,5, 8] and old_move[1] % 3 == 0:
				blocks_allowed  = [3,6,7]
			elif old_move[0] in [2,5,8] and old_move[1] in [2,5,8]:
				blocks_allowed = [5,7,8]
			else:
				print "SOMETHING REALLY WEIRD HAPPENED!"
				sys.exit(1)
		else:
			if old_move[0] % 3 == 0 and old_move[1] in [1,4,7]:
				blocks_allowed = [1]
	
			elif old_move[0] in [1,4,7] and old_move[1] % 3 == 0:
				blocks_allowed = [3]
		
			elif old_move[0] in [2,5,8] and old_move[1] in [1,4,7]:
				blocks_allowed = [7]

			elif old_move[0] in [1,4,7] and old_move[1] in [2,5,8]:
				blocks_allowed = [5]
			elif old_move[0] in [1,4,7] and old_move[1] in [1,4,7]:
				blocks_allowed = [4]
                for i in reversed(blocks_allowed):
                    if temp_block[i] != '-':
                        blocks_allowed.remove(i)
		cells = self.get_empty_out_of(temp_board, blocks_allowed,temp_block)
		send_it = []
		for each in temp_board:
			send_it.append(each[:])
		send_it2 = temp_block[:]
		cmon = old_move[:]
		check_it = []
		count_empty = 0
		if len(cells) == 1:
			return cells[0]
		elif len(cells) < 4:
			x = self.alphabeta(send_it, send_it2, cmon, flag, 5, -1000000, 1000000, 1, check_it, flag, 5)
		else:
			x = self.alphabeta(send_it, send_it2, cmon, flag, 4, -1000000, 1000000, 1, check_it, flag, 4)
		return_val = 0
	
		random_selection = []
		if check_it != []:
			for j in range(len(check_it)):
				if check_it[j] == x:
					random_selection.append(j)
			return_val = random_selection[random.randrange(len(random_selection))]
		else:
			return_val = 40
		return cells[return_val]

	def heuristic(self,game_board, game_block, my_move):
		if my_move == 'o':
			not_my_move = 'x'
		elif my_move == 'x':
			not_my_move = 'o'
		total_val = []
		count_my_move = 0
		count_not_my_move = 0
		for i in range(len(game_block)):
			if game_block[i] == '-':
				id1 = i/3
				id2 = i%3
				add = 0
				count_my_move = 0
				count_not_my_move = 0
				for j in range(id1*3, id1*3 + 3):
					count_my_move = 0
					count_not_my_move = 0
					for k in range(id2*3, id2*3 + 3):
						if game_board[j][k] == my_move:
							count_my_move += 1
						elif game_board[j][k] == not_my_move:
							count_not_my_move += 1
					if count_not_my_move == 0 and count_my_move != 0:
						add = add + pow(10, count_my_move)
					elif count_my_move == 0 and count_not_my_move != 0:
						add = add + pow(10, count_not_my_move)
					else:
						add = add + pow(10, count_my_move) - pow(10, count_not_my_move)
				for j in range(id2*3, id2*3 + 3):
					count_my_move = 0
					count_not_my_move = 0
					for k in range(id1*3, id1*3 + 3):
						if game_board[k][j] == my_move:
							count_my_move += 1
						elif game_board[k][j] == not_my_move:
							count_not_my_move += 1
					if count_not_my_move == 0 and count_my_move != 0:
						add = add + pow(10, count_my_move)
					elif count_my_move == 0 and count_not_my_move != 0:
						add = add + pow(10, count_not_my_move)
					else:
						add = add + pow(10, count_my_move) - pow(10, count_not_my_move)
				count_my_move = 0
				count_not_my_move = 0
				for j in range(0, 3):
					if game_board[id1*3 + j][id2*3 + j] == my_move:
						count_my_move += 1
					elif game_board[id1*3 + j][id2*3 + j] == not_my_move:
						count_not_my_move += 1
				if count_not_my_move == 0 and count_my_move != 0:
					add = add + pow(10, count_my_move)
				elif count_my_move == 0 and count_not_my_move != 0:
					add = add + pow(10, count_not_my_move)
				else:
					add = add + pow(10, count_my_move) - pow(10, count_not_my_move)
				count_my_move = 0
				count_not_my_move = 0
				for j in range(0, 3):
					if game_board[id1*3 + j][id2*3 + (2 - j)] == my_move:
						count_my_move += 1
					elif game_board[id2*3 + j][id2*3 + (2 - j)] == not_my_move:
						count_not_my_move += 1
				if count_not_my_move == 0 and count_my_move != 0:
					add = add + pow(10, count_my_move)
				elif count_my_move == 0 and count_not_my_move != 0:
					add = add + pow(10, count_not_my_move)
				else:
					add = add + pow(10, count_my_move) - pow(10, count_not_my_move)
				total_val.append(add)	
			elif game_block[i] == my_move:
				total_val.append(1000)
			elif game_block[i] == not_my_move:
				total_val.append(-1000)
			else:
				total_val.append(0)
		total = 0
		count_my_move = 0
		count_not_my_move = 0
		temp_sum = 0
		for i in range(0, 3):
			for j in range(0, 3):
				if total_val[(i*3) + j] == 1000:
					count_my_move += 1
				elif total_val[(i*3) + j] == -1000:
					count_not_my_move += 1
				else:
					temp_sum += total_val[(i*3) + j]
			if count_not_my_move == 0 and count_my_move != 0:
				total = total + pow(1000, count_my_move) + temp_sum
			elif count_not_my_move != 0 and count_my_move == 0:
				total = total - pow(1000, count_not_my_move) + temp_sum
			else:
				total = total + pow(1000, count_my_move) - pow(1000, count_not_my_move) + temp_sum
		count_my_move = 0
		count_not_my_move = 0
		temp_sum = 0
		for i in range(0, 3):
			for j in range(0, 3):
				if total_val[(j*3) + i] == 1000:
					count_my_move += 1
				elif total_val[(j*3) + i] == -1000:
					count_not_my_move += 1
				else:
					temp_sum += total_val[(j*3) + i]
			if count_not_my_move == 0 and count_my_move != 0:
				total = total + pow(1000, count_my_move) + temp_sum
			elif count_not_my_move != 0 and count_my_move == 0:
				total = total - pow(1000, count_not_my_move) + temp_sum
			else:
				total = total + pow(1000, count_my_move) - pow(1000, count_not_my_move) + temp_sum
		count_my_move = 0
		count_not_my_move = 0
		temp_sum = 0			
		for i in range(0, 3):
			if total_val[(i*3) + i] == 1000:
				count_my_move += 1
			elif total_val[(i*3) + i] == -1000:
				count_not_my_move += 1
			else:
				temp_sum += total_val[(i*3) + i]
		if count_not_my_move == 0 and count_my_move != 0:
			total = total + pow(1000, count_my_move) + temp_sum
		elif count_not_my_move != 0 and count_my_move == 0:
			total = total - pow(1000, count_not_my_move) + temp_sum
		else:
			total = total + pow(1000, count_my_move) - pow(1000, count_not_my_move) + temp_sum
		count_my_move = 0
		count_not_my_move = 0
		temp_sum = 0
		for i in range(0, 3):
			if total_val[(i*3) + (2 - i)] == 1000:
				count_my_move += 1
			elif total_val[(i*3) + (2 - i)] == -1000:
				count_not_my_move += 1
			else:
				temp_sum += total_val[(i*3) + (2 - i)]
		if count_not_my_move == 0 and count_my_move != 0:
			total = total + pow(1000, count_my_move) + temp_sum
		elif count_not_my_move != 0 and count_my_move == 0:
			total = total - pow(1000, count_not_my_move) + temp_sum
		else:
			total = total + pow(1000, count_my_move) - pow(1000, count_not_my_move) + temp_sum

		return total
				
		
	def alphabeta(self, temp_board, temp_block, old_move, flag, depth, alpha, beta, maximizingPlayer, check_it, my_move, depth_limit):
		if flag == 'o':
			send_it = 'x'
		elif flag == 'x':
			send_it = 'o'
		cells = self.moveit(temp_board, temp_block, old_move, flag)
		if len(cells) == 81:
			return 1
		if depth == 0 or self.terminal_state_reached(temp_board, temp_block) == 1:
			return self.heuristic(temp_board, temp_block, my_move)
		if maximizingPlayer == 1:
			v = -1000000
			for each in cells:
				temp_save_board = []
				for every in temp_board:
					temp_save_board.append(every[:])
				temp_save_block = temp_block[:]
				self.update_lists(temp_save_board, temp_save_block, each, flag)
				v = max(v, self.alphabeta(temp_save_board, temp_save_block, each, send_it, depth - 1, alpha, beta, 0, check_it, my_move, depth_limit))
				alpha = max(v, alpha)
				if depth == depth_limit:
					check_it.append(v)
				if beta <= alpha:
					break
			return v
		if maximizingPlayer == 0:
			v = 1000000
			for each in cells:
				temp_save_board = []
				for every in temp_board:
					temp_save_board.append(every[:])
				temp_save_block = temp_block[:]
				self.update_lists(temp_save_board, temp_save_block, each, flag)
				v = min(v, self.alphabeta(temp_save_board, temp_save_block, each, send_it, depth - 1, alpha, beta, 1, check_it, my_move, depth_limit))
				beta = min(beta, v)
				if beta <= alpha:
					break
			return v
			
	def moveit(self, temp_board,temp_block,old_move,flag):
		for_corner = [0,2,3,5,6,8]

		blocks_allowed  = []

		if old_move[0] in for_corner and old_move[1] in for_corner:

			if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
				blocks_allowed = [0, 1, 3]
			elif old_move[0] % 3 == 0 and old_move[1] in [2, 5, 8]:
				blocks_allowed = [1,2,5]
			elif old_move[0] in [2,5, 8] and old_move[1] % 3 == 0:
				blocks_allowed  = [3,6,7]
			elif old_move[0] in [2,5,8] and old_move[1] in [2,5,8]:
				blocks_allowed = [5,7,8]
			else:
				print "SOMETHING REALLY WEIRD HAPPENED!"
				sys.exit(1)
		else:
			if old_move[0] % 3 == 0 and old_move[1] in [1,4,7]:
				blocks_allowed = [1]
		
			elif old_move[0] in [1,4,7] and old_move[1] % 3 == 0:
				blocks_allowed = [3]
			
			elif old_move[0] in [2,5,8] and old_move[1] in [1,4,7]:
				blocks_allowed = [7]

			elif old_move[0] in [1,4,7] and old_move[1] in [2,5,8]:
				blocks_allowed = [5]
			elif old_move[0] in [1,4,7] and old_move[1] in [1,4,7]:
				blocks_allowed = [4]
		for i in reversed(blocks_allowed):
			if temp_block[i] != '-':
				blocks_allowed.remove(i)
		cells = self.get_empty_out_of(temp_board, blocks_allowed, temp_block)
		return cells

	def terminal_state_reached(self, game_board, block_stat):
		
		bs = block_stat
		if (bs[0] == bs[1] and bs[1] == bs[2] and bs[1]!='-' and bs[1]!='d') or (bs[3]!='d' and bs[3]!='-' and bs[3] == bs[4] and bs[4] == bs[5]) or (bs[6]!='d' and bs[6]!='-' and bs[6] == bs[7] and bs[7] == bs[8]):
			return 1
		elif (bs[0]!='d' and bs[0] == bs[3] and bs[3] == bs[6] and bs[0]!='-') or (bs[1]!='d'and bs[1] == bs[4] and bs[4] == bs[7] and bs[4]!='-') or (bs[2]!='d' and bs[2] == bs[5] and bs[5] == bs[8] and bs[5]!='-'):
			return 1
		elif (bs[0] == bs[4] and bs[4] == bs[8] and bs[0]!='-' and bs[0]!='d') or (bs[2] == bs[4] and bs[4] == bs[6] and bs[2]!='-' and bs[2]!='d'):
			return 1
		else:
			return 0

	def update_lists(self, game_board, block_stat, move_ret, fl):
		game_board[move_ret[0]][move_ret[1]] = fl

		block_no = (move_ret[0]/3)*3 + move_ret[1]/3
		id1 = block_no/3
		id2 = block_no%3
		mg = 0
		mflg = 0
		if block_stat[block_no] == '-':
			if game_board[id1*3][id2*3] == game_board[id1*3+1][id2*3+1] and game_board[id1*3+1][id2*3+1] == game_board[id1*3+2][id2*3+2] and game_board[id1*3+1][id2*3+1] != '-':
				mflg=1
			if game_board[id1*3+2][id2*3] == game_board[id1*3+1][id2*3+1] and game_board[id1*3+1][id2*3+1] == game_board[id1*3][id2*3 + 2] and game_board[id1*3+1][id2*3+1] != '-':
				mflg=1
			
			if mflg != 1:
			    for i in range(id2*3,id2*3+3):
				if game_board[id1*3][i]==game_board[id1*3+1][i] and game_board[id1*3+1][i] == game_board[id1*3+2][i] and game_board[id1*3][i] != '-':
					mflg = 1
					break

			if mflg != 1:
			    for i in range(id1*3,id1*3+3):
				if game_board[i][id2*3]==game_board[i][id2*3+1] and game_board[i][id2*3+1] == game_board[i][id2*3+2] and game_board[i][id2*3] != '-':
					mflg = 1
					break

		
		if mflg == 1:
			block_stat[block_no] = fl
		

		id1 = block_no/3
		id2 = block_no%3
		cells = []
		for i in range(id1*3,id1*3+3):
		    for j in range(id2*3,id2*3+3):
			if game_board[i][j] == '-':
			    cells.append((i,j))

		if cells == [] and mflg!=1:
		    block_stat[block_no] = 'd'
		
		return

	def get_empty_out_of(self, gameb, blal,block_stat):
		cells = []
		for idb in blal:
			id1 = idb/3
			id2 = idb%3
			for i in range(id1*3,id1*3+3):
				for j in range(id2*3,id2*3+3):
					if gameb[i][j] == '-':
						cells.append((i,j))

		if cells == []:
			for i in range(9):
				for j in range(9):
					no = (i/3)*3
					no += (j/3)
					if gameb[i][j] == '-' and block_stat[no] == '-':
						cells.append((i,j))	
		return cells



