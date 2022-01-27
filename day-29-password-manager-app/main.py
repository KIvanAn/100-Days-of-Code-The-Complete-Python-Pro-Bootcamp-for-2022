from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '{', '}', '~']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Inputs don't be empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message="These are the details entered:\n\n"
                                                              f"Email: {email}\n\nPassword: {password}\n\n"
                                                              "Is it ok to save?")
        if is_ok:
            try:
                # Read old data
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                # Write new data the first time
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # Update old data
                data.update(new_data)
                # Write new data
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()

    if len(website) == 0:
        messagebox.showerror(title="Error", message="Input 'Website' don't be empty.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="You have not passwords")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=f"{website} data:", message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showerror(title="Empty", message="This website not found in your list")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

# Logo
canvas = Canvas(width=200, height=190)
logo_img = PhotoImage(file="data/logo.png")
canvas.create_image(100, 95, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", pady=10)
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:", pady=10)
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=30)
email_input = Entry(width=49)
password_input = Entry(width=30)
website_input.focus()
email_input.insert(0, "my_email@yandex.ru")
website_input.grid(column=1, row=1)
email_input.grid(column=1, row=2, columnspan=2)
password_input.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)
generate_pass_button = Button(text="Generate Password", width=15, command=generate_password)
generate_pass_button.grid(column=2, row=3)
add_pass_button = Button(text="Add", width=40, command=save_password)
add_pass_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
