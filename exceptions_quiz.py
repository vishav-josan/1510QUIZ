def reverse_concat(first_word, second_word):
    """
    Concatenate and reverse first_word and second_word.

    :param first_word: a string
    :param second_word: a string
    :precondition: first_word must not be empty
    :precondition: first_word must be a string
    :precondition: second_word must not be empty
    :precondition: second_word must be a string
    :postcondition: concatenates then reverses first_word and second_word
    :return: first_word and second_word concatenated then reversed as a string
    :raises TypeError: if first_word is not a string
    :raises TypeError: if second_word is not a string
    :raises ValueError: if first_word is an empty string
    :raises ValueError: if second_word is an empty string
    >>> reverse_concat("one", "two")
    'owteno'
    >>> reverse_concat("123456", "789")
    '987654321'
    >>> reverse_concat("desreveR"," sI sihT")
    'This Is Reversed'
    """
    if type(first_word) is not str or type(second_word) is not str:
        raise TypeError("Your inputs must be strings!")
    elif first_word == "" or second_word == "":
        raise ValueError("Your inputted strings cannot be empty!")
    else:
        first_result = first_word + second_word
        final_result = (first_result[::-1])
        return final_result


def main():
    """
    Drive the program.
    """
    first_word = input("please enter the first word")
    second_word = input("please enter the second word")
    try:
        result = reverse_concat(first_word, second_word)

    except TypeError as error_message:
        print(error_message)

    except ValueError as error_message:
        print(error_message)

    else:
        print(result)


if __name__ == "__main__":
    main()
