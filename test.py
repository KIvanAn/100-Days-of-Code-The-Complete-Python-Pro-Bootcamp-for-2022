def your_favorite_color(my_color, **kwargs):
    if "color" in kwargs:
        print(f"My favorite color is {my_color}, but {kwargs['color']} is also pretty good!")
    else:
        print(f"My favorite color is {my_color}, what is your favorite color?")


print(your_favorite_color("black", bom="red"))
