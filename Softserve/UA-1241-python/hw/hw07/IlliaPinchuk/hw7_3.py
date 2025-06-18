def char_count(s):
    if not s:
        print("The input string is empty.")
        return {}

    count_dict = {}
    for char in s:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

input_string = input("Enter a string: ").strip()
output = char_count(input_string)
if output:
    print(output)
