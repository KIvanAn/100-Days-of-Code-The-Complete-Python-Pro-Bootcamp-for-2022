from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
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

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Inputs don't be empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message="These are the details entered:\n\n"
                                                              f"Email: {email}\n\nPassword: {password}\n\n"
                                                              "Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"Website: {website} | Email: {email} | Password: {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


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
website_input = Entry(width=40)
email_input = Entry(width=40)
password_input = Entry(width=22)
website_input.focus()
email_input.insert(0, "my_email@yandex.ru")
website_input.grid(column=1, row=1, columnspan=2)
email_input.grid(column=1, row=2, columnspan=2)
password_input.grid(column=1, row=3)

# Buttons
generate_pass_button = Button(text="Generate Password", command=generate_password)
add_pass_button = Button(text="Add", width=20, command=save_password)
generate_pass_button.grid(column=2, row=3)
add_pass_button.grid(column=1, row=4)

window.mainloop()
