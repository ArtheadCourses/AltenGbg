import tkinter as tk
def main():
    window = tk.Tk()
    lbl_username = tk.Label(window, text="Username:")
    ent_username = tk.Entry(window)
    lbl_username.pack()
    ent_username.pack()

    lbl_password = tk.Label(window, text="Password:")
    ent_password = tk.Entry(window, show="*")
    lbl_password.pack()
    ent_password.pack()

    btn_login = tk.Button(window, text="Login")
    btn_login.pack()
    window.mainloop()
    
if __name__ == '__main__':
    main()