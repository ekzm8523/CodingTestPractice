import asyncio

async def test1():
    global tmp
    tmp = 2


async def test2():
    global tmp
    tmp = None

async def main():
    # task1 = asyncio.create_task(test1())
    await test1()
    print(tmp)
    # task2 = asyncio.create_task(test2())
    await test2()
    print(tmp)

if __name__ == '__main__':

    asyncio.run(main())