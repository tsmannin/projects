###
# Tristan Manning
# CSE 140
# 10/25/20
###

import numpy as np

class AIPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'ai'
        self.player_string = 'Player {}:ai'.format(player_number)

    def get_alpha_beta_move(self, board):

		def check_win_condition(board, player_num):
			player_win_str = '{0}{0}{0}{0}'.format(player_num)
			to_str = lambda a: ''.join(a.astype(str))
			
			for row in board:
				if player_win_str in to_str(row):
					return True
			for row in board.T:
				if player_win_str in to_str(row):
					return True

			for op in [None, np.fliplr]:
				op_board = op(board) if op else board
                
				root_diag = np.diagonal(op_board, offset=0).astype(np.int)
				if player_win_str in to_str(root_diag):
					return True

				for i in range(1, board.shape[1]-3):
  					for offset in [i, -i]:
						diag = np.diagonal(op_board, offset=offset)
						diag = to_str(diag.astype(np.int))
						if player_win_str in diag:
							return True
			return False


		def alpha_beta_search(self, board, player_number):
			value = max_value(board, 0, player_number, np.NINF, np.Inf)
			return value


		def max_value(board, depth, player_number, alpha, beta):
			if check_win_condition(board, player_number) == True:
				return 999999999
			if check_win_condition(board, (2/player_number)) == True:
				return 555555555
			if depth == 5:
				return self.evaluation_function(board)

			v = np.NINF
			for move in range(7):
				c_board = board.copy()
				valid = update(c_board, move, player_number)
				if valid[0] == True:							# valid[0] = boolean for valid/invalid move, valid[1] = updated/non-updated board
					v2 = min_value(valid[1], (depth+1), (2/player_number), alpha, beta)
					if v2 > v:
						v = v2
						alpha = max(alpha, v)
					if v >= beta:
						return v
			return v


		def min_value(board, depth, player_number, alpha, beta):
			if check_win_condition(board, player_number) == True:
				return 999999999
			if check_win_condition(board, (2/player_number)) == True:
				return 555555555
			if depth == 5:
				return self.evaluation_function(board)

			v = np.Inf
			for move in range(7):
				c_board = board.copy()
				temp_board = update(c_board, move, player_number)
				if temp_board[0] == True:
					v2 = max_value(valid[1], (depth+1), (2/player_number), alpha, beta)
					if v2 < v:
						v = v2
						beta = min(beta, v)
					if v <= alpha:
						return v
			return v


		def update(board, move, player_num):			
			if 0 in board[:,move]:
			    update_row = -1
			    for row in range(1, board.shape[0]):
			        update_row = -1
			        if board[row, move] > 0 and board[row-1, move] == 0:
			            update_row = row-1
			        elif row==board.shape[0]-1 and board[row, move] == 0:
			            update_row = row

			        if update_row >= 0:
			            board[update_row, move] = player_num
                       	return True, board
			
			return False


        # raise NotImplementedError('Whoops I don\'t know what to do')
	
		player_num = self.player_number
		optimal = 0
		best_value = 0

		for move in range (7):	
			copy_board = board.copy()
			valid = update(copy_board, move, player_num)
			if valid[0] == True:	
				utility = alpha_beta_search(self, valid[1], player_num)
				if utility > best_value:
					best_value = utility
					optimal = move

		return optimal
		"""
        Given the current state of the board, return the next move based on
        the alpha-beta pruning algorithm

        This will play against either itself or a human player

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        # raise NotImplementedError('Whoops I don\'t know what to do')

    def get_expectimax_move(self, board):

		def check_win_condition(board, player_num):
			player_win_str = '{0}{0}{0}{0}'.format(player_num)
			to_str = lambda a: ''.join(a.astype(str))
			
			for row in board:
				if player_win_str in to_str(row):
					return True
			for row in board.T:
				if player_win_str in to_str(row):
					return True

			for op in [None, np.fliplr]:
				op_board = op(board) if op else board
                
				root_diag = np.diagonal(op_board, offset=0).astype(np.int)
				if player_win_str in to_str(root_diag):
					return True

				for i in range(1, board.shape[1]-3):
  					for offset in [i, -i]:
						diag = np.diagonal(op_board, offset=offset)
						diag = to_str(diag.astype(np.int))
						if player_win_str in diag:
							return True
			return False


		def value(self, board, depth, player_number):
			if check_win_condition(board, player_number) == True:
				return 999999999
			if depth == 3:
				return self.evaluation_function(board)	
			if player_num == 1:
				return max_value(board, depth)
			if player_num == 2:
				return exp_value(board, depth)


		def max_value(board, depth):
			v = np.NINF
			for move in range(7):
				c_board = board.copy()
				valid = update(c_board, move, 1)
				if valid[0] == True:							# valid[0] = boolean for valid/invalid move, valid[1] = updated/non-updated board
					v = max(v, value(self, valid[1], (depth+1), (2/self.player_number)))
			return v


		def exp_value(board, depth):
			v = 0
			for move in range(7):
				c_board = board.copy()
				temp_board = update(c_board, move, 2)
				if temp_board[0] == True:
					v += (1/7) * value(self, temp_board[1], (depth+1), (2/self.player_number))
			return v


		def update(board, move, player_num):			
			if 0 in board[:,move]:
			    update_row = -1
			    for row in range(1, board.shape[0]):
			        update_row = -1
			        if board[row, move] > 0 and board[row-1, move] == 0:
			            update_row = row-1
			        elif row==board.shape[0]-1 and board[row, move] == 0:
			            update_row = row

			        if update_row >= 0:
			            board[update_row, move] = player_num
                       	return True, board
			
			return False


        # raise NotImplementedError('Whoops I don\'t know what to do')
	
		player_num = self.player_number
		optimal = 0
		best_value = 0

		for move in range (7):	
			copy_board = board.copy()
			valid = update(copy_board, move, player_num)
			if valid[0] == True:	
				utility = value(self, valid[1], 0, player_num)
				if utility > best_value:
					best_value = utility
					optimal = move

		return optimal


		"""
        Given the current state of the board, return the next move based on
        the expectimax algorithm.

        This will play against the random player, who chooses any valid move
        with equal probability

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """


    def evaluation_function(self, board):
		player_score = 0
		current_player = self.player_number
		opponent_player = int(2 / current_player)

		# calculate score for current player, add to total score
		player_4_str = '{0}{0}{0}{0}'.format(current_player)
		player_3_str = '{0}{0}{0}'.format(current_player)
		player_2_str = '{0}{0}'.format(current_player)
		player_1_str = '{0}'.format(current_player)
		to_str = lambda a: ''.join(a.astype(str))

		# check_horizontal(b):
		for row in board:
			if player_4_str in to_str(row):
				player_score += 100000
			elif player_3_str in to_str(row):
				player_score += 50
			elif player_2_str in to_str(row):
				player_score += 5
			elif player_1_str in to_str(row):
				player_score += 1

		# check_verticle(b):
		for col in board.T:
			if player_4_str in to_str(col):
				player_score += 100000
			elif player_3_str in to_str(col):
				player_score += 50
			elif player_2_str in to_str(col):
				player_score += 5
			elif player_1_str in to_str(col):
				player_score += 1

		# check_diagonal(board):
		for op in [None, np.fliplr]:
			op_board = op(board) if op else board
            
			root_diag = np.diagonal(op_board, offset=0).astype(np.int)
			if player_4_str in to_str(root_diag):
				player_score += 100000
			elif player_3_str in to_str(root_diag):
				player_score += 40
			elif player_2_str in to_str(root_diag):
				player_score += 3
			elif player_1_str in to_str(root_diag):
				player_score += 1

			for i in range(1, board.shape[1]-3):
				for offset in [i, -i]:
					diag = np.diagonal(op_board, offset=offset)
					diag = to_str(diag.astype(np.int))
					if player_4_str in diag:
						player_score += 100000
					elif player_3_str in diag:
						player_score += 40
					elif player_2_str in diag:
						player_score += 3
					elif player_1_str in diag:
						player_score += 1



		# calculate score for other player, subtract from total score
		player_4_str = '{0}{0}{0}{0}'.format(opponent_player)
		player_3_str = '{0}{0}{0}'.format(opponent_player)
		player_2_str = '{0}{0}'.format(opponent_player)
		player_1_str = '{0}'.format(opponent_player)
		to_str = lambda a: ''.join(a.astype(str))

		# check_horizontal(b):
		for row in board:
			if player_4_str in to_str(row):
				player_score -= 10000
			elif player_3_str in to_str(row):
				player_score -= 25
			elif player_2_str in to_str(row):
				player_score -= 3
			elif player_1_str in to_str(row):
				player_score -= 1

		# check_verticle(b):
		for col in board.T:
			if player_4_str in to_str(col):
				player_score -= 10000
			elif player_3_str in to_str(col):
				player_score -= 30
			elif player_2_str in to_str(col):
				player_score -= 3
			elif player_1_str in to_str(col):
				player_score -= 1

		# check_diagonal(b):
		for op in [None, np.fliplr]:
			op_board = op(board) if op else board
            
			root_diag = np.diagonal(op_board, offset=0).astype(np.int)
			if player_4_str in to_str(root_diag):
				player_score -= 10000
			elif player_3_str in to_str(root_diag):
				player_score -= 25
			elif player_2_str in to_str(root_diag):
				player_score -= 3
			elif player_1_str in to_str(root_diag):
				player_score -= 1

			for i in range(1, board.shape[1]-3):
				for offset in [i, -i]:
					diag = np.diagonal(op_board, offset=offset)
					diag = to_str(diag.astype(np.int))
					if player_4_str in diag:
						player_score -= 10000
					elif player_3_str in diag:
						player_score -= 25
					elif player_2_str in diag:
						player_score -= 3
					elif player_1_str in diag:
						player_score -= 1       	

		return player_score
		
		"""
        Given the current state of the board, return the scalar value that 
        represents the evaluation function for the current player
       
        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in thpipem
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The utility value for the current board
        """

class RandomPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'random'
        self.player_string = 'Player {}:random'.format(player_number)

    def get_move(self, board):
        """
        Given the current board state select a random column from the available
        valid moves.

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        valid_cols = []
        for col in range(board.shape[1]):
            if 0 in board[:,col]:
                valid_cols.append(col)

        return np.random.choice(valid_cols)


class HumanPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'human'
        self.player_string = 'Player {}:human'.format(player_number)

    def get_move(self, board):
        """
        Given the current board state returns the human input for next move

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """

        valid_cols = []
        for i, col in enumerate(board.T):
            if 0 in col:
                valid_cols.append(i)

        move = int(input('Enter your move: '))

        while move not in valid_cols:
            print('Column full, choose from:{}'.format(valid_cols))
            move = int(input('Enter your move: '))

        return move

