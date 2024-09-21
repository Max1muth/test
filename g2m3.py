from tkinter import *

""" Своеобразная пасхалка """

ball = {"x": 500, "y": 30}
moveSide = {"x": True, "y": True}
platformX = [310, 390]
gameActive = True
score = 0

window = Tk()
window.geometry("700x700")
window.resizable(False, False)
window.title("arkanoid")

board = Canvas(window, bg="silver")
board.pack(fill=BOTH, expand=True)


def draw(event):
    global platformX
    platformX[0] = event.x - 40
    platformX[1] = event.x + 40


def move():
    global gameActive
    global ball
    global moveSide
    global platformX
    global score
    board.delete("all")
    if moveSide["x"]:
        ball["x"] += 15
    else:
        ball["x"] -= 15
    if moveSide["y"]:
        ball["y"] += 10
    else:
        ball["y"] -= 10
    if ball["x"] > 680 or ball["x"] < 20:
        moveSide["x"] = not moveSide["x"]
    if ball["y"] < 20:
        moveSide["y"] = not moveSide["y"]
    if ball["y"] >= 680:
        gameActive = False
    if ball["y"] == 640 and ball["x"] in range(platformX[0], platformX[1]):
        moveSide["y"] = not moveSide["y"]
        score += 1

    board.create_oval(ball["x"] - 10, ball["y"] - 10, ball["x"] + 10, ball["y"] + 10, fill="red")
    board.create_rectangle(platformX[0], 646, platformX[1], 666, fill="red")
    board.create_text(50, 20, text=f"Счет: {score}", fill="black")

    if gameActive:
        board.after(20, move)


move()
board.bind("<Motion>", draw)
window.mainloop()
