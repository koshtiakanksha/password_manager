from tkinter import *
from tkinter import messagebox
import random
import pyperclip

EMAIL = "your_email@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    lis = []
    for i in range(random.randint(6, 8)):
        l = random.choice(letters)
        lis.append(l)
    for i in range(random.randint(2, 4)):
        s = random.choice(symbols)
        lis.append(s)
    for i in range(random.randint(2, 4)):
        n = random.choice(numbers)
        lis.append(n)

    random.shuffle(lis)
    hard_password = ""
    for i in lis:
        hard_password += i

    password_input.insert(0, hard_password)
    pyperclip.copy(password_input.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website_input.get(), message=f"These are the details entered:\nEmail: "
                                                                          f"{email_input.get()}\nPassword: "
                                                                          f"{password_input.get()}\nIs it ok to save?")

        if is_ok:
            with open("saved_password.txt", "a") as file:
                file.write(f"{website_input.get()} | {email_input.get()} | {password_input.get()}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(width=39)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=39, justify=LEFT)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, EMAIL)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
