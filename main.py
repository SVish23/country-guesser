import tkinter as tk

from welcome import start_and_difficulty

def main():
    
    root = tk.Tk()
    root.geometry("800x600")

    def no_tab(event):
        return 'break'

    root.bind("<Tab>", no_tab)

    start_and_difficulty(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    

