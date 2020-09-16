import time
import curses

def main(stdscr):
    curses.curs_set (0)
    curses.init_pair(1,curses.COLOR_YELLOW ,curses.COLOR_WHITE)
    h,w =stdscr.getmaxyx()

    T = "Hello Alex !!"

    x=w//2 - len(T)//2 
    h=h//2

    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(h,x,T)
    stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()
    time.sleep(5)
curses.wrapper(main)
