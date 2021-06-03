def solution(com_code, day, data):
    answer = []

    for d in data:
        price, code, time = d.split()
        price = price.rsplit('=')[-1]
        code = code.rsplit('=')[-1]
        time = time.rsplit('=')[-1]

        if com_code == code and day in time:
            answer.append((int(price), time))
    answer = sorted(answer, key= lambda x: x[1])
    answer = [x for x, y in answer]
    return answer

if __name__ == "__main__":
    company_code = "012345"
    day = "20190620"
    data = ["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]
    print(solution(company_code, day, data))