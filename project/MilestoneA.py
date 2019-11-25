#!/usr/bin/python3
'''MilestoneA.py
This runnable file will provide a representation of
answers to key questions about your project in CSE 415.

'''

# DO NOT EDIT THE BOILERPLATE PART OF THIS FILE HERE:

CATEGORIES=['Baroque Chess Agent','Wicked Problem Formulation and A* Search',\
  'Backgammon Agent that Learns','Hidden Markov Models: Algorithms and Applications']

class Partner():
  def __init__(self, lastname, firstname, uwnetid):
    self.uwnetid=uwnetid
    self.lastname=lastname
    self.firstname=firstname

  def __lt__(self, other):
    return (self.lastname+","+self.firstname).__lt__(other.lastname+","+other.firstname)

  def __str__(self):
    return self.lastname+", "+self.firstname+" ("+self.uwnetid+")"

class Who_and_what():
  def __init__(self, team, option, title, approach, workload_distribution, references):
    self.team=team
    self.option=option
    self.title=title
    self.approach = approach
    self.workload_distribution = workload_distribution
    self.references = references

  def report(self):
    rpt = 80*"#"+"\n"
    rpt += '''The Who and What for This Submission

Project in CSE 415, University of Washington, Autumn, 2019
Milestone A

Team:
'''
    team_sorted = sorted(self.team)
    # Note that the partner whose name comes first alphabetically
    # must do the turn-in.
    # The other partner(s) should NOT turn anything in.
    rpt += "    "+ str(team_sorted[0])+" (the partner who must turn in all files in Catalyst)\n"
    for p in team_sorted[1:]:
      rpt += "    "+str(p) + " (partner who should NOT turn anything in)\n\n"

    rpt += "Option: "+str(self.option)+"\n\n"
    rpt += "Title: "+self.title + "\n\n"
    rpt += "Approach: "+self.approach + "\n\n"
    rpt += "Workload Distribution: "+self.workload_distribution+"\n\n"
    rpt += "References: \n"
    for i in range(len(self.references)):
      rpt += "  Ref. "+str(i+1)+": "+self.references[i] + "\n"

    rpt += "\n\nThe information here indicates that the following file will need\n"+\
     "to be submitted (in addition to code and possible data files):\n"
    rpt += "    "+\
     {'1':"Baroque_Chess_Agent_Report",'2':"Wicked_Problem_Forulation_Report",\
      '3':"Backgammon_Agent_That_Learns_Report", '4':"Hidden_Markov_Models_Report"}\
        [self.option]+".pdf\n"

    rpt += "\n"+80*"#"+"\n"
    return rpt

# END OF BOILERPLATE.

# Change the following to represent your own information:

Yutong = Partner("Liu", "Yutong", "yliu21")
Tianqi = Partner("Fang", "Tianqi", "fang2018")
team = [Yutong, Tianqi]

OPTION = '1'
# Legal options are 1, 2, 4, and 4.

title = "A Blustering Baroque Chess Player"

approach = '''Our approach will be to first understand the rules of
the Baroque Chess in order to develop a move generator. Then we will
define a personality for the agent. Based on its personality, we will
program a static evaluation function to win competitions. Using functions
such as alpha-beta pruning and Zobrist hashing to optimize computations.
Finally, we might develop an alternative static evaluation functions.'''

workload_distribution = '''Same as the procedures of assignment 6, we will figure out the moving rules of Baroque Chess together.
Yutong will do the static evaluation function part,
and the Tianqi will do the optimizations of alpha-beta pruning and Zobrist hashing.
Finally, we will finish the introduce part together.'''


reference1 = '''Wikipedia article on Baroque Chess;
    URL: https://en.wikipedia.org/wiki/Baroque_chess (accessed Nov. 19, 2019)'''

reference2 = ''''Pure' Rules of Ultima (also known as 'Baroque Chess');
    URL: http://www.inference.org.uk/mackay/ultima/ultima.html (accessed Nov. 19, 2019)'''

our_submission = Who_and_what([Yutong, Tianqi], OPTION, title, approach, workload_distribution, [reference1, reference2])

# You can run this file from the command line by typing:
# python3 who_and_what.py

# Running this file by itself should produce a report that seems correct to you.
if __name__ == '__main__':
  print(our_submission.report())
