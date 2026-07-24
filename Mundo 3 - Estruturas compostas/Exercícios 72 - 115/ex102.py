def fatorial(n, show=False):

    f = 1

    for c in range(n, 0, -1):
        f *= c

        if show:
            print(f"{c} ", end="x " if c > 1 else f"= {f} ")


    if not show:
        print(f"O fatorial de {n} é: {f} ")


fatorial(5, show=True)