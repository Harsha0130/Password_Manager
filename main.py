from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Inputs
web_input = Entry(width=35, highlightthickness=2, highlightcolor="#80C4E9")
web_input.grid(column=1, row=1, columnspan=2, sticky="EW")
web_input.focus()

email_input = Entry(width=35, highlightthickness=2, highlightcolor="#80C4E9")
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(0, "xyz@gmail.com")

password_input = Entry(width=32, highlightthickness=2, highlightcolor="#80C4E9")
password_input.grid(column=1, row=3, sticky="W")

# Buttons
generate_btn = Button(text="Generate Password")
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=35)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")



window.mainloop()
