
def solution(commands):
    answer = []
    table = [[None] * 51 for _ in range(51)]
    for cmd in commands:
        if cmd[0] == "U":
            if cmd[1] == "P":
                split_cmd = cmd.split()
                if len(split_cmd) == 4:  # UPDATE r, c, value
                    _, r, c, value = split_cmd
                    r, c = int(r), int(c)
                    if isinstance(table[r][c], list):
                        for er, ec in table[r][c][0]:  # 머지된 원소들
                            table[er][ec][1] = value
                    else:
                        table[r][c] = value

                else:  # UPDATE value1, value2
                    _, value1, value2 = split_cmd
                    for r in range(1, 51):
                        for c in range(1, 51):
                            if isinstance(table[r][c], list):
                                if table[r][c][1] == value1:
                                    table[r][c][1] = value2
                            else:
                                if table[r][c] == value1:
                                    table[r][c] = value2

            elif cmd[1] == "N":  # UNMERGE r c
                _, r, c = cmd.split()
                r, c = int(r), int(c)
                if isinstance(table[r][c], list):
                    value = table[r][c][1]
                    for er, ec in table[r][c][0]:
                        table[er][ec] = None
                    table[r][c] = value

        elif cmd[0] == "M":  # Merge r1, c1, r2, c2
            _, r1, c1, r2, c2 = cmd.split()
            r1, c1, r2, c2 = map(int, (r1, c1, r2, c2))
            if isinstance(table[r1][c1], list) and isinstance(table[r2][c2], list):
                merged_set = table[r1][c1][0] | table[r2][c2][0]
                if table[r1][c1][1] is not None and table[r2][c2][1] is not None:
                    value = table[r1][c1][1]
                elif table[r1][c1][1] is not None:
                    value = table[r1][c1][1]
                elif table[r2][c2][1] is not None:
                    value = table[r2][c2][1]
                else:
                    value = None
                for er, ec in merged_set:
                    table[er][ec] = [merged_set, value]

            elif isinstance(table[r1][c1], list):  # 참조관계 잘 확인하기

                if table[r1][c1][1] is not None and table[r2][c2] is not None:
                    value = table[r1][c1][1]
                elif table[r1][c1][1] is not None:
                    value = table[r1][c1][1]
                elif table[r2][c2] is not None:
                    value = table[r2][c2]
                else:
                    value = None
                table[r1][c1][0].add((r2, c2))
                merged_set = table[r1][c1][0]
                for er, ec in merged_set:
                    table[er][ec] = [merged_set, value]

            elif isinstance(table[r2][c2], list):
                if table[r2][c2][1] is not None and table[r1][c1] is not None:
                    value = table[r1][c1]
                elif table[r1][c1] is not None:
                    value = table[r1][c1]
                elif table[r2][c2][1] is not None:
                    value = table[r2][c2][1]
                else:
                    value = None

                table[r2][c2][0].add((r1, c1))
                merged_set = table[r2][c2][0]
                for er, ec in merged_set:
                    table[er][ec] = [merged_set, value]

            else:
                if table[r2][c2] is not None and table[r1][c1] is not None:
                    value = table[r1][c1]
                elif table[r1][c1] is not None:
                    value = table[r1][c1]
                elif table[r2][c2] is not None:
                    value = table[r2][c2]
                else:
                    value = None
                table[r1][c1] = table[r2][c2] = [set(((r1, c1), (r2, c2))), value]

        elif cmd[0] == "P":  # PRINT r c
            _, r, c = cmd.split()
            r, c = int(r), int(c)
            if isinstance(table[r][c], list):
                if table[r][c][1] is not None:
                    answer.append(table[r][c][1])
                else:
                    answer.append("EMPTY")
            else:
                if table[r][c] is not None:
                    answer.append(table[r][c])
                else:
                    answer.append("EMPTY")
        else:
            raise "설계 오류"

    return answer

if __name__ == '__main__':
    print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
    print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))