EMPTY_SPACE = "."
GRID_LENGTH = 9
FULL_GRID_SIZE = GRID_LENGTH*GRID_LENGTH

class sudoku_grid:
  def __init__(self, originalSetup):
    # originalSetup is a string of 81 characters for the puzzle
    # setup, with numbers and periods (for the blank spaces).
    # See https://inventwithpython.com/sudokupuzzles.txt
    self.originalSetup = originalSetup
    self.grid = {}

  def reset_grid(self):
    for i in range(1, GRID_LENGTH + 1):
      for j in range(1, GRID_LENGTH + 1):
        self.grid[(i,j)] = EMPTY_SPACE

    assert len(self.originalSetup) == FULL_GRID_SIZE, "Please provide a valid sudoku puzzle."

    for i in range(1, GRID_LENGTH + 1):
      for y in range(1, GRID_LENGTH + 1):
        self.grid[(i,y)] = self.originalSetup[i*y-1]
