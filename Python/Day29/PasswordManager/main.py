from tkinter import *
from tkinter import messagebox
import random
import pyperclip

WHITE = "#FFFFFF"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if website or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty?")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nWebsite: {website}\nEmail/Username: {email}\nPassword: {password}")
        if is_ok:
            f = open("data.txt", "a")
            f.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg=WHITE)
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_username_label = Label(text="Email/Username:", bg=WHITE)
email_username_label.grid(column=0, row=2)
email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "aenaeble@email.com")

password_label = Label(text="Password:", bg=WHITE)
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", highlightthickness=0, command=password_generator)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
