from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
C1 = "#B5C0D0"
C2 = "#CCD3CA"
C3 = "#F5E8DD"
C4 = "#EED3D9"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=C4)


canvas = Canvas(width=200, height=200, highlightthickness=0, bg=C4)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:", bg=C4)
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg=C4)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg=C4)
password_label.grid(column=0, row=3)

web_input = Entry(width=35, bg=C1)
web_input.grid(column=1, row=1, columnspan=2, sticky="EW")

email_input = Entry(width=35, bg=C1)
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")

password_input = Entry(width=32, bg=C1)
password_input.grid(column=1, row=3, sticky="W")

generate_btn = Button(text="Generate Password", bg=C2)
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=35, bg=C2)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")



window.mainloop()
