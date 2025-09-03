def solution(keyinput, board):
    x = y = 0
    x_lim, y_lim = board[0] // 2, board[1] // 2

    for k in keyinput:
        if k == "left":   x -= 1
        elif k == "right": x += 1
        elif k == "up":    y += 1
        elif k == "down":  y -= 1

        x = max(-x_lim, min(x, x_lim))
        y = max(-y_lim, min(y, y_lim))

    return [x, y]
