
collection = [3, -1, -1]

def most_frequent_item_count(collection):
    if len(collection) == 0:
        return 0
    else:
        max_value = collection.count(collection[0])
        for value in collection:
            if collection.count(value) > max_value:
                max_value = collection.count(value)

        return max_value



print(most_frequent_item_count(collection))
