from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

EMAIL = "koshtiakanksha12@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    lis = []
    for i in range(random.randint(5, 6)):
        l = random.choice(letters)
        lis.append(l)
    for i in range(random.randint(2, 3)):
        s = random.choice(symbols)
        lis.append(s)
    for i in range(random.randint(2, 3)):
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
    new_data = {
        website_input.get(): {
            "email": email_input.get(),
            "password": password_input.get()
        }
    }
    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #


def find_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")
    else:
        if website in data:
            messagebox.showinfo(title=f"{website}", message=f"Email: {data[website]['email']}\nPassword: "
                                                            f"{data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


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

website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=39, justify=LEFT)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, EMAIL)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

search_button = Button(text="Search", command=find_password, activebackground="#789395")
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate Password", command=generate_password, activebackground="#789395")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save, activebackground="#789395")
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
