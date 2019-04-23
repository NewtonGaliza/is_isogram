def is_isogram(word):

    raw_word = word.lower()  #getting a raw word

    letter_list = []

    if word == '':
        return False

    for letter in raw_word:
        if letter.isdigit():
            return False

        if letter.isalpha():
            if letter in letter_list:
                return False
            letter_list.append(letter)

    return True
