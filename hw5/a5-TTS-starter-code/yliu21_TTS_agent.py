
# Name:Yutong Liu
# Date: 11/08/2019
# Toro-Tile-Straight Agent



from TTS_State import TTS_State
import time

USE_CUSTOM_STATIC_EVAL_FUNCTION = False

class MY_TTS_State(TTS_State):
    def static_eval(self):
        if USE_CUSTOM_STATIC_EVAL_FUNCTION:
          return self.custom_static_eval()
        else:
          return self.basic_static_eval()

    # def basic_static_eval(self):
    #   raise Exception("basic_static_eval not yet implemented.")

    # def custom_static_eval(self):
    #   raise Exception("custom_static_eval not yet implemented.")


    def basic_static_eval(self):
        # get current state
        current_s = self.board
        row = len(current_s)
        column = len(current_s[0])

        # initial TWF and TBF
        TWF = 0
        TBF = 0

        for i in range(row):
            for j in range(column):

                if current_s[i][j] == '-':
                    continue

                if current_s[i][j] == "W":
                    neighboos = self.neighbors_location(i, j)
                    TWF = TWF + self.reward(neighboos)

                if current_s[i][j] == "B":
                    neighboos = self.neighbors_location(i, j)
                    TBF = TBF + self.reward(neighboos)
        score = TWF - TBF
        return score

    def neighbors_location(self, i, j):
        current_s = self.board
        row = len(current_s)
        column = len(current_s[0])
        direction = [None]*8
        if i == 0:
            if j == 0:
                direction[0] = [row, column]
            else:
                direction[0] = [row, j - 1]
        elif i == row:
            if j == 0:
                direction[0] = [i-1, column]
            else:
                direction[0] = [i-1, j -1]
        else:
            direction[0] = [i-1, j-1]

        # dir 2
        if i == 0:
            direction[1] = [row, j]
        else:
            direction[1] = [i-1, j]

        # dir 3
        if i == 0:
            if j == column:
                direction[2] = [row, 0]
            else:
                direction[2] = [row, j+1]
        elif i == row:
            if j == column:
                direction[2] = [i-1, j]
            else:
                direction[2] = [i-1, j+1]
        else:
            direction[2] = [i-1, j+1]

        # dir 4
        if j == 0:
            direction[3] = [i, column]
        else:
            direction[3] = [i, j-1]


        # dir 5
        if j == column:
            direction[4] = [i, 0]
        else:
            direction[4] = [i, j+1]

        # dir 6
        if i == row:
            if j == 0:
                direction[5] = [0, column]
            else:
                direction[5] = [0, j-1]
        elif i == 0:
            if j == 0:
                direction[5] = [i+1, column]
            else:
                direction[5] = [i+1, j-1]

        else:
            direction[5] = [i+1, j-1]

        # dir 7
        if i == row:
            direction[6] = [0, j]
        else:
            direction[6] = [i+1, j]

        # dir8
        if i == row:
            if j == column:
                direction[7] = [0, 0]
            else:
                direction[7] = [0, j+1]
        elif i == 0:
            if j == column:
                direction[7] = [i+1, 0]
            else:
                direction[7] = [i+1, j+1]
        else:
            direction[7] = [i+1, j+1]

        return direction


    def reward(self, direction):
        current_s = self.board
        count = 0
        for i in direction:
            if current_s[i[0]][i[1]] == " ":
                count = count + 1
        return count

    def custom_static_eval(self):
        score = 0
        return score

# The following is a skeleton for the function called parameterized_minimax,
# which should be a top-level function in each agent file.
# A tester or an autograder may do something like
# import ABC_TTS_agent as player, call get_ready(),
# and then it will be able to call tryout using something like this:
# results = player.parameterized_minimax(**kwargs)


