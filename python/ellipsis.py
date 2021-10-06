import numpy as np
import pprint

if __name__ == '__main__':
    ar = np.array([[[i + 2 * j + 8 * k for i in range(3)] for j in range(3)] for k in range(3)])
    pprint.pprint(ar)

    # 이때 ...(ellipsis)는 전부다, 싹다와 같은 의미로 사용
    print(ar[1, ...])   # 이때는 ar[1, :, :]과 같다.
    print(ar[..., 1])   # 이때는 ar[:, :, 1]과 같다.
    print(ar[1, ..., 1])    # shape가 (3, 3, 3)이기 때문에 ar[1, :, 1]과 같다.

    # 추가로 FastAPI 라는 프레임워크를 사용할때 validation check를 하려고 type annotation을 강제로 해야하는데 그때 ...으로 필수파라미로 선언가능

def my_function():
    # 이때의 ...(ellipsis)는 아무 행동도 취하지 않겠다 라는 의미
    # pass는 나중에 사용하겠다라는 의미이므로 약간 다르다.
    ...


