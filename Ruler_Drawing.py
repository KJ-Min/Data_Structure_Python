def draw_ruler(n_inches, major_length):
    draw_line(major_length, 0)
    for j in range(1, n_inches + 1):
        draw_interval(major_length - 1)
        draw_line(major_length, j)


def draw_interval(central_length):
    if central_length >= 1:
        result = 0
        for j in range(central_length):
            result = result * 2 + 1

        for k in range(1, result + 1):
            if k % 2 == 1:
                draw_line(1)
            else:
                for i in range(central_length - 1):
                    if k % (4 * (2**i)) == 2 ** (i + 1):
                        draw_line(i + 2)


def draw_line(tick_length, tick_label=-1):
    print("-" * tick_length, end="")
    if tick_label >= 0:
        print(" " + str(tick_label), end="")
    print()


draw_ruler(1, 5)
