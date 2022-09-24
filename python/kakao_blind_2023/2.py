def solution(cap, n, deliveries, pickups):
    answer = 0

    delivery_end_idx = len(deliveries) - 1
    pickup_end_idx = len(pickups) - 1

    while delivery_end_idx >= 0 and deliveries[delivery_end_idx] == 0:
        delivery_end_idx -= 1

    while pickup_end_idx >= 0 and pickups[pickup_end_idx] == 0:
        pickup_end_idx -= 1

    while delivery_end_idx >= 0 or pickup_end_idx >= 0:
        distance = max(delivery_end_idx, pickup_end_idx) + 1
        answer += distance

        capacity = cap
        while delivery_end_idx >= 0 and capacity > 0:
            if deliveries[delivery_end_idx] <= capacity:
                capacity -= deliveries[delivery_end_idx]
                deliveries[delivery_end_idx] = 0
                delivery_end_idx -= 1
            else:
                deliveries[delivery_end_idx] -= capacity
                capacity = 0
        while delivery_end_idx >= 0 and deliveries[delivery_end_idx] == 0:
            delivery_end_idx -= 1

        capacity = cap
        while pickup_end_idx >= 0 and capacity > 0:

            if pickups[pickup_end_idx] <= capacity:
                capacity -= pickups[pickup_end_idx]
                pickups[pickup_end_idx] = 0
                pickup_end_idx -= 1
            else:
                pickups[pickup_end_idx] -= capacity
                capacity = 0
        while pickup_end_idx >= 0 and pickups[pickup_end_idx] == 0:
            pickup_end_idx -= 1

    return answer * 2


if __name__ == '__main__':
    print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
    print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))