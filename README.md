# Password Manager

This is a simple Password Manager application built with Python and Tkinter. The application allows you to generate strong passwords and save them along with associated website URLs and email addresses.
- This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp for 2023" course by Dr. Angela Yu.

## Features

- **Password Generation**: Generates a strong password containing letters, numbers, and symbols.
- **Save Passwords**: Allows you to save website URLs, email addresses, and passwords to a file.
- **Clipboard Copy**: Automatically copies the generated password to the clipboard.

## Requirements

- Python 3.x
- Tkinter library (included with Python standard library)
- pyperclip library (install using `pip install pyperclip`)

## File Structure:

- **main.py**: The main script containing the password manager code.
- **logo.png**: The logo image displayed in the application.
- **data.txt**: The file where the saved passwords are stored.

## New Features(Updated)

- **Search Password**: A new "Search" button has been added to allow users to find passwords stored in the `data.json` file. Enter the website URL and click "Search" to retrieve the email and password associated with that site.
- **Exception Handling**: Improved exception handling for file operations. The application now handles scenarios where the `data.json` file is not found, providing appropriate error messages.
- **Data Storage**: Passwords are now stored in a JSON file (`data.json`) instead of a text file for better data management and retrieval.
 


## Screenshots:

![Screenshot 2024-06-14 114501](https://github.com/Harsha0130/Password_Manager/assets/127675058/0b0f4279-0821-4aea-9847-f4fa3c87d77a)
- Updated
  
![Screenshot 2024-06-15 152001](https://github.com/Harsha0130/Password_Manager/assets/127675058/863c0187-3470-4934-be39-d36477cc1da3)
