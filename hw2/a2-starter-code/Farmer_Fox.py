'''Farmer_Fox.py
by Yutong Liu
UWNetID: yliu21
Student number: 

Assignment 2, in CSE 415, Autumn 2019.
 
This file contains my problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.
'''

# Put your formulation of the Farmer-Fox-Chicken-and-Grain problem here.
# Be sure your name, uwnetid, and 7-digit student number are given above in 
# the format shown.


PROBLEM_DESC=\
''' "A farmer needs to take a fox, chicken and sack of grain across a river using a small
boat. He can only take one of the three items in the boat with him at one time. The
fox must never be left alone with the chicken, and the chicken must never be left alone
with the grain. How can he get everything across the river?" '''


LEFT=0 # same idea for left side of river
RIGHT=1 # etc.
farmer = 0
fox = 1
chicken = 2
grain =3

class State():

  def __init__(self, d=None):
    if d==None: 
      d = {'passengers':[[0,0],[0,0],[0,0],[0,0]]
           'boat':LEFT,
           }
    self.d = d

  def __eq__(self,s2):
    for prop in ['passengers', 'boat']:
      if self.d[prop] != s2.d[prop]: return False
    return True

  def __str__(self):
    # Produces a textual description of a state.
    p = self.d['passengers']
    # left side
    txt = "\n Farmer on left:"+str(p[farmer][LEFT])+"\n"
    txt += " Fox on left:"+str(p[fox][LEFT])+"\n"
    txt += "   Chicken on right:"+str(p[chicken][LEFT])+"\n"
    txt += "   grain on right:"+str(p[grain][LEFT])+"\n"
    # right side
    txt = "\n Farmer on left:"+str(p[farmer][RIGHT])+"\n"
    txt += " Fox on left:"+str(p[fox][RIGHT])+"\n"
    txt += "   Chicken on right:"+str(p[chicken][RIGHT])+"\n"
    txt += "   grain on right:"+str(p[grain][RIGHT])+"\n"
    # boat
    side='left'
    if self.d['boat']==1: side='right'
    txt += " boat is on the "+side+".\n"
    return txt

  def __hash__(self):
    return (self.__str__()).__hash__()

  def copy(self):
    # Performs an appropriately deep copy of a state,
    # for use by operators in creating new states.
    news = State({})
    news.d['passengers']=[self.d['people'][F_F_C_G][:] for F_F_C_G in [farmer, fox, chicken,grain]]
    news.d['boat'] = self.d['boat']
    return news 

  def can_move(self,fa,fo,c,g):
    '''Tests whether it's legal to move the boat and take
     famer, fox, chicken, grain.'''
    side = self.d['boat'] # Where the boat is.
    p = self.d['people']

    # famer always exist
    if fa<1:
    	return False;

    # famer fox chicken grain > available_passengers
    if (p[famer][side] < fa) or (p[fox][side] < fo) or (p[chicken][side] <c) or (p[grain][side] <g):
    	return False

    # Fox and chicken, chicken and grain, cannot stay on the same side
    if fo == 1:
    	if (p[fox][side] == p[chicken][side]) and (p[chicken][side] != p[grain][side]) and (p[famer][side] == p[fox][side]):
    		return False
    	if (p[chicken][side] == p[grain][side]) and [p[chicken][side] != p[fox][side]] and (p[famer][side] == p[fox][side]):
    		return False
    if c == 1:
    	if (p[fox][side] == p[chicken][side]) and (p[chicken][side] != p[grain][side]) and (p[famer][side] == p[chicken][side]):
    		return False
    	if (p[chicken][side] == p[grain][side]) and [p[chicken][side] != p[fox][side]] and (p[famer][side] == p[chicken][side]):
    		return False
    if g == 1:
    	if (p[fox][side] == p[chicken][side]) and (p[chicken][side] != p[grain][side]) and (p[famer][side] == p[grain][side]):
    		return False
    	if (p[chicken][side] == p[grain][side]) and [p[chicken][side] != p[fox][side]] and (p[famer][side] == p[grain][side]):
    		return False
    return True


  def move(self,m,c):
    '''Assuming it's legal to make the move, this computes
     the new state resulting from moving the boat carrying
     m missionaries and c cannibals.'''
    news = self.copy()      # start with a deep copy.
    side = self.d['boat']         # where is the boat?
    p = news.d['people']          # get the array of arrays of people.
    p[M][side] = p[M][side]-m     # Remove people from the current side.
    p[C][side] = p[C][side]-c
    p[M][1-side] = p[M][1-side]+m # Add them at the other side.
    p[C][1-side] = p[C][1-side]+c
    news.d['boat'] = 1-side       # Move the boat itself.
    return news

def goal_test(s):
  '''If all Ms and Cs are on the right, then s is a goal state.'''
  p = s.d['people']
  return (p[M][RIGHT]==3 and p[C][RIGHT]==3)

def goal_message(s):
  return "Congratulations on successfully guiding the missionaries and cannibals across the river!"

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)
#</COMMON_CODE>

#<INITIAL_STATE>
CREATE_INITIAL_STATE = lambda : State(d={'people':[[3, 0], [3, 0]], 'boat':LEFT })
#</INITIAL_STATE>

#<OPERATORS>
MC_combinations = [(1,0),(2,0),(3,0),(1,1),(2,1)]

OPERATORS = [Operator(
  "Cross the river with "+str(m)+" missionaries and "+str(c)+" cannibals",
  lambda s, m1=m, c1=c: s.can_move(m1,c1),
  lambda s, m1=m, c1=c: s.move(m1,c1) ) 
  for (m,c) in MC_combinations]
#</OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>
