import tkinter as tk

def main():
    window = tk.Tk()

    def callback():
        print("Button Clicked")

    btn = tk.Button(window, text="Click Me", command=callback)
    btn.pack()
    window.mainloop()
    
if __name__ == '__main__':
    main()