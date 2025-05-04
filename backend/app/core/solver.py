from collections import deque
from app.core.sudoku import Sudoku
import copy

def AC3(board : Sudoku):
    """AC-3 algorithm for arc consistency."""
    queue = deque(board.get_all_arcs())
    total_revisions = 0

    while queue:
        Xi, Xj = queue.popleft()
        print(f"Revising arc [{Xi} -> {Xj}]")
        if revise(Xi, Xj, board):
            total_revisions += 1
            if len(board.domains[Xi]) == 0:
                print(f"Domain wiped out for {Xi}")
                return False
            for Xk in board.get_neighbors(Xi):
                if Xk != Xj:
                    queue.append((Xk, Xi))
    print(f"AC-3 completed with {total_revisions} revisions.")
    print("-"*100)
    return True

def revise(Xi, Xj, board: Sudoku):
    """Revise the domain of Xi based on the domain of Xj."""
    revised = False
    new_domain = ""
    domain_i = board.domains[Xi]
    domain_j = board.domains.get(Xj, "")

    print(f"Current Domain of {Xi}: {domain_i}")
    print(f"Domain of {Xj}: {domain_j}")

    for val_i in domain_i:
        if any(val_i != val_j for val_j in domain_j):
            new_domain += val_i
        else:
            revised = True
            print(f"Removed value {val_i} from {Xi} because no supporting value exists in {Xj}")
            print(f"Supporting values for '{val_i}' in var {Xj} whose domain = [{domain_j}]: None")

    if revised:
        print(f"Updated Domain of {Xi}: {new_domain}")
    board.domains[Xi] = new_domain
    return revised


def backtrack(board : Sudoku):
    """Backtracking algorithm for solving the Sudoku puzzle."""
    ## if all variables have single value in their domain, return True
    if all(len(board.domains[var]) == 1 for var in board.variables):
        return True  # Solved

    # Minimum Remaining Values (MRV) heuristic: select the variable with the fewest legal values
    var = board.select_unassigned_variable()
    if not var:
        return False

    # Least Constraining Value (LCV) heuristic: order the values in the domain of var -> fewest values in the remaining variables
    for value in board.order_domain_values(var):
        if board.is_consistent(var, value):
            original_domains = copy.deepcopy(board.domains)
            board.domains[var] = value

            # Forward checking: remove the value from the domains of neighbors
            inference_result = AC3(board)   ## Inference using arc consistency
            
            if inference_result:
                result = backtrack(board)
                if result:
                    return True
            board.domains = original_domains  # Backtrack

    return False

import time

def solve_board(board: Sudoku):
    print("Applying AC-3 for preprocessing...")
    if not AC3(board):
        print("Unsolvable after AC-3.")
        return False
    time.sleep(5)
    print("Applying backtracking search...")
    if backtrack(board):
        board.update_board_from_domains()
        print("Solved successfully!")
        return True
    else:
        print("No solution found.")
        return False


if __name__ == "__main__":
    board = [
        [4,0,0,8,0,9,5,0,0],
        [0,0,0,0,5,0,6,0,2],
        [0,0,8,0,0,2,0,0,0],
        [0,0,0,0,0,4,0,3,7],
        [0,0,7,0,0,0,4,0,0],
        [6,8,0,9,0,7,0,0,0],
        [0,0,0,5,0,0,7,0,0],
        [1,0,9,0,4,0,0,0,0],
        [0,0,2,3,7,1,8,9,4]
    ]
    
    # board = [
    #     [0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,8,0,5],
    #     [0,0,0,0,7,1,0,0,0],
    #     [0,0,0,0,0,0,0,0,7],
    #     [0,0,5,0,9,0,0,8,1],
    #     [0,0,7,0,0,8,5,9,3],
    #     [0,0,8,0,2,3,0,7,0],
    #     [0,3,9,0,0,5,0,0,0],
    #     [0,7,1,0,6,0,0,0,4]
    # ]

    sudoku = Sudoku(board)
    print("Initial board:")
    sudoku.print_board()

    print("\nSolving Sudoku with CSP...\n")
    if solve_board(sudoku):
        print("\nFinal board:")
        sudoku.print_board()
    else:
        print("Failed to solve.")