import os


def comparing(first_word, second_word):
    lenght_first, lenght_second = len(first_word), len(second_word)
    array = [[0] * (lenght_second + 1) for repeater in range(lenght_first + 1)]

    for first_index in range(1, lenght_first + 1):
        for second_index in range(1, lenght_second + 1):
            if first_word[first_index - 1] == second_word[second_index - 1]:
                array[first_index][second_index] = (
                    1 + array[first_index - 1][second_index - 1]
                )
            else:
                array[first_index][second_index] = max(
                    array[first_index][second_index - 1],
                    array[first_index - 1][second_index],
                )

    return array[lenght_first][lenght_second]


def longest_word_chain(words):
    max_chain_length = 0

    for word in words:
        max_length = 1
        for other_word in words:
            if len(other_word) == len(word) + 1 and comparing(word, other_word) == len(
                word
            ):
                max_length = max(max_length, len(other_word))
        max_chain_length = max(max_chain_length, max_length)

    return max_chain_length


def read_input_data(input_filename):
    with open(input_filename, "r") as file:
        num_words = int(file.readline().strip())
        words = [file.readline().strip() for _ in range(num_words)]
    return words


def write_output_data(output_filename, result):
    with open(output_filename, "w") as file:
        file.write(str(result))


current_dir = os.path.dirname(__file__)
input_filename = os.path.join(current_dir, "wchain.in")
output_filename = os.path.join(current_dir, "wchain.out")

words = read_input_data(input_filename)
result = longest_word_chain(words)

print("Найбільша кількість слів:", result)
write_output_data(output_filename, result)
