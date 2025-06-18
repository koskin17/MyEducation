def categorize_numbers():
    numbers = range(1, 11)
    
    even_div_2 = list(filter(lambda x: x % 2 == 0, numbers))
    odd_div_3 = list(filter(lambda x: x % 2 != 0 and x % 3 == 0, numbers))
    not_div_2_3 = list(filter(lambda x: x % 2 != 0 and x % 3 != 0, numbers))
    
    categories = {
        "even_div_2": even_div_2,
        "odd_div_3": odd_div_3,
        "not_div_2_3": not_div_2_3
    }
    
    return categories

categories = categorize_numbers()

for category, numbers in categories.items():
    print(f"{category}: {numbers}")