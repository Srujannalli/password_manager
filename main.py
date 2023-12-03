from tkinter import *
from tkinter import messagebox
import random
import numpy
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    word=random.sample(letters, nr_letters)
    symb = random.sample(symbols, nr_symbols)
    num = random.sample(numbers, nr_numbers)
    letters_in_password = str( )
    for letters_of_password in word:
        letters_in_password += letters_of_password
    symbols_in_password = str( )
    for symbols_of_password in symb:
        symbols_in_password += symbols_of_password
    numbers_in_password = str()
    for numbers_of_password in num:
        numbers_in_password += numbers_of_password
    password=letters_in_password+symbols_in_password+numbers_in_password
    randomness = list(password)
    numpy.random.shuffle(randomness)
    random_password=str()
    for randomness in randomness:
        random_password += randomness
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def ADD():
    mail = email_entry.get()
    site = website_entry.get()
    password = password_entry.get()
    new_data = {
        site:
            {
                "mail": mail,
                "password": password,
            }
    }

    if len(site) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="you should not leave any options empty")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
                data.update(new_data)

            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        
        except json.decoder.JSONDecodeError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search():
    mail = email_entry.get()
    site = website_entry.get()
    password = password_entry.get()

    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
            website = data[site]

    except KeyError:
        messagebox.showinfo(title="error", message="you have not logged in this website, so please login first")

    finally:
        messagebox.showinfo(title="website details", message=f"your website mail id: {data[site]['mail']} \n your password : {data[site]['password']}")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(background="white")
window.geometry("400x400")
canvas = Canvas(window, width=200, height=200,background="white", highlightthickness=0)
pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pic)
canvas.grid(column=1, row=0, pady=20)

website_label = Label(text="website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=17)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "srujan@gamail.com")
password_label = Label(text="Password")
password_label.grid(column=0, row=3)
password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)
password_button = Button(text="generate password", command=password_generator)
password_button.grid(column=2, row=3)
add_button = Button(text="add", width=30, command=ADD)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="search", command=search)
search_button.grid(column=2, row=1)
window.mainloop()