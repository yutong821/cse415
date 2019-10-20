from EightPuzzle import *


def h(s):
  count = 0
  goal_state = [[0,1,2],[3,4,5],[6,7,8]]
  listb = s.b
  for i in range(3):
    for j in range(3):
      if goal_state[i][j] != listb[i][j]:
        count = count + 1
  return count

