from typing import Callable
import numpy as np 

from adversarialsearchproblem import (
    Action,
    AdversarialSearchProblem,
    State as GameState,
)

"""
    Implement the minimax algorithm on ASPs, assuming that the given game is
    both 2-player and constant-sum.
    Input:
        asp - an AdversarialSearchProblem
    Output:
        an action (an element of asp.get_available_actions(asp.get_start_state()))
    """
def minimax(asp: AdversarialSearchProblem[GameState, Action]) -> Action:
    """
    important functions
    asp
        get_start_state()
        transition(state, action)
        is_terminal_state(state) = is terminal
        evaluate_terminal(state) = utility
        get_available_actions(state) = actions
    state
        player_to_move()
    """
    start_state = asp.get_start_state() 
    player = start_state.player_to_move()  
    value, move = max_value(asp, start_state, player)
    
    return move

    
def max_value(asp, state, player):
    if asp.is_terminal_state(state):
        return asp.evaluate_terminal(state)[player], None
    maxEval = -np.inf

    for action in asp.get_available_actions(state):
        next_state = asp.transition(state, action)
        value, action2 = min_value(asp, next_state, player)
        if value > maxEval:
            maxEval = value  
            best_action = action
    return maxEval, best_action


def min_value(asp, state, player):
    if asp.is_terminal_state(state):
        return asp.evaluate_terminal(state)[player], None
    minEval = np.inf

    for action in asp.get_available_actions(state):
        next_state = asp.transition(state, action)
        value, action2 = max_value(asp, next_state, player)
        if value < minEval:
            minEval = value
            best_action = action
    return minEval, best_action 

    


def alpha_beta(asp: AdversarialSearchProblem[GameState, Action]) -> Action:
    """
    Implement the alpha-beta pruning algorithm on ASPs,
    assuming that the given game is both 2-player and constant-sum.
##code here##
    Input:
        asp - an AdversarialSearchProblem
    Output:
        an action(an element of asp.get_available_actions(asp.get_start_state()))
    """
    ...

    minimax(currentPosition, 3, -infinity, +infinity, true)


#below is the pseudo code from the video, which is probably useless 
#function alpha_beta(position, depth, alpha, beta, maximizingPlayer)
    #if depth == 0 or game over in position
        #return static evaluation of position
    
    #if maximizingPlayer
        #maxEval = -infinity
        #for each child of position
            #eval = minimax(child, depth -1, alpha, beta, false)
            #maxEval = max(maxEval, eval)
            #alpha = max(alpha, eval)
            #if beta <= alpha
                #break
        #return maxEval
    
    #else
        #minEval = +infinity
        #for each child of position
            #eval = minimax(child, depth - 1, alpha, beta, true)
            #minEval = min(minEval, eval)
            #beta = min(beta, eval)
            #if beta <= alpha
                #break
        #return minEval


def alpha_beta_cutoff(
    asp: AdversarialSearchProblem[GameState, Action],
    cutoff_ply: int,
    # See AdversarialSearchProblem:heuristic_func
    heuristic_func: Callable[[GameState], float],
) -> Action:
    """
    This function should:
    - search through the asp using alpha-beta pruning
    - cut off the search after cutoff_ply moves have been made.

    Input:
        asp - an AdversarialSearchProblem
        cutoff_ply - an Integer that determines when to cutoff the search and
            use heuristic_func. For example, when cutoff_ply = 1, use
            heuristic_func to evaluate states that result from your first move.
            When cutoff_ply = 2, use heuristic_func to evaluate states that
            result from your opponent's first move. When cutoff_ply = 3 use
            heuristic_func to evaluate the states that result from your second
            move. You may assume that cutoff_ply > 0.
        heuristic_func - a function that takes in a GameState and outputs a
            real number indicating how good that state is for the player who is
            using alpha_beta_cutoff to choose their action. You do not need to
            implement this function, as it should be provided by whomever is
            calling alpha_beta_cutoff, however you are welcome to write
            evaluation functions to test your implemention. The heuristic_func
            we provide does not handle terminal states, so evaluate terminal
            states the same way you evaluated them in the previous algorithms.
    Output:
        an action(an element of asp.get_available_actions(asp.get_start_state()))
    """
    ...
