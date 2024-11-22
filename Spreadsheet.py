import curses

CELL_WIDTH = 10

def draw_grid(win, data, active_row, active_col):
    """Draw the spreadsheet grid."""
    win.clear()
    rows, cols = len(data), len(data[0])
    for i in range(rows):
        for j in range(cols):
            cell_value = data[i][j][:CELL_WIDTH - 1]  # Truncate long content
            if i == active_row and j == active_col:
                win.addstr(i * 2, j * CELL_WIDTH, f"[{cell_value:^8}]", curses.A_REVERSE)
            else:
                win.addstr(i * 2, j * CELL_WIDTH, f" {cell_value:^8} ")

    win.addstr(rows * 2 + 1, 0, "Arrow keys to navigate, Enter to edit, 'a' to add row/col, 'r' to remove row/col, 'q' to quit.")
    win.refresh()

def edit_cell(win, data, active_row, active_col):
    """Allow the user to edit the content of the active cell."""
    curses.echo()  # Enable input echoing
    win.addstr(len(data) * 2 + 3, 0, f"Editing R{active_row+1}C{active_col+1}: ")
    win.clrtoeol()
    new_value = win.getstr(len(data) * 2 + 3, len(f"Editing R{active_row+1}C{active_col+1}: "), CELL_WIDTH - 1).decode('utf-8')
    curses.noecho()  # Disable input echoing
    if new_value.strip():
        data[active_row][active_col] = new_value.strip()

def add_row_or_col(data, add_type):
    """Add a row or column to the spreadsheet."""
    rows, cols = len(data), len(data[0])
    if add_type == "row":
        new_row = [f"R{rows+1}C{j+1}" for j in range(cols)]
        data.append(new_row)
    elif add_type == "col":
        for i in range(rows):
            data[i].append(f"R{i+1}C{cols+1}")

def remove_row_or_col(data, remove_type, active_row, active_col):
    """Remove a row or column from the spreadsheet."""
    rows, cols = len(data), len(data[0])
    if remove_type == "row" and rows > 1:
        data.pop(active_row)
    elif remove_type == "col" and cols > 1:
        for i in range(rows):
            data[i].pop(active_col)

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor

    # Ask the user for the size of the spreadsheet
    stdscr.addstr(0, 0, "Enter the number of rows: ")
    curses.echo()
    rows = int(stdscr.getstr().decode('utf-8'))
    stdscr.addstr(1, 0, "Enter the number of columns: ")
    cols = int(stdscr.getstr().decode('utf-8'))
    curses.noecho()

    # Initialize spreadsheet data
    data = [[f"R{i+1}C{j+1}" for j in range(cols)] for i in range(rows)]
    active_row, active_col = 0, 0

    while True:
        draw_grid(stdscr, data, active_row, active_col)
        key = stdscr.getch()

        if key == curses.KEY_UP and active_row > 0:
            active_row -= 1
        elif key == curses.KEY_DOWN and active_row < len(data) - 1:
            active_row += 1
        elif key == curses.KEY_LEFT and active_col > 0:
            active_col -= 1
        elif key == curses.KEY_RIGHT and active_col < len(data[0]) - 1:
            active_col += 1
        elif key == ord('q'):
            break
        elif key == ord('\n') or key == curses.KEY_ENTER:
            edit_cell(stdscr, data, active_row, active_col)
        elif key == ord('a'):
            stdscr.addstr(len(data) * 2 + 3, 0, "Add row (r) or column (c)? ")
            stdscr.clrtoeol()
            choice = stdscr.getch()
            if choice == ord('r'):
                add_row_or_col(data, "row")
            elif choice == ord('c'):
                add_row_or_col(data, "col")
        elif key == ord('r'):
            stdscr.addstr(len(data) * 2 + 3, 0, "Remove row (r) or column (c)? ")
            stdscr.clrtoeol()
            choice = stdscr.getch()
            if choice == ord('r'):
                remove_row_or_col(data, "row", active_row, active_col)
                active_row = max(0, active_row - (1 if active_row >= len(data) else 0))
            elif choice == ord('c'):
                remove_row_or_col(data, "col", active_row, active_col)
                active_col = max(0, active_col - (1 if active_col >= len(data[0]) else 0))

if __name__ == "__main__":
    curses.wrapper(main)
