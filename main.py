from gui import *
from tkinter import Tk

def main():
    window = Tk()
    window.title('Personal Password Vault')
    window.geometry('600x600')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()
