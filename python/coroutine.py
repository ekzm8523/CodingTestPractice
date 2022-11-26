import dis
import inspect
import opcode
frame = None


def func():
    x = 10
    y = 20
    print(x + y)
    global frame
    frame = inspect.currentframe()

def generator():
    global frame
    frame = inspect.currentframe()
    recv = yield 1

    return recv


async def coroutine():
    pass

if __name__ == '__main__':
    func()
    print(frame)  # func 메서드의 stack frame 정보
    print("*" * 50)
    print("func 메서드의 low level 명령어")
    print(dis.dis(func))  # func 메서드의
    print("*" * 50)
    print("func 메서드의 byte code")
    print(func.__code__.co_code)  # func의 byte 배열
    print("*" * 50)
    print("byte 배열을 알아볼 수 있게 변경")
    print(list(func.__code__.co_code))  # byte를 알아볼 수 있게 변경
    print("명령어, value의 pair로 출력 된 모습")
    print(f"instruction 100 == {opcode.opname[100]}")

    gen = generator()
    print(gen.send(None))
    lasti = gen.gi_frame.f_lasti
    print(lasti)
    code = gen.gi_code
    print(code is gen.gi_frame.f_code)

    print(opcode.opname[generator.__code__.co_code[lasti]])
