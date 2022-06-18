if __name__ == '__main__':
    for num in range(10000):
        num_address = id(num)
        for _ in range(10):
            new_num_address = num + num - num
            if id(new_num_address) != num_address:
                print(num, " 여기부터는 새롭게 할당됩니다.")
                exit()