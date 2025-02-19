def convert_to_snake_case(pascal_and_camel_case_string):
    snake_case_char_list = []
    for char in pascal_and_camel_case_string:
        if char.isupper():
            converted_charcter = '_' + char.lower()
            snake_case_char_list.append(converted_charcter)
        else:
            snake_case_char_list.append(char)

    snake_case_string = ''.join(snake_case_char_list).strip('_')
    print(snake_case_char_list)
    return snake_case_string

def main():
    print(convert_to_snake_case("ThisIsNotCamelCase"))

main()