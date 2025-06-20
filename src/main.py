import time
import curses

class Player:
    pass

class GameState():
    def __init__(self, turnphase, should_end, player, computer):
        self.turnphase = turnphase
        self.should_end = should_end
        self.player = player
        self.computer = computer


def main(stdscr):
    # initialization
    player = Player();
    computer = Player();

    gamestate = GameState(0, False, player, computer)

    stdscr.nodelay(True)
    curses.curs_set(0)

    while (gamestate.should_end == False):
        # game logic
        stdscr.clear()

        match gamestate.turnphase:
            case 0:
                key = stdscr.getch()
                if key == ord("e"):
                    gamestate.turnphase = 1
                pass
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass

        # draw
        match gamestate.turnphase:
            case 0:
                stdscr.addstr(0, 0, "Turnphase!")
                pass
            case 1:
                stdscr.addstr(0, 0, "Skillphase!")
                pass
            case 2:
                pass
            case 3:
                # write function to let cards know a round is over
                pass

        stdscr.refresh()
        time.sleep(0.1)


curses.wrapper(main)
