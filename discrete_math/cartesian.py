def cartesian_product(set1, set2):
    """Calculate cartesian product of two sets"""
    result = []
    for elem1 in set1:
        for elem2 in set2:
            result.append((elem1, elem2))
    return result

def display_cartesian_product(product):
    """Display the cartesian product in the required format"""
    print("\nCartesian Product: ")
    output = []
    for pair in product:
        output.append(f"({pair[0]}, {pair[1]})")
    print(", ".join(output)) 