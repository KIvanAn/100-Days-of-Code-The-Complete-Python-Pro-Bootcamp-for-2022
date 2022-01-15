class Chain:
    def __init__(self, number_of_items):
        self.number_of_items = number_of_items

    def __str__(self):
        return f"Chain with {self.number_of_items} items"

    def __len__(self):
        return self.number_of_items


new_class = Chain(5)
print(new_class)
print(len(new_class))
