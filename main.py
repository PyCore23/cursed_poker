import curses as cr
import os, time
from colorclass import Colors
from deck import deck


def poker(win):
    os.system('clear')
    win.clear()
    
    # BASIC SETUP CONFIGS
    cr.noecho()
    cr.cbreak()
    cr.curs_set(0)
    cr.start_color()
    cr.use_default_colors()
    
    HEIGHT, WIDTH = win.getmaxyx()

    # COLOR MANAGER OBJECT
    color = Colors()
    print(cr.COLORS)
    
    def create_button(win: "cr._CursesWindow", text: str, y: int, x: int) -> None:
        button = win.subwin(2, 25, y, x)
        button_shadow = win.subwin(2, 25, y+1, x+2)
        button_shadow.bkgd(' ', cr.color_pair(color.full_brown))
        button_shadow.refresh()
        button.bkgd(' ', cr.color_pair(color.buttons_pair))
        button.addstr(0, 10, text, cr.A_BOLD)
        button.refresh()
    
    
    win.bkgd(' ', cr.color_pair(color.win_pair))
    create_button(win, "START", HEIGHT//3-3, WIDTH//2)
    win.refresh()
    
    time.sleep(20)
    
    
    
    

if __name__ == "__main__":
    cr.wrapper(poker)