from copy import deepcopy
import numpy as np
from constsquare import const_square
from colorsquare import color_square


class state:
    def __init__(self, size_array):
        self.size = size_array
        self.my_array = np.full((size_array, size_array), fill_value="", dtype=object)
        self.destination_array = np.array((), dtype=color_square)
        # self.next_states_array = np.array((), dtype=object)
        for row in range(0, size_array):
            for col in range(0, size_array):
                self.my_array[row][col] = const_square(
                    row, col, "white", "⬜️"
                ).square_info

    def fill_const_col(self, row1, row2, col, color, shape):
        if row1 < row2:

            while row1 <= row2:
                self.my_array[row1][col] = const_square(
                    row1, col, color, shape
                ).square_info
                row1 += 1
            return
        elif row1 > row2:

            while row1 >= row2:
                self.my_array[row1][col] = const_square(
                    row1, col, color, shape
                ).square_info
                row1 -= 1
            return
        else:
            self.my_array[row1][col] = const_square(row1, col, color, shape).square_info
            return

    def fill_const_row(self, row, col1, col2, color, shape):
        if col1 < col2:

            while col1 <= col2:
                self.my_array[row][col1] = const_square(
                    row, col1, color, shape
                ).square_info
                col1 += 1
            return
        elif col1 > col2:

            while col1 >= col2:
                self.my_array[row][col1] = const_square(
                    row, col1, color, shape
                ).square_info
                col1 -= 1
            return
        else:
            self.my_array[row][col1] = const_square(row, col1, color, shape).square_info
            return

    def fill_color_cell(self, row, col, color, shape, final, move):
        self.my_array[row][col] = color_square(
            row, col, color, shape, final, move
        ).square_info

    def right_mobility(self, row, col):
        if self.my_array[row][col + 1]["color"] == "black":
            return False
        elif self.my_array[row][col + 1]["color"] == "white":
            return True
        else:
            if self.my_array[row][col + 1]["final"] == False:
                return False
            return True

    def left_mobility(self, row, col):
        if self.my_array[row][col - 1]["color"] == "black":
            return False
        elif self.my_array[row][col - 1]["color"] == "white":
            return True
        else:
            if self.my_array[row][col - 1]["final"] == False:
                return False
            return True

    def up_mobility(self, row, col):
        if self.my_array[row - 1][col]["color"] == "black":
            return False
        elif self.my_array[row - 1][col]["color"] == "white":
            return True
        else:
            if self.my_array[row - 1][col]["final"] == False:
                return False
            return True

    def down_mobility(self, row, col):
        if self.my_array[row + 1][col]["color"] == "black":
            return False
        elif self.my_array[row + 1][col]["color"] == "white":
            return True
        else:
            if self.my_array[row + 1][col]["final"] == False:
                return False
            return True

    #####################################################################################################################################
    @classmethod
    def right_move(cls, current_state):
        new_state = deepcopy(current_state)
        for row in range(0, new_state.size):
            for col in range(0, new_state.size):
                if (
                    new_state.my_array[row][col]["color"] == "white"
                    or new_state.my_array[row][col]["color"] == "black"
                ):
                    new_state.right_reverse_square(row, col - 1)
                    continue
                elif new_state.my_array[row][col]["final"] == True:
                    new_state.right_reverse_square(row, col - 1)
                    continue
                else:
                    if col != new_state.size - 1:
                        if new_state.right_mobility(row, col) == False:
                            new_state.right_reverse_square(row, col - 1)
                            continue
                        else:
                            new_state.my_array[row][col]["move"] = True
                            if (
                                new_state.my_array[row][col]["color"]
                                == new_state.my_array[row][col + 1]["color"]
                            ):
                                if new_state.destination_array.size == 0:
                                    new_state.my_array[row][col] = const_square(
                                        row, col, "white", "⬜️"
                                    ).square_info
                                    new_state.my_array[row][col + 1] = const_square(
                                        row, col + 1, "white", "⬜️"
                                    ).square_info
                                    new_state.right_reverse_square(row, col - 1)

                                else:
                                    for item in new_state.destination_array:
                                        if (
                                            item.square_info["row"] == row
                                            and item.square_info["col"] == col
                                        ):

                                            new_state.my_array[row][col + 1] = (
                                                const_square(
                                                    row, col + 1, "white", "⬜️"
                                                ).square_info
                                            )
                                            new_state.my_array[row][col] = color_square(
                                                item.square_info["row"],
                                                item.square_info["col"],
                                                item.square_info["color"],
                                                item.square_info["shape"],
                                                item.square_info["final"],
                                                item.square_info["move"],
                                            ).square_info
                                            index = np.where(
                                                new_state.destination_array == item
                                            )
                                            new_state.destination_array = np.delete(
                                                new_state.destination_array, index
                                            )
                                            new_state.right_reverse_square(row, col - 1)

                                            break
                                        else:
                                            new_state.my_array[row][col] = const_square(
                                                row, col, "white", "⬜️"
                                            ).square_info
                                            new_state.my_array[row][col + 1] = (
                                                const_square(
                                                    row, col + 1, "white", "⬜️"
                                                ).square_info
                                            )
                                            new_state.right_reverse_square(row, col - 1)

                            elif new_state.my_array[row][col + 1]["color"] == "black":
                                continue
                            elif new_state.my_array[row][col + 1]["color"] == "white":

                                if new_state.destination_array.size == 0:
                                    new_state.my_array[row][col + 1] = color_square(
                                        row,
                                        col + 1,
                                        new_state.my_array[row][col]["color"],
                                        new_state.my_array[row][col]["shape"],
                                        new_state.my_array[row][col]["final"],
                                        new_state.my_array[row][col]["move"],
                                    ).square_info
                                    new_state.my_array[row][col] = const_square(
                                        row, col, "white", "⬜️"
                                    ).square_info
                                    new_state.right_reverse_square(row, col - 1)

                                else:
                                    for item in new_state.destination_array:
                                        if (
                                            item.square_info["row"] == row
                                            and item.square_info["col"] == col
                                        ):
                                            if (
                                                new_state.my_array[row][col]["color"]
                                                != "white"
                                            ):
                                                new_state.my_array[row][col + 1] = (
                                                    color_square(
                                                        row,
                                                        col + 1,
                                                        new_state.my_array[row][col][
                                                            "color"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "shape"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "final"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "move"
                                                        ],
                                                    ).square_info
                                                )
                                            new_state.my_array[row][col] = color_square(
                                                item.square_info["row"],
                                                item.square_info["col"],
                                                item.square_info["color"],
                                                item.square_info["shape"],
                                                item.square_info["final"],
                                                item.square_info["move"],
                                            ).square_info
                                            index = np.where(
                                                new_state.destination_array == item
                                            )
                                            new_state.destination_array = np.delete(
                                                new_state.destination_array, index
                                            )
                                            new_state.right_reverse_square(row, col - 1)

                                            break

                                        else:
                                            if (
                                                new_state.my_array[row][col]["color"]
                                                != "white"
                                            ):
                                                new_state.my_array[row][col + 1] = (
                                                    color_square(
                                                        row,
                                                        col + 1,
                                                        new_state.my_array[row][col][
                                                            "color"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "shape"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "final"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "move"
                                                        ],
                                                    ).square_info
                                                )
                                                new_state.my_array[row][col] = (
                                                    const_square(
                                                        row, col, "white", "⬜️"
                                                    ).square_info
                                                )
                                                new_state.right_reverse_square(
                                                    row, col - 1
                                                )

                            elif new_state.my_array[row][col + 1]["final"] == False:
                                continue
                            else:
                                if new_state.my_array[row][col + 1]["shape"] != "🔶":

                                    new_state.destination_array = np.append(
                                        new_state.destination_array,
                                        color_square(
                                            new_state.my_array[row][col + 1]["row"],
                                            new_state.my_array[row][col + 1]["col"],
                                            new_state.my_array[row][col + 1]["color"],
                                            new_state.my_array[row][col + 1]["shape"],
                                            new_state.my_array[row][col + 1]["final"],
                                            new_state.my_array[row][col + 1]["move"],
                                        ),
                                    )
                                    new_state.my_array[row][col + 1] = color_square(
                                        row,
                                        col + 1,
                                        new_state.my_array[row][col]["color"],
                                        new_state.my_array[row][col]["shape"],
                                        new_state.my_array[row][col]["final"],
                                        new_state.my_array[row][col]["move"],
                                    ).square_info
                                    new_state.my_array[row][col] = const_square(
                                        row, col, "white", "⬜️"
                                    ).square_info
                                    new_state.right_reverse_square(row, col - 1)

                                else:

                                    new_state.destination_array = np.append(
                                        new_state.destination_array,
                                        color_square(
                                            new_state.my_array[row][col + 1]["row"],
                                            new_state.my_array[row][col + 1]["col"],
                                            new_state.my_array[row][col + 1]["color"],
                                            new_state.my_array[row][col + 1]["shape"],
                                            new_state.my_array[row][col + 1]["final"],
                                            new_state.my_array[row][col + 1]["move"],
                                        ),
                                    )
                                    new_state.destination_array[-1].square_info[
                                        "color"
                                    ] = new_state.my_array[row][col]["color"]
                                    new_state.my_array[row][col + 1] = color_square(
                                        row,
                                        col + 1,
                                        new_state.my_array[row][col]["color"],
                                        new_state.my_array[row][col]["shape"],
                                        new_state.my_array[row][col]["final"],
                                        new_state.my_array[row][col]["move"],
                                    ).square_info
                                    new_state.my_array[row][col] = const_square(
                                        row, col, "white", "⬜️"
                                    ).square_info
                                    new_state.right_reverse_square(row, col - 1)
        for row in range(0, new_state.size):
            for col in range(0, new_state.size):
                if (
                    new_state.my_array[row][col]["color"] != "white"
                    and new_state.my_array[row][col]["color"] != "black"
                ):
                    new_state.my_array[row][col]["move"] = False
        return new_state
        ####################################################################################################################

    @classmethod
    def left_move(cls, current_state):
        new_state = deepcopy(current_state)
        for row in range(0, new_state.size):
            for col in range(new_state.size - 1, -1, -1):
                if (
                    new_state.my_array[row][col]["color"] == "white"
                    or new_state.my_array[row][col]["color"] == "black"
                ):
                    new_state.left_reverse_square(row, col + 1)
                    continue
                elif new_state.my_array[row][col]["final"] == True:
                    new_state.left_reverse_square(row, col + 1)
                    continue
                else:
                    if col != 0:
                        if new_state.left_mobility(row, col) == False:
                            new_state.left_reverse_square(row, col + 1)
                            continue
                        else:
                            new_state.my_array[row][col]["move"] = True
                            if (
                                new_state.my_array[row][col]["color"]
                                == new_state.my_array[row][col - 1]["color"]
                            ):
                                if new_state.destination_array.size == 0:
                                    new_state.my_array[row][col] = const_square(
                                        row, col, "white", "⬜️"
                                    ).square_info
                                    new_state.my_array[row][col - 1] = const_square(
                                        row, col - 1, "white", "⬜️"
                                    ).square_info
                                    new_state.left_reverse_square(row, col + 1)

                                else:
                                    for item in new_state.destination_array:
                                        if (
                                            item.square_info["row"] == row
                                            and item.square_info["col"] == col
                                        ):

                                            new_state.my_array[row][col - 1] = (
                                                const_square(
                                                    row, col - 1, "white", "⬜️"
                                                ).square_info
                                            )
                                            new_state.my_array[row][col] = color_square(
                                                item.square_info["row"],
                                                item.square_info["col"],
                                                item.square_info["color"],
                                                item.square_info["shape"],
                                                item.square_info["final"],
                                                item.square_info["move"],
                                            ).square_info
                                            index = np.where(
                                                new_state.destination_array == item
                                            )
                                            new_state.destination_array = np.delete(
                                                new_state.destination_array, index
                                            )
                                            new_state.left_reverse_square(row, col + 1)

                                            break
                                        else:
                                            new_state.my_array[row][col] = const_square(
                                                row, col, "white", "⬜️"
                                            ).square_info
                                            new_state.my_array[row][col + 1] = (
                                                const_square(
                                                    row, col - 1, "white", "⬜️"
                                                ).square_info
                                            )
                                            new_state.left_reverse_square(row, col + 1)

                            elif new_state.my_array[row][col - 1]["color"] == "black":
                                continue
                            elif new_state.my_array[row][col - 1]["color"] == "white":

                                if new_state.destination_array.size == 0:
                                    new_state.my_array[row][col - 1] = color_square(
                                        row,
                                        col - 1,
                                        new_state.my_array[row][col]["color"],
                                        new_state.my_array[row][col]["shape"],
                                        new_state.my_array[row][col]["final"],
                                        new_state.my_array[row][col]["move"],
                                    ).square_info
                                    new_state.my_array[row][col] = const_square(
                                        row, col, "white", "⬜️"
                                    ).square_info
                                    new_state.left_reverse_square(row, col + 1)

                                else:
                                    for item in new_state.destination_array:
                                        if (
                                            item.square_info["row"] == row
                                            and item.square_info["col"] == col
                                        ):
                                            if (
                                                new_state.my_array[row][col]["color"]
                                                != "white"
                                            ):
                                                new_state.my_array[row][col - 1] = (
                                                    color_square(
                                                        row,
                                                        col - 1,
                                                        new_state.my_array[row][col][
                                                            "color"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "shape"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "final"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "move"
                                                        ],
                                                    ).square_info
                                                )
                                            new_state.my_array[row][col] = color_square(
                                                item.square_info["row"],
                                                item.square_info["col"],
                                                item.square_info["color"],
                                                item.square_info["shape"],
                                                item.square_info["final"],
                                                item.square_info["move"],
                                            ).square_info
                                            index = np.where(
                                                new_state.destination_array == item
                                            )
                                            new_state.destination_array = np.delete(
                                                new_state.destination_array, index
                                            )
                                            new_state.left_reverse_square(row, col + 1)

                                            break

                                        else:
                                            if (
                                                new_state.my_array[row][col]["color"]
                                                != "white"
                                            ):
                                                new_state.my_array[row][col - 1] = (
                                                    color_square(
                                                        row,
                                                        col - 1,
                                                        new_state.my_array[row][col][
                                                            "color"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "shape"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "final"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "move"
                                                        ],
                                                    ).square_info
                                                )
                                                new_state.my_array[row][col] = (
                                                    const_square(
                                                        row, col, "white", "⬜️"
                                                    ).square_info
                                                )
                                                new_state.left_reverse_square(
                                                    row, col + 1
                                                )

                            elif new_state.my_array[row][col - 1]["final"] == False:
                                continue
                            else:
                                if new_state.my_array[row][col - 1]["shape"] != "🔶":

                                    new_state.destination_array = np.append(
                                        new_state.destination_array,
                                        color_square(
                                            new_state.my_array[row][col - 1]["row"],
                                            new_state.my_array[row][col - 1]["col"],
                                            new_state.my_array[row][col - 1]["color"],
                                            new_state.my_array[row][col - 1]["shape"],
                                            new_state.my_array[row][col - 1]["final"],
                                            new_state.my_array[row][col - 1]["move"],
                                        ),
                                    )
                                    new_state.my_array[row][col - 1] = color_square(
                                        row,
                                        col - 1,
                                        new_state.my_array[row][col]["color"],
                                        new_state.my_array[row][col]["shape"],
                                        new_state.my_array[row][col]["final"],
                                        new_state.my_array[row][col]["move"],
                                    ).square_info
                                    new_state.my_array[row][col] = const_square(
                                        row, col, "white", "⬜️"
                                    ).square_info
                                    new_state.left_reverse_square(row, col + 1)

                                else:

                                    new_state.destination_array = np.append(
                                        new_state.destination_array,
                                        color_square(
                                            new_state.my_array[row][col - 1]["row"],
                                            new_state.my_array[row][col - 1]["col"],
                                            new_state.my_array[row][col - 1]["color"],
                                            new_state.my_array[row][col - 1]["shape"],
                                            new_state.my_array[row][col - 1]["final"],
                                            new_state.my_array[row][col - 1]["move"],
                                        ),
                                    )
                                    new_state.destination_array[-1].square_info[
                                        "color"
                                    ] = new_state.my_array[row][col]["color"]
                                    new_state.my_array[row][col - 1] = color_square(
                                        row,
                                        col - 1,
                                        new_state.my_array[row][col]["color"],
                                        new_state.my_array[row][col]["shape"],
                                        new_state.my_array[row][col]["final"],
                                        new_state.my_array[row][col]["move"],
                                    ).square_info
                                    new_state.my_array[row][col] = const_square(
                                        row, col, "white", "⬜️"
                                    ).square_info
                                    new_state.left_reverse_square(row, col + 1)
        for row in range(0, new_state.size):
            for col in range(0, new_state.size):
                if (
                    new_state.my_array[row][col]["color"] != "white"
                    and new_state.my_array[row][col]["color"] != "black"
                ):
                    new_state.my_array[row][col]["move"] = False
        return new_state

    #############################################################################################################################
    @classmethod
    def up_move(cls, current_state):
        new_state = deepcopy(current_state)

        for row in range(new_state.size - 1, -1, -1):
            for col in range(0, new_state.size):
                if (
                    new_state.my_array[row][col]["color"] == "white"
                    or new_state.my_array[row][col]["color"] == "black"
                ):
                    new_state.up_reverse_square(row + 1, col)
                    continue
                elif new_state.my_array[row][col]["final"] == True:
                    new_state.up_reverse_square(row + 1, col)
                    continue
                else:
                    if row != 0:
                        if new_state.up_mobility(row, col) == False:
                            new_state.up_reverse_square(row + 1, col)
                            continue
                        else:
                            new_state.my_array[row][col]["move"] = True
                            if (
                                new_state.my_array[row][col]["color"]
                                == new_state.my_array[row - 1][col]["color"]
                            ):
                                if new_state.destination_array.size == 0:
                                    new_state.my_array[row][col] = const_square(
                                        row, col, "white", "⬜️"
                                    ).square_info
                                    new_state.my_array[row - 1][col] = const_square(
                                        row - 1, col, "white", "⬜️"
                                    ).square_info
                                    new_state.up_reverse_square(row + 1, col)

                                else:
                                    for item in new_state.destination_array:
                                        if (
                                            item.square_info["row"] == row
                                            and item.square_info["col"] == col
                                        ):

                                            new_state.my_array[row - 1][col] = (
                                                const_square(
                                                    row - 1, col, "white", "⬜️"
                                                ).square_info
                                            )
                                            new_state.my_array[row][col] = color_square(
                                                item.square_info["row"],
                                                item.square_info["col"],
                                                item.square_info["color"],
                                                item.square_info["shape"],
                                                item.square_info["final"],
                                                item.square_info["move"],
                                            ).square_info
                                            index = np.where(
                                                new_state.destination_array == item
                                            )
                                            new_state.destination_array = np.delete(
                                                new_state.destination_array, index
                                            )
                                            new_state.up_reverse_square(row + 1, col)

                                            break
                                        else:
                                            new_state.my_array[row][col] = const_square(
                                                row, col, "white", "⬜️"
                                            ).square_info
                                            new_state.my_array[row - 1][col] = (
                                                const_square(
                                                    row - 1, col, "white", "⬜️"
                                                ).square_info
                                            )
                                            new_state.up_reverse_square(row + 1, col)

                            elif new_state.my_array[row - 1][col]["color"] == "black":
                                continue
                            elif new_state.my_array[row - 1][col]["color"] == "white":

                                if new_state.destination_array.size == 0:
                                    new_state.my_array[row - 1][col] = color_square(
                                        row - 1,
                                        col,
                                        new_state.my_array[row][col]["color"],
                                        new_state.my_array[row][col]["shape"],
                                        new_state.my_array[row][col]["final"],
                                        new_state.my_array[row][col]["move"],
                                    ).square_info
                                    new_state.my_array[row][col] = const_square(
                                        row, col, "white", "⬜️"
                                    ).square_info
                                    new_state.up_reverse_square(row + 1, col)

                                else:
                                    for item in new_state.destination_array:
                                        if (
                                            item.square_info["row"] == row
                                            and item.square_info["col"] == col
                                        ):
                                            if (
                                                new_state.my_array[row][col]["color"]
                                                != "white"
                                            ):
                                                new_state.my_array[row - 1][col] = (
                                                    color_square(
                                                        row - 1,
                                                        col,
                                                        new_state.my_array[row][col][
                                                            "color"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "shape"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "final"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "move"
                                                        ],
                                                    ).square_info
                                                )
                                            new_state.my_array[row][col] = color_square(
                                                item.square_info["row"],
                                                item.square_info["col"],
                                                item.square_info["color"],
                                                item.square_info["shape"],
                                                item.square_info["final"],
                                                item.square_info["move"],
                                            ).square_info
                                            index = np.where(
                                                new_state.destination_array == item
                                            )
                                            new_state.destination_array = np.delete(
                                                new_state.destination_array, index
                                            )
                                            new_state.up_reverse_square(row + 1, col)

                                            break

                                        else:
                                            if (
                                                new_state.my_array[row][col]["color"]
                                                != "white"
                                            ):
                                                new_state.my_array[row - 1][col] = (
                                                    color_square(
                                                        row - 1,
                                                        col,
                                                        new_state.my_array[row][col][
                                                            "color"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "shape"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "final"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "move"
                                                        ],
                                                    ).square_info
                                                )
                                                new_state.my_array[row][col] = (
                                                    const_square(
                                                        row, col, "white", "⬜️"
                                                    ).square_info
                                                )
                                                new_state.up_reverse_square(
                                                    row + 1, col
                                                )

                            elif new_state.my_array[row - 1][col]["final"] == False:
                                continue
                            else:
                                if new_state.my_array[row - 1][col]["shape"] != "🔶":

                                    new_state.destination_array = np.append(
                                        new_state.destination_array,
                                        color_square(
                                            new_state.my_array[row - 1][col]["row"],
                                            new_state.my_array[row - 1][col]["col"],
                                            new_state.my_array[row - 1][col]["color"],
                                            new_state.my_array[row - 1][col]["shape"],
                                            new_state.my_array[row - 1][col]["final"],
                                            new_state.my_array[row - 1][col]["move"],
                                        ),
                                    )
                                    new_state.my_array[row - 1][col] = color_square(
                                        row - 1,
                                        col,
                                        new_state.my_array[row][col]["color"],
                                        new_state.my_array[row][col]["shape"],
                                        new_state.my_array[row][col]["final"],
                                        new_state.my_array[row][col]["move"],
                                    ).square_info
                                    new_state.my_array[row][col] = const_square(
                                        row, col, "white", "⬜️"
                                    ).square_info
                                    new_state.up_reverse_square(row + 1, col)

                                else:

                                    new_state.destination_array = np.append(
                                        new_state.destination_array,
                                        color_square(
                                            new_state.my_array[row - 1][col]["row"],
                                            new_state.my_array[row - 1][col]["col"],
                                            new_state.my_array[row - 1][col]["color"],
                                            new_state.my_array[row - 1][col]["shape"],
                                            new_state.my_array[row - 1][col]["final"],
                                            new_state.my_array[row - 1][col]["move"],
                                        ),
                                    )
                                    new_state.destination_array[-1].square_info[
                                        "color"
                                    ] = new_state.my_array[row][col]["color"]
                                    new_state.my_array[row - 1][col] = color_square(
                                        row - 1,
                                        col,
                                        new_state.my_array[row][col]["color"],
                                        new_state.my_array[row][col]["shape"],
                                        new_state.my_array[row][col]["final"],
                                        new_state.my_array[row][col]["move"],
                                    ).square_info
                                    new_state.my_array[row][col] = const_square(
                                        row, col, "white", "⬜️"
                                    ).square_info
                                    new_state.up_reverse_square(row + 1, col)
        for row in range(0, new_state.size):
            for col in range(0, new_state.size):
                if (
                    new_state.my_array[row][col]["color"] != "white"
                    and new_state.my_array[row][col]["color"] != "black"
                ):
                    new_state.my_array[row][col]["move"] = False
        return new_state

    ############################################################################################################################
    @classmethod
    def down_move(cls, current_state):
        new_state = deepcopy(current_state)
        for row in range(0, new_state.size):
            for col in range(0, new_state.size):
                if (
                    new_state.my_array[row][col]["color"] == "white"
                    or new_state.my_array[row][col]["color"] == "black"
                ):
                    new_state.down_reverse_square(row - 1, col)
                    continue
                elif new_state.my_array[row][col]["final"] == True:
                    new_state.down_reverse_square(row - 1, col)
                    continue
                else:
                    if row != new_state.size - 1:
                        if new_state.down_mobility(row, col) == False:
                            new_state.down_reverse_square(row - 1, col)
                            continue
                        else:
                            new_state.my_array[row][col]["move"] = True
                            if (
                                new_state.my_array[row][col]["color"]
                                == new_state.my_array[row + 1][col]["color"]
                            ):
                                if new_state.destination_array.size == 0:
                                    new_state.my_array[row][col] = const_square(
                                        row, col, "white", "⬜️"
                                    ).square_info
                                    new_state.my_array[row + 1][col] = const_square(
                                        row + 1, col, "white", "⬜️"
                                    ).square_info
                                    new_state.down_reverse_square(row - 1, col)

                                else:
                                    for item in new_state.destination_array:
                                        if (
                                            item.square_info["row"] == row
                                            and item.square_info["col"] == col
                                        ):

                                            new_state.my_array[row + 1][col] = (
                                                const_square(
                                                    row + 1, col, "white", "⬜️"
                                                ).square_info
                                            )
                                            new_state.my_array[row][col] = color_square(
                                                item.square_info["row"],
                                                item.square_info["col"],
                                                item.square_info["color"],
                                                item.square_info["shape"],
                                                item.square_info["final"],
                                                item.square_info["move"],
                                            ).square_info
                                            index = np.where(
                                                new_state.destination_array == item
                                            )
                                            new_state.destination_array = np.delete(
                                                new_state.destination_array, index
                                            )
                                            new_state.down_reverse_square(row - 1, col)

                                            break
                                        else:
                                            new_state.my_array[row][col] = const_square(
                                                row, col, "white", "⬜️"
                                            ).square_info
                                            new_state.my_array[row + 1][col] = (
                                                const_square(
                                                    row + 1, col, "white", "⬜️"
                                                ).square_info
                                            )
                                            new_state.down_reverse_square(row - 1, col)

                            elif new_state.my_array[row + 1][col]["color"] == "black":
                                continue
                            elif new_state.my_array[row + 1][col]["color"] == "white":

                                if new_state.destination_array.size == 0:
                                    new_state.my_array[row + 1][col] = color_square(
                                        row + 1,
                                        col,
                                        new_state.my_array[row][col]["color"],
                                        new_state.my_array[row][col]["shape"],
                                        new_state.my_array[row][col]["final"],
                                        new_state.my_array[row][col]["move"],
                                    ).square_info
                                    new_state.my_array[row][col] = const_square(
                                        row, col, "white", "⬜️"
                                    ).square_info
                                    new_state.down_reverse_square(row - 1, col)

                                else:
                                    for item in new_state.destination_array:
                                        if (
                                            item.square_info["row"] == row
                                            and item.square_info["col"] == col
                                        ):
                                            if (
                                                new_state.my_array[row][col]["color"]
                                                != "white"
                                            ):
                                                new_state.my_array[row + 1][col] = (
                                                    color_square(
                                                        row + 1,
                                                        col,
                                                        new_state.my_array[row][col][
                                                            "color"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "shape"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "final"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "move"
                                                        ],
                                                    ).square_info
                                                )
                                            new_state.my_array[row][col] = color_square(
                                                item.square_info["row"],
                                                item.square_info["col"],
                                                item.square_info["color"],
                                                item.square_info["shape"],
                                                item.square_info["final"],
                                                item.square_info["move"],
                                            ).square_info
                                            index = np.where(
                                                new_state.destination_array == item
                                            )
                                            new_state.destination_array = np.delete(
                                                new_state.destination_array, index
                                            )
                                            new_state.down_reverse_square(row - 1, col)

                                            break

                                        else:
                                            if (
                                                new_state.my_array[row][col]["color"]
                                                != "white"
                                            ):
                                                new_state.my_array[row + 1][col] = (
                                                    color_square(
                                                        row + 1,
                                                        col,
                                                        new_state.my_array[row][col][
                                                            "color"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "shape"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "final"
                                                        ],
                                                        new_state.my_array[row][col][
                                                            "move"
                                                        ],
                                                    ).square_info
                                                )
                                                new_state.my_array[row][col] = (
                                                    const_square(
                                                        row, col, "white", "⬜️"
                                                    ).square_info
                                                )
                                                new_state.down_reverse_square(
                                                    row - 1, col
                                                )

                            elif new_state.my_array[row + 1][col]["final"] == False:
                                continue
                            else:
                                if new_state.my_array[row + 1][col]["shape"] != "🔶":

                                    new_state.destination_array = np.append(
                                        new_state.destination_array,
                                        color_square(
                                            new_state.my_array[row + 1][col]["row"],
                                            new_state.my_array[row + 1][col]["col"],
                                            new_state.my_array[row + 1][col]["color"],
                                            new_state.my_array[row + 1][col]["shape"],
                                            new_state.my_array[row + 1][col]["final"],
                                            new_state.my_array[row + 1][col]["move"],
                                        ),
                                    )
                                    new_state.my_array[row + 1][col] = color_square(
                                        row + 1,
                                        col,
                                        new_state.my_array[row][col]["color"],
                                        new_state.my_array[row][col]["shape"],
                                        new_state.my_array[row][col]["final"],
                                        new_state.my_array[row][col]["move"],
                                    ).square_info
                                    new_state.my_array[row][col] = const_square(
                                        row, col, "white", "⬜️"
                                    ).square_info
                                    new_state.down_reverse_square(row - 1, col)

                                else:

                                    new_state.destination_array = np.append(
                                        new_state.destination_array,
                                        color_square(
                                            new_state.my_array[row + 1][col]["row"],
                                            new_state.my_array[row + 1][col]["col"],
                                            new_state.my_array[row + 1][col]["color"],
                                            new_state.my_array[row + 1][col]["shape"],
                                            new_state.my_array[row + 1][col]["final"],
                                            new_state.my_array[row + 1][col]["move"],
                                        ),
                                    )
                                    new_state.destination_array[-1].square_info[
                                        "color"
                                    ] = new_state.my_array[row][col]["color"]
                                    new_state.my_array[row + 1][col] = color_square(
                                        row + 1,
                                        col,
                                        new_state.my_array[row][col]["color"],
                                        new_state.my_array[row][col]["shape"],
                                        new_state.my_array[row][col]["final"],
                                        new_state.my_array[row][col]["move"],
                                    ).square_info
                                    new_state.my_array[row][col] = const_square(
                                        row, col, "white", "⬜️"
                                    ).square_info
                                    new_state.down_reverse_square(row - 1, col)
        for row in range(0, new_state.size):
            for col in range(0, new_state.size):
                if (
                    new_state.my_array[row][col]["color"] != "white"
                    and new_state.my_array[row][col]["color"] != "black"
                ):
                    new_state.my_array[row][col]["move"] = False
        return new_state

    ################################################################################################################################
    def print_map(self):
        for row in self.my_array:
            print("".join(str(col["shape"]) for col in row))

    ################################################################################################################################
    def get_current_state(self):
        return self.my_array

    ################################################################################################################################
    def is_finite(self):
        for row in range(0, self.size):
            for col in range(0, self.size):
                if (
                    self.my_array[row][col]["color"] == "white"
                    or self.my_array[row][col]["color"] == "black"
                ):
                    continue
                else:
                    return False

        return True

    @classmethod
    def equals(cls, state, nextstate):

        for row in range(0, state.size):
            for col in range(0, state.size):
                if state.my_array[row][col] == nextstate.my_array[row][col]:
                    continue
                else:

                    return False
        return True

    @classmethod
    def next_state(cls, current_state):
        next_state = np.array([])
        right = state.right_move(current_state)
        if state.equals(current_state, right) == False:
            next_state = np.append(next_state, right)
        left = state.left_move(current_state)
        if state.equals(current_state, left) == False:
            next_state = np.append(next_state, left)
        up = state.up_move(current_state)
        if state.equals(current_state, up) == False:
            next_state = np.append(next_state, up)
        down = state.down_move(current_state)
        if state.equals(current_state, down) == False:
            next_state = np.append(next_state, down)
        return next_state

    
    #########################################################################################################################
    def right_reverse_square(self, i, j):
        for ind in range(j, -1, -1):
            if ( 
                
                self.my_array[i][ind]["color"] != "white"
                and self.my_array[i][ind]["color"] != "black"
            ):
                if self.my_array[i][ind]["move"] == True:
                    if (
                        self.my_array[i][ind]["color"]
                        == self.my_array[i][ind + 1]["color"]
                    ):
                        if self.destination_array.size == 0:
                            self.my_array[i][ind] = const_square(
                                i, ind, "white", "⬜️"
                            ).square_info
                            self.my_array[i][ind + 1] = const_square(
                                i, ind + 1, "white", "⬜️"
                            ).square_info
                        else:
                            for item in self.destination_array:
                                if (
                                    item.square_info["row"] == i
                                    and item.square_info["col"] == ind
                                ):

                                    self.my_array[i][ind + 1] = const_square(
                                        i, ind + 1, "white", "⬜️"
                                    ).square_info
                                    self.my_array[i][ind] = color_square(
                                        item.square_info["row"],
                                        item.square_info["col"],
                                        item.square_info["color"],
                                        item.square_info["shape"],
                                        item.square_info["final"],
                                        item.square_info["move"],
                                    ).square_info
                                    index = np.where(self.destination_array == item)
                                    self.destination_array = np.delete(
                                        self.destination_array, index
                                    )
                                    break
                                else:
                                    self.my_array[i][ind] = const_square(
                                        i, ind, "white", "⬜️"
                                    ).square_info
                                    self.my_array[i][ind + 1] = const_square(
                                        i, ind + 1, "white", "⬜️"
                                    ).square_info

                    elif self.my_array[i][ind + 1]["color"] == "black":
                        continue
                    elif self.my_array[i][ind + 1]["color"] == "white":

                        if self.destination_array.size == 0:
                            self.my_array[i][ind + 1] = color_square(
                                i,
                                ind + 1,
                                self.my_array[i][ind]["color"],
                                self.my_array[i][ind]["shape"],
                                self.my_array[i][ind]["final"],
                                self.my_array[i][ind]["move"],
                            ).square_info
                            self.my_array[i][ind] = const_square(
                                i, ind, "white", "⬜️"
                            ).square_info
                        else:
                            for item in self.destination_array:
                                if (
                                    item.square_info["row"] == i
                                    and item.square_info["col"] == ind
                                ):
                                    if self.my_array[i][ind]["color"] != "white":
                                        self.my_array[i][ind + 1] = color_square(
                                            i,
                                            ind + 1,
                                            self.my_array[i][ind]["color"],
                                            self.my_array[i][ind]["shape"],
                                            self.my_array[i][ind]["final"],
                                            self.my_array[i][ind]["move"],
                                        ).square_info
                                    self.my_array[i][ind] = color_square(
                                        item.square_info["row"],
                                        item.square_info["col"],
                                        item.square_info["color"],
                                        item.square_info["shape"],
                                        item.square_info["final"],
                                        item.square_info["move"],
                                    ).square_info
                                    index = np.where(self.destination_array == item)
                                    self.destination_array = np.delete(
                                        self.destination_array, index
                                    )
                                    break

                                else:
                                    if self.my_array[i][ind]["color"] != "white":
                                        self.my_array[i][ind + 1] = color_square(
                                            i,
                                            ind + 1,
                                            self.my_array[i][ind]["color"],
                                            self.my_array[i][ind]["shape"],
                                            self.my_array[i][ind]["final"],
                                            self.my_array[i][ind]["move"],
                                        ).square_info
                                        self.my_array[i][ind] = const_square(
                                            i, ind, "white", "⬜️"
                                        ).square_info
                    elif self.my_array[i][ind + 1]["final"] == False:
                        continue
                    else:
                        if self.my_array[i][ind + 1]["shape"] != "🔶":
                            self.destination_array = np.append(
                                self.destination_array,
                                color_square(
                                    self.my_array[i][ind + 1]["row"],
                                    self.my_array[i][ind + 1]["col"],
                                    self.my_array[i][ind + 1]["color"],
                                    self.my_array[i][ind + 1]["shape"],
                                    self.my_array[i][ind + 1]["final"],
                                    self.my_array[i][ind + 1]["move"],
                                ),
                            )
                            self.my_array[i][ind + 1] = color_square(
                                i,
                                ind + 1,
                                self.my_array[i][ind]["color"],
                                self.my_array[i][ind]["shape"],
                                self.my_array[i][ind]["final"],
                                self.my_array[i][ind]["move"],
                            ).square_info
                            self.my_array[i][ind] = const_square(
                                i, ind, "white", "⬜️"
                            ).square_info
                        else:
                            self.destination_array = np.append(
                                self.destination_array,
                                color_square(
                                    self.my_array[i][ind + 1]["row"],
                                    self.my_array[i][ind + 1]["col"],
                                    self.my_array[i][ind + 1]["color"],
                                    self.my_array[i][ind + 1]["shape"],
                                    self.my_array[i][ind + 1]["final"],
                                    self.my_array[i][ind + 1]["move"],
                                ),
                            )
                            self.destination_array[-1].square_info["color"] = (
                                self.my_array[i][ind]["color"]
                            )
                            self.my_array[i][ind + 1] = color_square(
                                i,
                                ind + 1,
                                self.my_array[i][ind]["color"],
                                self.my_array[i][ind]["shape"],
                                self.my_array[i][ind]["final"],
                                self.my_array[i][ind]["move"],
                            ).square_info
                            self.my_array[i][ind] = const_square(
                                i, ind, "white", "⬜️"
                            ).square_info

            else:
                break

    #########################################################################################################################
    def left_reverse_square(self, i, j):
        for ind in range(j, self.size, +1):
            if (
                self.my_array[i][ind]["color"] != "white"
                and self.my_array[i][ind]["color"] != "black"
            ):
                if self.my_array[i][ind]["move"] == True:
                    if (
                        self.my_array[i][ind]["color"]
                        == self.my_array[i][ind - 1]["color"]
                    ):
                        if self.destination_array.size == 0:
                            self.my_array[i][ind] = const_square(
                                i, ind, "white", "⬜️"
                            ).square_info
                            self.my_array[i][ind - 1] = const_square(
                                i, ind - 1, "white", "⬜️"
                            ).square_info
                        else:
                            for item in self.destination_array:
                                if (
                                    item.square_info["row"] == i
                                    and item.square_info["col"] == ind
                                ):

                                    self.my_array[i][ind - 1] = const_square(
                                        i, ind - 1, "white", "⬜️"
                                    ).square_info
                                    self.my_array[i][ind] = color_square(
                                        item.square_info["row"],
                                        item.square_info["col"],
                                        item.square_info["color"],
                                        item.square_info["shape"],
                                        item.square_info["final"],
                                        item.square_info["move"],
                                    ).square_info
                                    index = np.where(self.destination_array == item)
                                    self.destination_array = np.delete(
                                        self.destination_array, index
                                    )
                                    break
                                else:
                                    self.my_array[i][ind] = const_square(
                                        i, ind, "white", "⬜️"
                                    ).square_info
                                    self.my_array[i][ind - 1] = const_square(
                                        i, ind - 1, "white", "⬜️"
                                    ).square_info

                    elif self.my_array[i][ind - 1]["color"] == "black":
                        continue
                    elif self.my_array[i][ind - 1]["color"] == "white":

                        if self.destination_array.size == 0:
                            self.my_array[i][ind - 1] = color_square(
                                i,
                                ind - 1,
                                self.my_array[i][ind]["color"],
                                self.my_array[i][ind]["shape"],
                                self.my_array[i][ind]["final"],
                                self.my_array[i][ind]["move"],
                            ).square_info
                            self.my_array[i][ind] = const_square(
                                i, ind, "white", "⬜️"
                            ).square_info
                        else:
                            for item in self.destination_array:
                                if (
                                    item.square_info["row"] == i
                                    and item.square_info["col"] == ind
                                ):
                                    if self.my_array[i][ind]["color"] != "white":
                                        self.my_array[i][ind - 1] = color_square(
                                            i,
                                            ind + 1,
                                            self.my_array[i][ind]["color"],
                                            self.my_array[i][ind]["shape"],
                                            self.my_array[i][ind]["final"],
                                            self.my_array[i][ind]["move"],
                                        ).square_info
                                    self.my_array[i][ind] = color_square(
                                        item.square_info["row"],
                                        item.square_info["col"],
                                        item.square_info["color"],
                                        item.square_info["shape"],
                                        item.square_info["final"],
                                        item.square_info["move"],
                                    ).square_info
                                    index = np.where(self.destination_array == item)
                                    self.destination_array = np.delete(
                                        self.destination_array, index
                                    )
                                    break

                                else:
                                    if self.my_array[i][ind]["color"] != "white":
                                        self.my_array[i][ind - 1] = color_square(
                                            i,
                                            ind - 1,
                                            self.my_array[i][ind]["color"],
                                            self.my_array[i][ind]["shape"],
                                            self.my_array[i][ind]["final"],
                                            self.my_array[i][ind]["move"],
                                        ).square_info
                                        self.my_array[i][ind] = const_square(
                                            i, ind, "white", "⬜️"
                                        ).square_info
                    elif self.my_array[i][ind - 1]["final"] == False:
                        continue
                    else:
                        if self.my_array[i][ind - 1]["shape"] != "🔶":
                            self.destination_array = np.append(
                                self.destination_array,
                                color_square(
                                    self.my_array[i][ind - 1]["row"],
                                    self.my_array[i][ind - 1]["col"],
                                    self.my_array[i][ind - 1]["color"],
                                    self.my_array[i][ind - 1]["shape"],
                                    self.my_array[i][ind - 1]["final"],
                                    self.my_array[i][ind - 1]["move"],
                                ),
                            )
                            self.my_array[i][ind - 1] = color_square(
                                i,
                                ind - 1,
                                self.my_array[i][ind]["color"],
                                self.my_array[i][ind]["shape"],
                                self.my_array[i][ind]["final"],
                                self.my_array[i][ind]["move"],
                            ).square_info
                            self.my_array[i][ind] = const_square(
                                i, ind, "white", "⬜️"
                            ).square_info
                        else:
                            self.destination_array = np.append(
                                self.destination_array,
                                color_square(
                                    self.my_array[i][ind - 1]["row"],
                                    self.my_array[i][ind - 1]["col"],
                                    self.my_array[i][ind - 1]["color"],
                                    self.my_array[i][ind - 1]["shape"],
                                    self.my_array[i][ind - 1]["final"],
                                    self.my_array[i][ind - 1]["move"],
                                ),
                            )
                            self.destination_array[-1].square_info["color"] = (
                                self.my_array[i][ind]["color"]
                            )
                            self.my_array[i][ind - 1] = color_square(
                                i,
                                ind - 1,
                                self.my_array[i][ind]["color"],
                                self.my_array[i][ind]["shape"],
                                self.my_array[i][ind]["final"],
                                self.my_array[i][ind]["move"],
                            ).square_info
                            self.my_array[i][ind] = const_square(
                                i, ind, "white", "⬜️"
                            ).square_info

            else:
                break

    ####################################################################################################################
    def up_reverse_square(self, i, j):
        for ind in range(i, self.size, +1):
            if (
                self.my_array[ind][j]["color"] != "white"
                and self.my_array[ind][j]["color"] != "black"
            ):
                if self.my_array[ind][j]["move"] == True:
                    if (
                        self.my_array[ind][j]["color"]
                        == self.my_array[ind - 1][j]["color"]
                    ):
                        if self.destination_array.size == 0:
                            self.my_array[ind][j] = const_square(
                                ind, j, "white", "⬜️"
                            ).square_info
                            self.my_array[ind - 1][j] = const_square(
                                ind - 1, j, "white", "⬜️"
                            ).square_info
                        else:
                            for item in self.destination_array:
                                if (
                                    item.square_info["row"] == ind
                                    and item.square_info["col"] == j
                                ):

                                    self.my_array[ind - 1][j] = const_square(
                                        ind - 1, j, "white", "⬜️"
                                    ).square_info
                                    self.my_array[ind][j] = color_square(
                                        item.square_info["row"],
                                        item.square_info["col"],
                                        item.square_info["color"],
                                        item.square_info["shape"],
                                        item.square_info["final"],
                                        item.square_info["move"],
                                    ).square_info
                                    index = np.where(self.destination_array == item)
                                    self.destination_array = np.delete(
                                        self.destination_array, index
                                    )
                                    break
                                else:
                                    self.my_array[ind][j] = const_square(
                                        ind, j, "white", "⬜️"
                                    ).square_info
                                    self.my_array[ind - 1][j] = const_square(
                                        ind - 1, j, "white", "⬜️"
                                    ).square_info

                    elif self.my_array[ind - 1][j]["color"] == "black":
                        continue
                    elif self.my_array[ind - 1][j]["color"] == "white":

                        if self.destination_array.size == 0:
                            self.my_array[ind - 1][j] = color_square(
                                ind - 1,
                                j,
                                self.my_array[ind][j]["color"],
                                self.my_array[ind][j]["shape"],
                                self.my_array[ind][j]["final"],
                                self.my_array[ind][j]["move"],
                            ).square_info
                            self.my_array[ind][j] = const_square(
                                ind, j, "white", "⬜️"
                            ).square_info
                        else:
                            for item in self.destination_array:
                                if (
                                    item.square_info["row"] == ind
                                    and item.square_info["col"] == j
                                ):
                                    if self.my_array[ind][j]["color"] != "white":
                                        self.my_array[ind - 1][j] = color_square(
                                            ind - 1,
                                            j,
                                            self.my_array[ind][j]["color"],
                                            self.my_array[ind][j]["shape"],
                                            self.my_array[ind][j]["final"],
                                            self.my_array[ind][j]["move"],
                                        ).square_info
                                    self.my_array[ind][j] = color_square(
                                        item.square_info["row"],
                                        item.square_info["col"],
                                        item.square_info["color"],
                                        item.square_info["shape"],
                                        item.square_info["final"],
                                        item.square_info["move"],
                                    ).square_info
                                    index = np.where(self.destination_array == item)
                                    self.destination_array = np.delete(
                                        self.destination_array, index
                                    )
                                    break

                                else:
                                    if self.my_array[ind][j]["color"] != "white":
                                        self.my_array[ind - 1][j] = color_square(
                                            ind - 1,
                                            j,
                                            self.my_array[ind][j]["color"],
                                            self.my_array[ind][j]["shape"],
                                            self.my_array[ind][j]["final"],
                                            self.my_array[ind][j]["move"],
                                        ).square_info
                                        self.my_array[ind][j] = const_square(
                                            ind, j, "white", "⬜️"
                                        ).square_info
                    elif self.my_array[ind - 1][j]["final"] == False:
                        continue
                    else:
                        if self.my_array[ind - 1][j]["shape"] != "🔶":
                            self.destination_array = np.append(
                                self.destination_array,
                                color_square(
                                    self.my_array[ind - 1][j]["row"],
                                    self.my_array[ind - 1][j]["col"],
                                    self.my_array[ind - 1][j]["color"],
                                    self.my_array[ind - 1][j]["shape"],
                                    self.my_array[ind - 1][j]["final"],
                                    self.my_array[ind - 1][j]["move"],
                                ),
                            )
                            self.my_array[ind - 1][j] = color_square(
                                ind - 1,
                                j,
                                self.my_array[ind][j]["color"],
                                self.my_array[ind][j]["shape"],
                                self.my_array[ind][j]["final"],
                                self.my_array[ind][j]["move"],
                            ).square_info
                            self.my_array[ind][j] = const_square(
                                ind, j, "white", "⬜️"
                            ).square_info
                        else:
                            self.destination_array = np.append(
                                self.destination_array,
                                color_square(
                                    self.my_array[ind - 1][j]["row"],
                                    self.my_array[ind - 1][j]["col"],
                                    self.my_array[ind - 1][j]["color"],
                                    self.my_array[ind - 1][j]["shape"],
                                    self.my_array[ind - 1][j]["final"],
                                    self.my_array[ind  -1][j]["move"],
                                ),
                            )
                            self.destination_array[-1].square_info["color"] = (
                                self.my_array[ind][j]["color"]
                            )
                            self.my_array[ind - 1][j] = color_square(
                                ind - 1,
                                j,
                                self.my_array[ind][j]["color"],
                                self.my_array[ind][j]["shape"],
                                self.my_array[ind][j]["final"],
                                self.my_array[ind][j]["move"],
                            ).square_info
                            self.my_array[ind][j] = const_square(
                                ind, j, "white", "⬜️"
                            ).square_info

            else:
                break
        ####################################################################################################################

    def down_reverse_square(self, i, j):
        for ind in range(i, -1, -1):
            if (
                self.my_array[ind][j]["color"] != "white"
                and self.my_array[ind][j]["color"] != "black"
            ):
                if self.my_array[ind][j]["move"] == True:
                    if (
                        self.my_array[ind][j]["color"]
                        == self.my_array[ind + 1][j]["color"]
                    ):
                        if self.destination_array.size == 0:
                            self.my_array[ind][j] = const_square(
                                ind, j, "white", "⬜️"
                            ).square_info
                            self.my_array[ind + 1][j] = const_square(
                                ind + 1, j, "white", "⬜️"
                            ).square_info
                        else:
                            for item in self.destination_array:
                                if (
                                    item.square_info["row"] == ind
                                    and item.square_info["col"] == j
                                ):

                                    self.my_array[ind + 1][j] = const_square(
                                        ind + 1, j, "white", "⬜️"
                                    ).square_info
                                    self.my_array[ind][j] = color_square(
                                        item.square_info["row"],
                                        item.square_info["col"],
                                        item.square_info["color"],
                                        item.square_info["shape"],
                                        item.square_info["final"],
                                        item.square_info["move"],
                                    ).square_info
                                    index = np.where(self.destination_array == item)
                                    self.destination_array = np.delete(
                                        self.destination_array, index
                                    )
                                    break
                                else:
                                    self.my_array[ind][j] = const_square(
                                        ind, j, "white", "⬜️"
                                    ).square_info
                                    self.my_array[ind + 1][j] = const_square(
                                        ind + 1, j, "white", "⬜️"
                                    ).square_info

                    elif self.my_array[ind + 1][j]["color"] == "black":
                        continue
                    elif self.my_array[ind + 1][j]["color"] == "white":

                        if self.destination_array.size == 0:
                            self.my_array[ind + 1][j] = color_square(
                                ind + 1,
                                j,
                                self.my_array[ind][j]["color"],
                                self.my_array[ind][j]["shape"],
                                self.my_array[ind][j]["final"],
                                self.my_array[ind][j]["move"],
                            ).square_info
                            self.my_array[ind][j] = const_square(
                                ind, j, "white", "⬜️"
                            ).square_info
                        else:
                            for item in self.destination_array:
                                if (
                                    item.square_info["row"] == ind
                                    and item.square_info["col"] == j
                                ):
                                    if self.my_array[ind][j]["color"] != "white":
                                        self.my_array[ind + 1][j] = color_square(
                                            ind + 1,
                                            j,
                                            self.my_array[ind][j]["color"],
                                            self.my_array[ind][j]["shape"],
                                            self.my_array[ind][j]["final"],
                                            self.my_array[ind][j]["move"],
                                        ).square_info
                                    self.my_array[ind][j] = color_square(
                                        item.square_info["row"],
                                        item.square_info["col"],
                                        item.square_info["color"],
                                        item.square_info["shape"],
                                        item.square_info["final"],
                                        item.square_info["move"],
                                    ).square_info
                                    index = np.where(self.destination_array == item)
                                    self.destination_array = np.delete(
                                        self.destination_array, index
                                    )
                                    break

                                else:
                                    if self.my_array[ind][j]["color"] != "white":
                                        self.my_array[ind + 1][j] = color_square(
                                            ind + 1,
                                            j,
                                            self.my_array[ind][j]["color"],
                                            self.my_array[ind][j]["shape"],
                                            self.my_array[ind][j]["final"],
                                            self.my_array[ind][j]["move"],
                                        ).square_info
                                        self.my_array[ind][j] = const_square(
                                            ind, j, "white", "⬜️"
                                        ).square_info
                    elif self.my_array[ind + 1][j]["final"] == False:
                        continue
                    else:
                        if self.my_array[ind + 1][j]["shape"] != "🔶":
                            self.destination_array = np.append(
                                self.destination_array,
                                color_square(
                                    self.my_array[ind + 1][j]["row"],
                                    self.my_array[ind + 1][j]["col"],
                                    self.my_array[ind + 1][j]["color"],
                                    self.my_array[ind + 1][j]["shape"],
                                    self.my_array[ind + 1][j]["final"],
                                    self.my_array[ind + 1][j]["move"],
                                ),
                            )
                            self.my_array[ind + 1][j] = color_square(
                                ind + 1,
                                j,
                                self.my_array[ind][j]["color"],
                                self.my_array[ind][j]["shape"],
                                self.my_array[ind][j]["final"],
                                self.my_array[ind][j]["move"],
                            ).square_info
                            self.my_array[ind][j] = const_square(
                                ind, j, "white", "⬜️"
                            ).square_info
                        else:
                            self.destination_array = np.append(
                                self.destination_array,
                                color_square(
                                    self.my_array[ind + 1][j]["row"],
                                    self.my_array[ind + 1][j]["col"],
                                    self.my_array[ind + 1][j]["color"],
                                    self.my_array[ind + 1][j]["shape"],
                                    self.my_array[ind + 1][j]["final"],
                                    self.my_array[ind + 1][j]["move"],
                                ),
                            )
                            self.destination_array[-1].square_info["color"] = (
                                self.my_array[ind][j]["color"]
                            )
                            self.my_array[ind + 1][j] = color_square(
                                ind + 1,
                                j,
                                self.my_array[ind][j]["color"],
                                self.my_array[ind][j]["shape"],
                                self.my_array[ind][j]["final"],
                                self.my_array[ind][j]["move"],
                            ).square_info
                            self.my_array[ind][j] = const_square(
                                ind, j, "white", "⬜️"
                            ).square_info

            else:
                break


"""
    @classmethod
    def create_all_possible_next_states(cls, state):
        cls.creat_possible_next_state(state)
        if state.right_mobility == True:
            cls.creat_possible_next_state(state.get_next_state("r"))

            state.next_states_array = np.append(
                state.next_states_array,
            )
            cls.create_all_possible_next_states(state.get_next_state("r"))
        if state.left_mobility == True:
            cls.creat_possible_next_state(state.get_next_state("l"))
            next = cls.create_all_possible_next_states(state.get_next_state("l"))
            state.next_states_array = np.append(state.next_states_array, next)
        if state.up_mobility == True:
            cls.creat_possible_next_state(state.get_next_state("u"))
            next = cls.create_all_possible_next_states(state.get_next_state("u"))
            state.next_states_array = np.append(state.next_states_array, next)
        if state.down_mobility == True:
            cls.creat_possible_next_state(state.get_next_state("d"))
            next = cls.create_all_possible_next_states(state.get_next_state("d"))
            state.next_states_array = np.append(state.next_states_array, next)

        return state.next_states_array


a = np.array([])
b = np.append(a, [1, 2, 3])
"""
