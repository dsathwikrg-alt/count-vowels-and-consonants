import re
from typing import List,Any


def vowel_consonant(string_input: str) -> int:

    input_string = string_input

    cleaned_string = re.sub(r'[^A-Za-z]', '', input_string).lower()

    vowel: List[Any] = ['a','e','i','o','u']
    vowel_count = 0
    consonant_count = 0

    for x in cleaned_string:
        if x in vowel:
            vowel_count += 1
        else:
            consonant_count += 1

    return vowel_count, consonant_count


def main():

    user_input = input("Enter the String :")

    vowel_count, consonant_count = vowel_consonant(user_input)

    print(f'The number of vowels in the string {user_input} is {vowel_count}')

    print(f'The number of consonants in the string {user_input} is {consonant_count}')

if __name__=='__main__':
    main()    




    