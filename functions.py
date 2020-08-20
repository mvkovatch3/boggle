import numpy as np


def get_board(special=False):

    dice = np.array(
        [
            ["A", "A", "F", "I", "R", "S"],
            ["A", "E", "E", "E", "E", "M"],
            ["E", "M", "O", "T", "T", "T"],
            ["F", "I", "P", "R", "S", "Y"],
            ["D", "D", "H", "N", "O", "T"],
            ["A", "E", "E", "G", "M", "U"],
            ["D", "H", "H", "L", "N", "O"],
            ["C", "C", "E", "N", "S", "T"],
            ["A", "F", "I", "R", "S", "Y"],
            ["O", "O", "O", "T", "T", "U"],
            ["I", "K", "L", "Qu", "U", "W"],
            ["A", "E", "G", "M", "N", "N"],
            ["A", "A", "A", "F", "R", "S"],
            ["N", "O", "O", "T", "U", "W"],
            ["C", "E", "I", "I", "L", "T"],
            ["B", "J", "K", "Qu", "X", "Z"],
            ["E", "N", "S", "S", "S", "U"],
            ["D", "H", "H", "L", "O", "R"],
            ["D", "H", "L", "N", "O", "R"],
            ["E", "I", "I", "I", "T", "T"],
            ["A", "A", "E", "E", "E", "E"],
            ["A", "D", "E", "N", "N", "N"],
            ["C", "E", "I", "P", "S", "T"],
            ["C", "E", "I", "L", "P", "T"],
            ["G", "O", "R", "R", "V", "W"],
        ]
    )

    if special:
        special_die = np.array(["He", "An", "In", "Er", "Th", "Qu"])
        dice[np.random.choice(25, 1)] = special_die
    letter_inds = [
        [np.random.choice(25, 25, replace=False)],
        [np.random.choice(5, 25)],
    ]
    board = dice[tuple(letter_inds)].flatten()

    return board
