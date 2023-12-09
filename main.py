import curses as cr
import os, time
from colorclass import Colors
from deck import Deck
import locale
locale.getpreferredencoding('UTF-8')


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
    locale.getpreferredencoding("UTF-8")
    

    # COLOR MANAGER OBJECT
    ######################
    color = Colors()######
    ######################
    
    def create_button(win: "cr._CursesWindow", text: str, y: int, x: int) -> None:
        button_shadow = win.subwin(2, 26, y+1, x+2)
        button_shadow.bkgd(' ', cr.color_pair(color.full_brown))
        button_shadow.refresh()
        button = win.subwin(2, 26, y, x)
        button.bkgd(' ', cr.color_pair(color.buttons_base))
        button.addstr(0, 7, text, cr.A_BOLD)
        button.addstr(0, 20, ' ', cr.A_BOLD)
        button.refresh()
        return button
    
    
    win.bkgd(' ', cr.color_pair(color.win_pair))
    info = win.subwin(1, 20, 1, 2)
    info.addstr('⠫⠀⠑⠃⠁⠇⠀⠪⠞⠕⠞⠀⠏⠕⠅⠑⠗')
    info.refresh()
    title = win.subwin(1, WIDTH//2-20)
    poker_title = """
██████╗  ██████╗ ██╗  ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝██╔══██╗
██████╔╝██║   ██║█████╔╝ █████╗  ██████╔╝
██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║  ██╗███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""
    title.addstr(poker_title)
    title.refresh()
    win.border()
    
    def draw_menu_buttons():
        start = create_button(win, "START", HEIGHT//3+2, WIDTH//2-13)
        settings = create_button(win, "SETTINGS", HEIGHT//3+6, WIDTH//2-13)
        about = create_button(win, "ABOUT", HEIGHT//3+10, WIDTH//2-13)
        exit_btn = create_button(win, "EXIT", HEIGHT//3+14, WIDTH//2-13)
        return start, settings, about, exit_btn
    
    def clicking():
        current.bkgd(' ', cr.color_pair(color.fast_click))
        current.refresh()
        cr.delay_output(50)
        current.bkgd(' ', cr.color_pair(color.buttons_base))
        current.refresh()
    
    def draw_card(card: str, place: "cr._CursesWindow"):
        for char in card:
            if char in ['♦', '♥']:
                place.addch(char, cr.color_pair(color.red_card))
            if char in ['♣', '♠']:
                place.addch(char, cr.color_pair(color.black_pair))
            place.addch(char, cr.color_pair(color.btn_active))
    
    def start_game():
        win.clear()
        win.refresh()
        def draw_table_intarface():
            player_left_card_shadow = win.subwin(9, 11, HEIGHT-10, WIDTH//2-12)
            player_left_card_shadow.bkgd(' ')
            player_left_card_shadow.refresh()
            player_left_card = win.subwin(9, 11, HEIGHT-11, WIDTH//2-13)
            player_left_card.bkgd(' ')
            

            player_right_card_shadow = win.subwin(9, 11, HEIGHT-10, WIDTH//2+2)
            player_right_card_shadow.bkgd(' ')
            player_right_card_shadow.refresh()      
            player_right_card = win.subwin(9, 11, HEIGHT-11, WIDTH//2+1)
            player_right_card.bkgd(' ')
        
    
    def about_menu():
        win.clear()
        app_info = """
        This is a simple command-line poker game implemented in Python
        using the curses module. In the future, 
        I plan to enhance the game by incorporating artificial intelligence 
        to power a computer-controlled opponent
        """
        win.addstr(5, 5, app_info, cr.A_BLINK)
        win.refresh()
        back = create_button(win, "BACK", HEIGHT-3, WIDTH//2-2)
        back.bkgd('_')
        back.refresh()
        while True:
            key = win.getch()
            if key == 10:
                win.clear()
                win.refresh()
                break
    
    def quit_game():
        win.clear()
        confirm_btn = create_button(win, "EXIT ???", 22, 42)
        confirm_btn.refresh()
        cr.set_escdelay(10)
        while True:
            key = win.getch()
            if key == 10:
                clicking()
                cr.endwin()
                exit()
            if key == 27:
                clicking()
                break
    
    
    win.refresh()
    buttons = [btn for btn in draw_menu_buttons()]
    current = buttons[0]
    while True:
        key = win.getch()
        win.refresh()
        
        # ONENTER PRESS
        if key == 10:
            if current == buttons[0]: # START
                clicking()
                start_game()

            if current == buttons[1]: # SETTINGS
                clicking()
                while True:
                    text = win.subwin(10, 20, HEIGHT//2-10, WIDTH//2-20)
                    text.addstr("in progress", cr.A_ITALIC)
                    text.refresh()
                    cr.delay_output(400)
                    break

            if current == buttons[2]: # ABOUT
                clicking()
                about_menu()
                draw_menu_buttons()
                title.addstr(1, WIDTH//2-20, poker_title)
                title.refresh()
                info = win.subwin(1, 20, 1, 2)
                info.addstr('⠫⠀⠑⠃⠁⠇⠀⠪⠞⠕⠞⠀⠏⠕⠅⠑⠗')
                info.refresh()
                
            if current == buttons[3]: # EXIT
                clicking()
                quit_game()
    
        # NAVIGATE MENU
        if key == 258 or key == 259:
            current.bkgd(' ', cr.color_pair(color.buttons_base))
            current.refresh()
            if key == 259:
                current.bkgd(' ', cr.color_pair(color.buttons_base))
                current.refresh()
                if buttons.index(current) == 0:
                    current = buttons[-1]
                    current.bkgd(' ', cr.color_pair(color.btn_active))
                    current.refresh()
                else:
                    current = buttons[buttons.index(current) - 1]
                    current.bkgd(' ', cr.color_pair(color.btn_active))
                    current.refresh()
            if key == 258:
                current.bkgd(' ', cr.color_pair(color.buttons_base))
                current.refresh()
                if buttons.index(current) == 3:
                    current = buttons[0]
                    current.bkgd(' ', cr.color_pair(color.btn_active))
                    current.refresh()        
                else:
                    current = buttons[buttons.index(current) + 1]
                    current.bkgd(' ', cr.color_pair(color.btn_active))
                    current.refresh()        

    
    
if __name__ == "__main__":
    cr.wrapper(poker)