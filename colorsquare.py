from constsquare import const_square


class color_square:
    def __init__(self, row, col, color, shape, final, move):
        self.square_info = const_square(row, col, color, shape).square_info
        self.square_info.update({"final": final})
        self.square_info.update({"move": move})
