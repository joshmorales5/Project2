from tkinter import *
from tkinter import ttk
import os
import csv

class Gui:
    def __init__(self, window) -> None:
        self.window = window
        self.data = []

        """
        Header Above the Entry Fields
        """
        self.frame_welcome = Frame(self.window)
        self.label_welcome = Label(self.frame_welcome, text='Welcome to Your Personal Password Vault')
        self.label_welcome.pack()
        self.frame_welcome.pack(anchor='center', pady=25)

        """
        Entry Fields for Site, Username, and Password
        """

        self.frame_site = Frame(self.window)
        self.label_site = Label(self.frame_site, text='Site Name:')
        self.input_site = Entry(self.frame_site)
        self.label_site.pack(side='left')
        self.input_site.pack(padx=120, side='left')
        self.frame_site.pack(anchor='w', padx=10, pady=10)

        self.frame_user = Frame(self.window)
        self.label_user = Label(self.frame_user, text='Username/Email:')
        self.input_user = Entry(self.frame_user)
        self.label_user.pack(side='left')
        self.input_user.pack(padx=85, side='left')
        self.frame_user.pack(anchor='w', padx=10, pady=10)


        self.frame_password = Frame(self.window)
        self.label_password = Label(self.frame_password, text='Password:')
        self.input_password = Entry(self.frame_password)
        self.input_password.config(show='*')
        self.label_password.pack(side='left')
        self.input_password.pack(padx=123, side='left')
        self.frame_password.pack(anchor='w', padx=10, pady=10)

        """
        Buttons for Save, Encrypt, and Decrypt
        Label for feedback
        """

        self.frame_button = Frame(self.window)
        self.save_entry = Button(self.frame_button, text="Save Entry", command=self.submit)
        self.save_label = Label(self.frame_button, text='Enter Information')
        self.save_label.pack()
        self.save_entry.pack()
        self.frame_button.pack(anchor='center', pady=30)

        self.frame_encrypt = Frame(self.window)
        self.encrypt_entry = Button(self.frame_encrypt, text="Encrypt", command=self.encrypt)
        self.encrypt_entry.pack()
        self.frame_encrypt.pack(anchor='center', pady=0)


        self.frame_decrypt = Frame(self.window)
        self.decrypt_entry = Button(self.frame_decrypt, text="Decrypt", command=self.decrypt)
        self.decrypt_entry.pack()
        self.frame_decrypt.pack(anchor='center', pady=0)

        """
        Table to display the saved entries
        """

        self.frame_table = Frame(self.window)
        self.table = ttk.Treeview(self.frame_table, columns=('Site', 'Username', 'Password'), show='headings')
        self.table.heading('Site', text='Site')                     #Used AI to help me with this part since we didn't
        self.table.heading('Username', text='Username')             #cover in class
        self.table.heading('Password', text='Password')
        self.frame_table.pack(anchor='w', padx=10, pady=10)
        self.table.pack()



    def submit(self) -> None:
        """
        Save the entry to the table and CSV File
        """
        site = self.input_site.get().strip()
        user = self.input_user.get().strip()
        password = self.input_password.get().strip()
        csv_file = 'vault.csv'


        if not site or not user or not password:
            """
            If any of the inputs are empty, Shows a Message to fill in the missing information"""
            self.save_label.config(text='Fill out missing information')
        else:
            """
            If all inputs are filled, it saves the entry to the table and CSV file
            """
            self.data.append((site, user, password)) # Append the data to the list
            self.table.insert('', 'end', values=(site, user, '*' * len(password))) # Insert the data into the table
            self.input_site.delete(0, END) # Clears the Site
            self.input_user.delete(0, END) # Clears the User field
            self.input_password.delete(0, END) # Clears the Password
            self.save_label.config(text='Information Saved! Enter Another Entry')

            # Save to CSV file
            with open(csv_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([site, user, password])


    def encrypt(self) -> None:
        """
        Encrypt the passwords in the table and save to CSV file
        """
        csv_file = 'vault.csv'

        # Check if the CSV file exists and is not empty

        if not os.path.exists(csv_file) or os.path.getsize(csv_file) == 0: # Check if the CSV file exists and is not empty
            self.save_label.config(text='No data to encrypt')
            return

        self.save_label.config(text='Encrypting...') #Gets message to 'encrypt' (not really encrypting)
        for row in self.table.get_children():
            self.table.delete(row)

        with open(csv_file, 'r') as file: # Open the CSV file in read mode
            reader = csv.reader(file)
            for row in reader:
                site, user, password = row
                self.table.insert('', 'end', values=(site, user, '*' * len(password))) # Insert the data into the table and 'Encrypts' the password


    def decrypt(self) -> None:
        """
        Decrypt the passwords in the table and save to CSV file
        """
        csv_file = 'vault.csv'

        if not os.path.exists(csv_file) or os.path.getsize(csv_file) == 0: # Check if the CSV file exists and is not empty
            self.save_label.config(text='No data to decrypt')
            return

        self.save_label.config(text='Decrypting...') #'Gets message to 'decrypt' (not really decrypting)
        for row in self.table.get_children():
            self.table.delete(row)


        with open(csv_file, 'r') as file: # Open the CSV file in read mode
            reader = csv.reader(file)
            for row in reader:
                site, user, password = row
                self.table.insert('', 'end', values=(site, user, password)) # Insert the data into the table and 'Decrypts' the password




