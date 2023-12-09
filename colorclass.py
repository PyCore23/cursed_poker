import curses as cr
from curses import color_pair as clr_p
from curses import init_color as i_clr



class Colors:
    
    def __init__(self):
        # COLORS
        self.create_color(1, (239*3, 199*3, 194*3), 'pink')        # PINK
        self.create_color(2, (255*3, 229*3, 212*3), 'soft_white')  # SOFT WHITE
        self.create_color(3, (191*3, 211*3, 193*3), 'soft_green')  # SOFT GREEN
        self.create_color(4, (104*3, 166*3, 145*3), 'green')       # GREEN
        self.create_color(5, (105*3, 79*3, 93*3), 'brown')         # BROWN
        self.create_color(6, (100, 100, 100), 'black')             # BLACK
        self.create_color(7, (1000, 1000, 1000), 'white')          # WHITE
        self.create_color(8, (162*3, 221*3, 224*3), 'blue')        # BLUE 
        self.create_color(9, (200, 700, 300), 'l_green')           # l_green
        self.create_color(10, (700, 100, 300), 'red')              # red
        
        
        # PAIRS
        self.create_pair(1, self.black, self.soft_green, "win_pair")
        self.create_pair(2, self.black, self.black, "black_pair")
        self.create_pair(3, self.soft_white, self.green, "buttons_base")
        self.create_pair(4, self.brown, self.brown, "full_brown")
        self.create_pair(5, self.brown, self.soft_white, 'btn_active')
        self.create_pair(6, self.white, self.pink, 'btn_click')
        self.create_pair(7, self.pink, self.pink, 'shd_click')
        self.create_pair(8, self.l_green, self.l_green, 'fast_click')
        self.create_pair(9, self.red, self.pink, 'red_card')
        

    def create_color(self, number: int, RGB: tuple, attr_color_name: str):
        if number not in self.__dict__.values():
            cr.init_color(number, *RGB)
            self.__setattr__(attr_color_name, number)
        else:
            raise ValueError('color already exists')


    def create_pair(self, number, fg, bg, pair_name):
        if pair_name not in self.__dict__.keys():
            cr.init_pair(number, fg, bg)
            self.__setattr__(pair_name, number)
        else:
            raise ValueError("pair error")