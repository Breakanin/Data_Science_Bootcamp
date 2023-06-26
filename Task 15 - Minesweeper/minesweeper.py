# Define a function that takes a grid of # and - as an argument
def minesweeper(grid):
  # Create an empty list to store the output grid
  output = []
  # Loop through each row and column of the input grid using enumerate
  for row_index, row in enumerate(grid): # outer loop for rows
    # Create an empty list to store the current row of the output grid
    output_row = []
    for col_index, col in enumerate(row): # inner loop for columns
      # If the current position is a mine, append # to the output row
      if col == "#":
        output_row.append("#")
      # Else, count the number of adjacent mines and append it to the output row
      else:
        # Initialize a counter for adjacent mines
        mines_counter = 0
        # Loop through the adjacent positions using relative indexes
        for x in [-1, 0, 1]:
          for y in [-1, 0, 1]:
            # Skip the current position
            if x == 0 and y == 0:
              continue
            # Calculate the absolute indexes of the adjacent position
            adjacent_row = row_index + x
            adjacent_col = col_index + y
            # Check if the adjacent position is valid and has a mine
            if 0 <= adjacent_row < len(grid) and 0 <= adjacent_col < len(row) and grid[adjacent_row][adjacent_col] == "#":
              # Increment the counter for adjacent mines
              mines_counter += 1
        # Append the number of adjacent mines to the output row as a string
        output_row.append(str(mines_counter))
    # Append the output row to the output grid
    output.append(output_row)
  # Return the output grid
  return output

# Example of an input grid
grid = [ ["-", "T", "O", "T", "#"],
         ["-", "O", "X", "O", "-"],
         ["-", "T", "O", "T", "-"],
         ["-", "#", "#", "-", "-"],
         ["-", "-", "-", "-", "-"] ]

# Example of calling the function and printing the output grid
output = minesweeper(grid)
for row in output:
  print(row)