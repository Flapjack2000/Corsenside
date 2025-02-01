"""
"Four is cosmic" is a riddle that describes how any number can be reduced to four.
Start with any number and count the letters in its word form.
Now do the same with that number, and so on. Eventually you'll get to four,
which is a "cosmic number" because it has a number of letters equal to its value.
In fact, four is the only cosmic number.
"""
from num2words import num2words

def cosmic(number):
    if number == 4:
        print("four -> cosmic")
    else:
        old_num_as_words = word_format(num2words(number))

        new_num = len([char for char in old_num_as_words if char.isalpha()])

        new_num_as_words = word_format(num2words(new_num))

        print(f'{old_num_as_words} -> {new_num_as_words}')

        cosmic(new_num)

def word_format(word):
    # Format words to remove dashes and only count the names of the numbers and not the word 'and'

    while ' and' in word:
        word = word.replace(' and', '')

    while '-' in word:
        word = word.replace('-', ' ')
    return word

while True:
    cosmic(int(input("Enter a number: ")))
    print("------------------------------------------------------------------------------------------------------------------------------------------------------")
