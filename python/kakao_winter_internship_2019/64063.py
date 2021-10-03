"""
1. 한 번에 한 명씩 신청한 순서대로 방을 배정합니다.
2. 고객은 투숙하기 원하는 방 번호를 제출합니다.
3. 고객이 원하는 방이 비어 있다면 즉시 배정합니다.
4. 고객이 원하는 방이 이미 배정되어 있으면 원하는 방보다 번호가 크면서 비어있는 방 중 가장 번호가 작은 방을 배정합니다.
"""
import sys

def find_next_node(room_record, room):

    if room not in room_record.keys():
        room_record[room] = room + 1
        return room + 1

    next_room = find_next_node(room_record, room_record[room])
    room_record[room] = next_room
    return next_room


def solution(k, room_number):

    sys.setrecursionlimit(int(1e9))
    room_record = {}  # key : node number , value : next node number

    for room in room_number:
        find_next_node(room_record, room)
    return list(room_record.keys())

if __name__ == '__main__':
    k = 10
    room_number = [1,3,4,1,3,1]
    print(solution(k, room_number))
    result = [1,3,4,2,5,6]

