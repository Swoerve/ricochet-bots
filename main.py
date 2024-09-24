from curses import wrapper

class Game():

    def __init__(self, len_x, len_y) -> None:
        self.len_x = len_x
        self.len_y = len_y
        self.board = []
        self.robots = []
    
    def init_robots(self):
        for i in range(0,4):
            colors = ["blue", "green", "red", "yellow"]
            rb = Robot(0, 0, colors[i], i)
            self.robots.append(rb)

    def print_robots(self):
        content = ""
        for i in self.robots:
            content += str(i)
        print(content)
        return content

    def init_board(self):
        for y in range(0, self.len_y):
            self.board.append([])
            for x in range(0, self.len_x):
                self.board[y].append("#")

    def print_board(self):
        content = ""
        for y in self.board:
            for x in y:
                content += x
            content += "\n"
        return content

class Robot():
    def __init__(self, x: int, y: int, color, id: int) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.id = id

def main(stdscr):
    # Clear screen
    stdscr.clear()

    gem = Game(5, 5)
    gem.init_board()
    gem.init_robots()
    stdscr.addstr(gem.print_board())
    
    def update_screen():
        stdscr.clear()
        stdscr.addstr(gem.print_board())
        stdscr.addstr(gem.print_robots())

    while True:
        update_screen()
        inp = stdscr.getch()
        if inp == ord('q'):
            break
    stdscr.refresh()
wrapper(main)
