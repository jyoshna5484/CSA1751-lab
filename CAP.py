from itertools import permutations

def solve_cryptarithmetic(puzzle):
    left, right = puzzle.split("=")
    left_words = left.replace("+", "").split()
    result_word = right.strip()

    letters = set("".join(left_words + [result_word]))
    if len(letters) > 10:
        return None

    letters = list(letters)

    def word_to_number(word, mapping):
        return int("".join(str(mapping[c]) for c in word))

    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))

        # No leading zeros
        if any(mapping[word[0]] == 0 for word in left_words + [result_word]):
            continue

        left_sum = sum(word_to_number(word, mapping) for word in left_words)
        result_value = word_to_number(result_word, mapping)

        if left_sum == result_value:
            return mapping

    return None


# Example usage
puzzle = "SEND + MORE = MONEY"
mapping = solve_cryptarithmetic(puzzle)

if mapping:
    print("Mapping:", mapping)
    translated = puzzle
    for k, v in mapping.items():
        translated = translated.replace(k, str(v))
    print("Solution:", translated)
else:
    print("No solution found.")
