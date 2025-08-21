a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

numbers = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5]
top_k = 3

def top_k_element(values, top_k):

    dict = {item: values.count(item) for item in values}

    decending = sorted(dict.items(), key=lambda item: item[1], reverse=True)

    top_k_numbers = decending[:top_k]

    top_k_items = [pair[0] for pair in top_k_numbers]

    return top_k_items

top_k_items = top_k_element(numbers, top_k)

print(f"Top {top_k} most frequent items: {top_k_items}")