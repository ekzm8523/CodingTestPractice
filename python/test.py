
if __name__ == "__main__":

    n = int(1e6)
    x = 1
    while (2**x) < n:
        x += 1
    print(x)