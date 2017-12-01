def get_num_of_characters(inputStr):
    num_count = 0
    for c in inputStr:
        num_count += 1
    return num_count

def output_without_whitespace(input_str):
    result = ''
    for c in input_str:
        if c == ' ':
            continue
        result += c
    return result

if __name__ == '__main__':
    phrase = input('Enter a sentence or phrase: \n')
    print('You entered:' + ' ' + phrase)
    print()
    num_char = get_num_of_characters(phrase)
    print('Number of characters: ' + str(num_char))
    phrase_no_space = output_without_whitespace(phrase)
    print('String with no whitespace: ' + phrase_no_space)