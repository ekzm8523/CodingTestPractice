def main():
    alpha = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    str2int = {ch: i for i, ch in enumerate(alpha)}
    int2str = {i: ch for i, ch in enumerate(alpha)}
    a, b = map(int, input().split())
    encoding_message = input()
    answer = []

    for ch in encoding_message:
        num = str2int[ch]
        idx = 0
        while (num + idx * 26 - b) % a != 0:
            idx += 1
        encoded_ch = (num + idx * 26 - b) // a
        answer.append(int2str[encoded_ch])
    print(''.join(answer))


if __name__ == "__main__":
    main()