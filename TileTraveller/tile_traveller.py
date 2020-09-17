# Map Layout y*x -> 7 * 13 (6 * 12 from 0) and P is player start pos = 73
UNDER_UPPER = 14
LEFT_RIGHT = 2

MOVE_DOWN_UP = 2 * UNDER_UPPER
MOVE_LEFT_RIGHT = 2 * LEFT_RIGHT

MAP = """
# # # # # # #
#   O   O   #
# O # # # O #
# P O   #   #
# O # O # O #
# P #   #   #
# # # # # # #
"""


def check_surrounding(player_pos):
    av = []
    if MAP[player_pos - UNDER_UPPER] == "O":
        av.append('north')
    if MAP[player_pos + LEFT_RIGHT] == "O":
        av.append('east')
    if MAP[player_pos + UNDER_UPPER] == "O":
        av.append('south')
    if MAP[player_pos - LEFT_RIGHT] == "O":
        av.append('west')
    return av


def map_move(direction, player_pos, x, y):
    if direction == 'north':
        player_pos -= MOVE_DOWN_UP
        y += 1
    elif direction == 'south':
        player_pos += MOVE_DOWN_UP
        y -= 1
    elif direction == 'east':
        player_pos += MOVE_LEFT_RIGHT
        x += 1
    elif direction == 'west':
        player_pos -= MOVE_LEFT_RIGHT
        x -= 1
    return player_pos, x, y


def get_moves(av_moves):
    r_str = ""
    if len(av_moves) == 1:
        return "({}){}.".format(av_moves[0][0].upper(), av_moves[0][1:])
    else:
        for m in av_moves:
            if av_moves.index(m) < len(av_moves) - 1:
                r_str += "({}){} or ".format(m[0].upper(), m[1:])
            else:
                r_str += "({}){}.".format(m[0].upper(), m[1:])
        return r_str


player_map_pos = 73
pos_x = 1
pos_y = 1

while True:
    av_moves = check_surrounding(player_map_pos)
    print("You can travel: {}".format(get_moves(av_moves)))

    choice = input("Direction: ")

    for move in av_moves:
        if choice.lower() == move[0]:
            player_map_pos, pos_x, pos_y = map_move(move, player_map_pos, pos_x, pos_y)
            break
    else:
        print("Not a valid direction!")

    if (pos_x == 3) and (pos_y == 1):
        print("Victory!")
        break
