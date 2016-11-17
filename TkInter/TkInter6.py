import tkinter as tk
def main():
    window = tk.Tk()
    tk.Label(window, text="Name:").grid(row=0, column=0, sticky=tk.W)
    tk.Label(window, text="E-mail Address:").grid(row=1, column=0, sticky=tk.W)

    ent_name = tk.Entry(window)
    ent_email = tk.Entry(window)
    ent_name.grid(row=0, column=1)
    ent_email.grid(row=1, column=1)

    chk_remeber = tk.Checkbutton(window, text="Remember me")
    chk_remeber.grid(row=2, column=0, columnspan=2, sticky=tk.W)
    btn = tk.Button(window, text="Submit")
    btn.grid(row=2, column=2)
    window.mainloop()
    
if __name__ == '__main__':
    main()