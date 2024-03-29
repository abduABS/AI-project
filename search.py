# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    startstate = problem.getStartState()
    stateSpace = util.Stack()
    stateSpace.push((startstate, []))
    expList = []

    while not stateSpace.isEmpty():
        currState, path = stateSpace.pop()
        if problem.isGoalState(currState):
            return path
        expList.append(currState)
        nextSteps = problem.getSuccessors(currState)

        for next in nextSteps:
            newCoord = next[0]
            if newCoord not in expList:
                newPath = path + [next[1]]
                stateSpace.push((newCoord, newPath))
    
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visited = {} #holds the visited nodes
    solution = [] #holds the solution to return
    queue = util.Queue()
    path = {} #holds the successor nodes

    start = problem.getStartState()
    if problem.isGoalState(start):
        return solution
    queue.push((start, 'None', 0))
    visited[start] = 'None'
    #print(visited)

    while not (queue.isEmpty()):
        edge = queue.pop()
        visited[edge[0]] = edge[1] #each cords corresponding dir
        if problem.isGoalState(edge[0]):
            child = edge[0]
            break

        for i in problem.getSuccessors(edge[0]):
            if i[0] not in visited.keys() and i[0] not in path.keys(): #keys are the child nodes in both dics
                path[i[0]] = edge[0]
                queue.push(i)

    while (child in path.keys()): #to trace the solution from path
        parent = path[child]
        solution.insert(0, visited[child])
        child = parent

    return solution
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    initial = problem.getStartState()
    state_space = util.PriorityQueue()
    state_space.push((initial, []) ,0)
    explored = []
    while not state_space.isEmpty():
        state, moves = state_space.pop()
        if problem.isGoalState(state):
            return moves
        if state not in explored:
            success = problem.getSuccessors(state)
            for s in success:
                coords = s[0]
                if coords not in explored:
                    dir = s[1]
                    Cost = moves + [dir]
                    state_space.push((coords, moves + [dir]), problem.getCostOfActions(Cost))
        explored.append(state)
    return moves
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    initial = problem.getStartState()
    state_space = util.PriorityQueue()
    state_space.push((initial, []), 0)
    explored = []
    while not state_space.isEmpty():
        state, moves = state_space.pop()
        if problem.isGoalState(state):
            return moves
        if state not in explored:
            success = problem.getSuccessors(state)
            for s in success:
                coords = s[0]
                if coords not in explored:
                    direction = s[1]
                    cost = moves + [direction]
                    state_space.push((coords, moves + [direction]), problem.getCostOfActions(cost) + heuristic(coords, problem))
            explored.append(state)
    return moves
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
