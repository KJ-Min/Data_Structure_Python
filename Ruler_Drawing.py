def draw_ruler(n_inches, major_length):
    draw_line(major_length, 0)
    for j in range(1, n_inches + 1):
        draw_interval(major_length - 1)
        draw_line(major_length, j)


def draw_interval(central_length):
    if central_length >= 1:
        draw_interval(central_length - 1)
        draw_line(central_length)
        draw_interval(central_length - 1)


def draw_line(tick_length, tick_label=-1):
    print("-" * tick_length, end="")
    if tick_label >= 0:
        print(" " + str(tick_label), end="")
    print()


draw_ruler(1, 5)
