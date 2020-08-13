#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Sahana Sreeprakash
# email: sahanas@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def __init__(self, depth_limit):
        """constructs new searcher"""
        self.states = []
        self.num_tested = 0 
        self.depth_limit = depth_limit
        

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


    def should_add(self, state):
        """takes a State object called state and returns True if the called Searcher should add state to its list of untested states, and False otherwise."""
        if state == GOAL_TILES or self.depth_limit != -1 or state.creates_cycle() == True:
            return False               
        else:
            self.states += [state]
            return True
    
    def add_state(self, new_state):
        """that adds takes a single State object called new_state and adds it to the Searcher‘s list of untested states. This method should only require one line of code! It should not return a value."""
    
        self.states += [new_state]
    
    def add_states(self, new_states):
        """takes a list State objects called new_states, and that processes the elements of new_states one at a time"""
        for s in new_states:
            if self.depth_limit == -1 and s.creates_cycle() == False:
                self.add_state(new_states)
    
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s 

    def find_solution(self, init_state):
        self.states += [init_state]
        while len(self.states) > 0:
            self.num_tested += 1
            s = self.next_state()
            if s == GOAL_TILES:
                return s
            else:
                self.add_states(s.generate_successors())
        else: 
            return None


 



### Add your BFSearcher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    def next_state(self):
        """Rather than choosing at random from the list of untested states, this version of next_state should follow FIFO (first-in first-out) ordering – choosing the state that has been in the list the longest.
        """
        s = self.states[0]
        self.states.remove(s)
        return s
    

class DFSearcher(Searcher):
    def next_state(self):
        """objects that perform depth-first search (DFS) instead of random search. As discussed in class, DFS involves always choosing one the untested states that has the largest depth"""
        s = self.states[-1]
        self.states.remove(s)
        return s

class GreedySearcher(Searcher):
    def __init__(self, depth_limit, heuristic):
        """ constructor for a GreedySearcher object
            inputs:
             * depth_limit - the depth limit of the searcher
             * heuristic - a reference to the function that should be used 
             when computing the priority of a state
        """
        # add code that calls the superclass constructor
        Searcher.__init__(self, depth_limit)
        
        self.heuristic = heuristic
    
    def priority(self, state):
        return -1 * Board.num_misplaced()
    
    def add_state(self, state):
        self.states += [self.priority(state), state]
        

    def next_state(self):
        s = max(self.states)
        self.states.remove(s)
        return s[1]

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

def h1(state):
    """to find num misplaced tiles"""
    return num_misplaced(state) * -1

def h2(state):
    """ find num misplaced tiles and moves to get there"""
    return (self.num_misplaced + self.num_moves) * -1 


### Add your other heuristic functions here. ###




    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


### Add your AStarSeacher class definition below. ###

class AStarSearcher(GreedySearcher):
    def priority(self, state):
        return -1 * (self.heuristic(state) + self.num_moves)





if __name__ == "__main__":
    searcher1 = Searcher(-1)
    print(searcher1)
    searcher2 = Searcher(10)
    print(searcher2)

    b1 = Board('142358607')
    s1 = State(b1, None, 'init')  # initial state
    searcher1 = Searcher(-1)  # no depth limit
    searcher1.add_state(s1)
    searcher2 = Searcher(1)   # depth limit of 1 move!
    searcher1.add_state(s1)
    b2 = b1.copy()
    print(b2.move_blank('left'))

    s2 = State(b2, s1, 'left')
    print(searcher1.should_add(s2))

    print(searcher2.should_add(s2))

    b3 = b2.copy()
    print(b3.move_blank('right'))


    print('num3')
    b = Board('142358607')
    s = State(b, None, 'init')
    searcher = Searcher(-1)
    searcher.add_state(s)
    print(searcher.states)

    succ = s.generate_successors()
    print('succ =', succ)


    print('num4')
    b = Board('142358607')
    s = State(b, None, 'init')
    searcher = Searcher(-1)
    searcher.add_state(s)
    print(searcher.states)

    succ = s.generate_successors()
    print(succ)

    print('num6')
    b = Board('012345678')       # the goal state!
    s = State(b, None, 'init')   # start at the goal
    print(s)

    searcher = Searcher(-1)
    print(searcher)

    print(searcher.find_solution(s))

    print(searcher)



    # part IV
    print('####PARTIV###')
    b = Board('142358607')       
    s = State(b, None, 'init')
    print(s)

    bfs = BFSearcher(-1)
    bfs.add_state(s)
    print(bfs.next_state())

    succ = s.generate_successors()
    print(succ)

    bfs.add_states(succ)
    print(bfs.next_state())

    print('####DFS######')
    b = Board('142358607')       
    s = State(b, None, 'init')
    print(s)

    dfs = DFSearcher(-1)
    dfs.add_state(s)
    print(dfs.next_state())

    succ = s.generate_successors()
    print(succ)

    dfs.add_states(succ)
    print(dfs.next_state())

    print('####greedy and a###')
    b = Board('142358607')       
    s = State(b, None, 'init')
    g = GreedySearcher(-1, h1)

    g.add_state(s)
    print(g.states)

    succ = s.generate_successors()
    g.add_state(succ[0])
    print(g.states)

    g.add_state(succ[1])
    print(g.states)

    print(g.next_state())
    print(g.states)


    #5
    b = Board('142358607')       
    s = State(b, None, 'init')
    a = AStarSearcher(-1, h1)  # no depth limit, basic heuristic
    a.add_state(s)
    print(a.states)

    succ = s.generate_successors()
    a.add_state(succ[1])
    print(a.states) 
    print(a.next_state)
    print(a.states)




