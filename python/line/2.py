"""
문제 설명
부서진 키보드가 있습니다. 부서진 키보드는 공백을 입력하기 위한 스페이스바와 스페이스바 외의 다른 n개의 키만 사용이 가능합니다.
예를 들어 n이 4고 l, i, n, e 4개의 키를 사용할 수 있다고 했을 때, "line in line", "in    n          in"과 같은 문장을 만들 수 있습니다.
알파벳 대문자를 만들려면 shift키와 해당 알파벳의 소문자 키가 필요합니다.
예를 들어, "L I N e"을 완성하려면 shift, l, i, n, e 이렇게 5개의 키가 필요합니다.

당신은 이 부서진 키보드로 주어진 문자열 배열에 있는 문자열을 완성하면 완성한 문자열의 길이만큼 점수를 받는 게임을 하려고 합니다.
예를 들어, "coding is fun"이라는 문자열을 완성하면 13점을 얻을 수 있습니다.
단, 완성된 문자열 속에 알파벳 대문자가 있을 경우 알파벳 대문자 개수만큼 1점씩 추가로 점수를 얻을 수 있습니다.
예를 들어, "COding is fun"이라는 문자열을 완성하면 15(= 13 + 2)점을 얻을 수 있습니다.
문자열을 완전히 완성시키지 못하면 점수를 얻을 수 없습니다.
예를 들어, "abcde"라는 문자열을 "abc"까지만 완성하면 점수를 얻을 수 없습니다.

여러 개의 문자열을 담은 문자열 배열 sentences와 스페이스바 외에 사용 가능한 키의 개수를 나타내는 정수 n이 매개변수로 주어집니다. 이때, 얻을 수 있는 최대 점수를 return 하도록 solution 함수를 완성해주세요. 단, 완성할 수 있는 문자열이 없을 경우 0을 return 해주세요.

제한사항
1 ≤ sentences 길이 ≤ 15
1 ≤ sentences의 원소 길이 ≤ 100,000
sentences의 원소는 알파벳과 공백으로 이루어져 있습니다.
sentences의 원소는 항상 알파벳으로 시작하여 알파벳으로 끝납니다.
예를 들어, ["a ", " A ", " A"]와 같은 원소는 주어지지 않습니다.
1 ≤ n ≤ 27
입출력 예
sentences	n	result
["line in line", "LINE", "in lion"]	5	20
["ABcD", "bdbc", "a", "Line neWs"]	7	12
입출력 예 설명
입출력 예 #1

문자열	필요한 키	점수
"line in line"	l, i, n, e	12
"LINE"	shift, l, i, n, e	8
"in lion"	l, i, n, o	7
사용할 키로 l, i, n, e, o를 고르면 첫 번째와 세 번째 문자열을 완성해 19점을 얻을 수 있습니다.
하지만, l, i, n, e, shift를 고르면 첫 번째와 두 번째 문자열을 완성해 20점을 얻을 수 있습니다.
따라서 20을 return 해야 합니다.

입출력 예 #2

문자열	필요한 키	점수
"ABcD"	shift, a, b, c, d	7
"bdbc"	b, c, d	4
"a"	a	1
"Line neWs"	shift, l, i, n, e, w, s	11
사용할 키로 shift, l, i, n, e, w, s를 고르면 네 번째 문자열을 완성해 11점을 얻을 수 있습니다.
하지만, shift, a, b, c, d를 고르면 첫 번째, 두 번째, 세 번째 문자열을 완성해 12점을 얻을 수 있습니다. (7개까지 키를 사용할 수 있지만 5개로도 충분히 3개의 문자열을 완성할 수 있습니다.)
따라서 12를 return 해야 합니다.
"""

from itertools import combinations

def solution(sentences, n):

    entire_key = set()
    required_key = []
    for sentence in sentences:
        weight = len(sentence)
        sentence_set = set()
        if not sentence.islower():
            sentence_set.add("sp")
            for ch in sentence:
                if ch.isupper():
                    weight += 1

        sentence_set |= set(str.lower(sentence))
        if ' ' in sentence_set:
            sentence_set.remove(' ')
        entire_key |= sentence_set
        print(entire_key, sentence, sentence_set, weight)
        required_key.append((sentence_set, weight))

    answer = 0
    for keys in combinations(entire_key, n):
        keys = set(keys)
        weight_sum = 0
        for sentence_key, weight in required_key:
            if sentence_key.issubset(keys):
                weight_sum += weight
        answer = max(weight_sum, answer)

    return answer


if __name__ == "__main__":
    sentences = ["line in line", "LINE", "in lion"]
    print(solution(sentences, 5))
    sentences = ["ABcD", "bdbc", "a", "Line neWs"]
    print(solution(sentences, 7))