class Sudoku:
    def __init__(self, board, debug=False):
        """
        Initialize the Sudoku puzzle.
        board: a 9x9 list of lists with integers (0 means empty).
        """
        self.board = board
        self.debug = debug
        self.size = 9
        self.box_size = 3
        self.variables = self.__initialize_variables()
        self.domains = self.__initialize_domains()

    def print_board(self):
        for i, row in enumerate(self.board):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j, val in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(val if val != 0 else ".", end=" ")
            print()

    def __initialize_variables(self):
        variables = []
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    variables.append((r, c))
        return variables

    def __initialize_domains(self):
        domains = {}
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    domains[(r, c)] = "123456789"
                else:
                    domains[(r, c)] = str(self.board[r][c])
        return domains

    
    def get_neighbors(self, var):
        row, col = var
        neighbors = set()

        # Row and Column neighbors
        for i in range(self.size):
            if (row, i) != var:
                neighbors.add((row, i))
            if (i, col) != var:
                neighbors.add((i, col))

        # 3x3 box neighbors
        box_start_row = 3 * (row // 3)
        box_start_col = 3 * (col // 3)
        for r in range(box_start_row, box_start_row + 3):
            for c in range(box_start_col, box_start_col + 3):
                if (r, c) != var:
                    neighbors.add((r, c))

        return neighbors
    
    def get_all_arcs(self):
        arcs = []
        for var in self.variables:
            for neighbor in self.get_neighbors(var):
                arcs.append((var, neighbor))
        return arcs
    
    def update_board_from_domains(self):
        # for (r, c), domain in self.domains.items():
        #     if len(domain) == 1:
        #         self.board[r][c] = int(domain[0])
        for var in self.variables:
            if len(self.domains[var]) == 1:
                r, c = var
                self.board[r][c] = int(self.domains[var])

    def is_consistent(self, var, value):
        for neighbor in self.get_neighbors(var):
            if len(self.domains[neighbor]) == 1 and self.domains[neighbor] == value:
                return False
        return True
    
    def select_unassigned_variable(self):
        # Select the variable with the smallest domain size
        # Min Remaining Values (MRV) heuristic
        return min(
            (var for var in self.variables if len(self.domains[var]) > 1),
            key=lambda var: len(self.domains[var]),
            default=None
        )
    
    def order_domain_values(self, var):
        """
        Return the values in the domain of `var` ordered by the LCV heuristic.
        Values that eliminate the fewest choices for neighbors come first.
        """
        # LCV (Least Constraining Value) heuristic
        if len(self.domains[var]) == 1:
            return self.domains[var]

        neighbors = self.get_neighbors(var)
        value_constraints = []

        for value in self.domains[var]:
            elimination_count = 0
            for neighbor in neighbors:
                if len(self.domains[neighbor]) > 1:
                    if value in self.domains[neighbor]:
                        elimination_count += 1
            value_constraints.append((value, elimination_count))

        # Sort values by the number of eliminations (least first)
        sorted_values = sorted(value_constraints, key=lambda x: x[1])
        return [val for val, _ in sorted_values]