def parameterized_minimax(
       current_state=None,
       max_ply=2,
       use_alpha_beta=False,
       use_basic_static_eval=False):

  # All students, add code to replace these default
  # values with correct values from your agent (either here or below).
    DATA = {}
    DATA['CURRENT_STATE_STATIC_VAL'] = -1000.0
    DATA['N_STATES_EXPANDED'] = 0
    DATA['N_STATIC_EVALS'] = 0
    DATA['N_CUTOFFS'] = 0


    if use_basic_static_eval:
        DATA['CURRENT_STATE_STATIC_VAL'] = MY_TTS_State(current_state.board).basic_static_eval()

    if use_alpha_beta:
        output = alpha_beta(use_alpha_beta, current_state, max_ply, alpha=-10000, beta=10000, DATA=DATA)
    else:
        output = alpha_beta(use_alpha_beta, current_state, max_ply, alpha=-10000, beta=10000, DATA=DATA)

    DATA['CURRENT_STATE_STATIC_VAL'] = output


  # STUDENTS: You may create the rest of the body of this function here.


  # Actually return all results...
    return(DATA)

def alpha_beta(use_alpha_beta, current_state, max_ply, alpha, beta, DATA):

    if max_ply == 0:
        DATA['N_STATIC_EVALS'] += 1
        return MY_TTS_State(current_state.board).basic_static_eval()

    ww = 0
    bb = 0

    current_board = current_state.copy().board
    for i in range(len(current_board)):
      for j in range(len(current_board[0])):
            if current_board[i][j] == "W":
                ww += 1
            elif current_board[i][j] == "B":
                bb += 1

    if ww > bb:
        current_state.whose_turn = "B"
    else:
        current_state.whose_turn = "W"

    successors = []
    next_va = _find_next_vacancy(current_state.board)
    van = []
    stored_state1= current_state.copy()

    while next_va != False:
        van.append(next_va)
        stored_state1.board[next_va[0]][next_va[1]] = stored_state1.whose_turn
        next_va = _find_next_vacancy(stored_state1.board)

    for loc in van:
        new_state = current_state.copy()
        new_state.board[loc[0]][loc[1]] = new_state.whose_turn
        new_state.whose_turn = switch_player(new_state)
        # print(new_state)
        successors.append(new_state)

    DATA['N_STATES_EXPANDED'] +=1
    for s in successors:
        if s.whose_turn == "W":
            v = -10000
            if use_alpha_beta:
                v = max(v, alpha_beta(use_alpha_beta,s, max_ply-1, alpha, beta, DATA))
                alpha = max(alpha, v)
                if alpha >= beta:
                    DATA['N_CUTOFFS'] += 1
                    break
            else:
                new_val = alpha_beta(use_alpha_beta,s, max_ply-1, alpha, beta, DATA)
                if new_val > v:
                    v = new_val
        else:
            v = 10000
            if use_alpha_beta:
                v = min(v, alpha_beta(use_alpha_beta,s, max_ply-1, alpha, beta, DATA))
                beta = min(beta, v)
                if alpha >= beta:
                    DATA['N_CUTOFFS'] += 1
                    break
            else:
                new_val = alpha_beta(use_alpha_beta,s, max_ply-1, alpha, beta, DATA)
                if new_val < v:
                    v = new_val
    return v


def switch_player(current_state):
    if current_state.whose_turn == "W":
        return "B"
    return "W"



def take_turn(current_state, last_utterance, time_limit):

    # Compute the new state for a move.
    # Start by copying the current state.
    new_state = MY_TTS_State(current_state.board)
    # Fix up whose turn it will be.
    who = current_state.whose_turn
    new_who = 'B'
    if who=='B': new_who = 'W'
    new_state.whose_turn = new_who

    # Place a new tile
    location = _find_next_vacancy(new_state.board)
    if location==False: return [[False, current_state], "I don't have any moves!"]
    new_state.board[location[0]][location[1]] = who

    # Construct a representation of the move that goes from the
    # currentState to the newState.
    move = location

    # Make up a new remark
    new_utterance = "I'll think harder in some future game. Here's my move"

    return [[move, new_state], new_utterance]


def _find_next_vacancy(b):
    for i in range(len(b)):
      for j in range(len(b[0])):
        if b[i][j]==' ': return (i,j)
    return False

def moniker():
    return "JaneDou" # Return your agent's short nickname here.

def who_am_i():
    return """My name is YL, created by Yutong.
 I consider myself to be an aggressive line-blocker."""

def get_ready(initial_state, k, who_i_play, player2Nickname):
    # do any prep, like eval pre-calculation, here.

    return "OK"




