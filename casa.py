import turtle

# ------------------------------ CONFIG TELA ------------------------------
screen = turtle.Screen()
screen.title("Casa com Árvore Realista - Atividade Guiada")
screen.setup(width=900, height=700)
screen.bgcolor("skyblue")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(2)

# ------------------------------ FUNÇÕES AUXILIARES ------------------------------

def draw_rectangle(t, x, y, w, h, fill_color, border_color="black"):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(border_color, fill_color)
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

def draw_triangle(t, x, y, w, h, fill_color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black", fill_color)
    t.begin_fill()
    t.goto(x + w/2, y + h)
    t.goto(x + w, y)
    t.goto(x, y)
    t.end_fill()

# ------------------------------ CASA ------------------------------

def draw_house_base(t, x, y, w=260, h=180, color="cornsilk"):
    draw_rectangle(t, x, y, w, h, color)

def draw_roof(t, x, y, w=260, h=100, color="firebrick"):
    draw_triangle(t, x, y, w, h, color)

def draw_door(t, x, y, w=60, h=100, color="sienna"):
    draw_rectangle(t, x, y, w, h, color)
    t.penup()
    t.goto(x + w - 12, y + h/2)
    t.dot(10, "gold")

def draw_window(t, x, y, size=60, color="lightblue"):
    draw_rectangle(t, x, y, size, size, "white")
    inset = 6
    draw_rectangle(t, x + inset, y + inset, size - 2*inset, size - 2*inset, color)

    # cruz
    t.penup()
    t.goto(x + size/2, y + inset)
    t.pendown()
    t.goto(x + size/2, y + size - inset)

    t.penup()
    t.goto(x + inset, y + size/2)
    t.pendown()
    t.goto(x + size - inset, y + size/2)

# ------------------------------ ÁRVORE REALISTA ------------------------------

def draw_leaf_cluster(t, x, y, radius, color):
    """Desenha um grupo de folhas com formato mais natural."""
    t.penup()
    t.goto(x, y)
    t.color("black", color)
    t.begin_fill()
    t.pendown()

    for _ in range(6):
        t.circle(radius)
        t.left(60)

    t.end_fill()

def draw_realistic_tree(t, x, y):
    # ------- TRONCO REALISTA -------
    t.color("sienna4", "sienna4")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()

    # tronco irregular natural
    t.goto(x + 30, y)
    t.goto(x + 40, y + 120)
    t.goto(x + 10, y + 140)
    t.goto(x - 20, y + 120)
    t.goto(x - 10, y)
    t.goto(x, y)

    t.end_fill()

    # ------- CAMADAS DE FOLHAS -------
    leaf_colors = ["forestgreen", "limegreen", "seagreen", "darkgreen"]

    # Inferior
    draw_leaf_cluster(t, x - 20, y + 120, 45, leaf_colors[0])
    draw_leaf_cluster(t, x + 20, y + 130, 50, leaf_colors[1])

    # Intermediária
    draw_leaf_cluster(t, x - 10, y + 180, 40, leaf_colors[2])
    draw_leaf_cluster(t, x + 25, y + 170, 35, leaf_colors[0])

    # Topo
    draw_leaf_cluster(t, x + 5, y + 230, 30, leaf_colors[3])

# ------------------------------ GRAMADO ------------------------------

def draw_lawn(t):
    draw_rectangle(t, -500, -250, 1000, 180, "lightgreen", "lightgreen")

# ------------------------------ CASA COMPLETA ------------------------------

def draw_complete_house(t, base_x=-130, base_y=-80):
    base_w = 260
    base_h = 180

    draw_house_base(t, base_x, base_y, base_w, base_h)
    draw_roof(t, base_x, base_y + base_h, base_w, 100)

    # porta
    door_w, door_h = 70, 110
    draw_door(t, base_x + (base_w - door_w)/2, base_y, door_w, door_h)

    # janelas
    win = 60
    draw_window(t, base_x + 25, base_y + 90, win)
    draw_window(t, base_x + base_w - win - 25, base_y + 90, win)

# ------------------------------ MAIN ------------------------------

def main():
    pen.speed(3)
    draw_lawn(pen)
    draw_complete_house(pen)

    # Árvore realista afastada
    draw_realistic_tree(pen, 330, -80)

    pen.penup()
    pen.goto(300, 260)
    pen.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
