# https://www.acmicpc.net/problem/3425
"""
NUM X: X를 스택의 가장 위에 저장한다. (0 ≤ X ≤ 109)
POP: 스택 가장 위의 숫자를 제거한다.
INV: 첫 번째 수의 부호를 바꾼다. (42 -> -42)
DUP: 첫 번째 숫자를 하나 더 스택의 가장 위에 저장한다.
SWP: 첫 번째 숫자와 두 번째 숫자의 위치를 서로 바꾼다.
ADD: 첫 번째 숫자와 두 번째 숫자를 더한다.
SUB: 첫 번째 숫자와 두 번째 숫자를 뺀다. (두 번째 - 첫 번째)
MUL: 첫 번째 숫자와 두 번째 숫자를 곱한다.
DIV: 첫 번째 숫자로 두 번째 숫자를 나눈 몫을 저장한다. 두 번째 숫자가 피제수, 첫 번째 숫자가 제수이다.
MOD: 첫 번째 숫자로 두 번째 숫자를 나눈 나머지를 저장한다. 두 번째 숫자가 피제수, 첫 번째 숫자가 제수이다
숫자가 부족해서 연산을 수행할 수 없을 때, 0으로 나눴을 때 (DIV, MOD), 연산 결과의 절댓값이 109를 넘어갈 때는 모두 프로그램 에러이다.
프로그램 에러가 발생했을 경우에는, 현재 프로그램의 수행을 멈추고, 그 다음 어떤 명령도 수행하지 않는다.
"""
from importlib import import_module
import sys
INF = int(1e9)
class go_stack:
    def __init__(self, num):
        self.stack = [num]
        self.is_error = False


    def NUM(self, num):
        self.stack.append(num)


    def POP(self):
        if self.stack:
            self.stack.pop()
        else:
            self.is_error = True


    def INV(self):
        if self.stack:
            self.stack[-1] = -self.stack[-1]
        else:
            self.is_error = True


    def DUP(self):
        if self.stack:
            self.stack.append(self.stack[-1])
        else:
            self.is_error = True


    def SWP(self):
        if len(self.stack) >= 2:
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
        else:
            self.is_error = True


    def ADD(self):
        if len(self.stack) >= 2:
            tmp = self.stack.pop()
            self.stack[-1] += tmp
            if self.stack[-1] > INF:
                self.is_error = True
        else:
            self.is_error = True


    def SUB(self):
        if len(self.stack) >= 2:
            tmp = self.stack.pop()
            self.stack[-1] -= tmp
            if self.stack[-1] > INF:
                self.is_error = True
        else:
            self.is_error = True


    def MUL(self):
        if len(self.stack) >= 2:
            tmp = self.stack.pop()
            self.stack[-1] *= tmp
            if self.stack[-1] > INF:
                self.is_error = True
        else:
            self.is_error = True


    def DIV(self):
        if len(self.stack) >= 2:
            tmp = self.stack.pop()
            if tmp == 0:
                self.is_error = True
                return
            self.stack[-1] //= tmp
        else:
            self.is_error = True


    def MOD(self):
        if len(self.stack) >= 2:
            tmp = self.stack.pop()
            if tmp == 0:
                self.is_error = True
                return
            self.stack[-1] %= tmp
        else:
            self.is_error = True



if __name__ == "__main__":


    is_quit = False
    is_program = True
    while True:
        program = []

        while True:
            query = sys.stdin.readline().rstrip()
            if query == "QUIT":
                is_quit = True
                break
            if query == "END":
                break
            program.append(query)
        if is_quit:
            break
ㅅ
        n = int(sys.stdin.readline())

        for _ in range(n):
            num = int(sys.stdin.readline())
            stack = go_stack(num)
            for query in program:
                if "NUM" in query:
                    query, num = query.split()
                    stack.NUM(int(num))
                    continue
                getattr(stack, query)()
                if stack.is_error:
                    print("ERROR")
                    break
            if not stack.is_error:
                print("ERROR") if len(stack.stack) >= 2 or not stack.stack else print(stack.stack.pop())

        sys.stdin.readline()
        print()