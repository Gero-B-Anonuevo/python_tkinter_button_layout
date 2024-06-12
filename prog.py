import tkinter as tk

main_window = tk.Tk()
main_window.title("GUI No. 3")
main_window.geometry("400x300")

main_frame = tk.Frame(main_window)
main_frame.pack(fill='both', expand=True)

first_frame = tk.LabelFrame(main_frame)
first_frame.pack(side="left", fill='both', expand=True)

second_frame = tk.LabelFrame(main_frame)
second_frame.pack(side='right', fill='both', expand=True)

button_a = tk.Button(first_frame, text="A")
button_a.pack(side='top', fill='both', expand=True)

button_b = tk.Button(second_frame, text="B")
button_b.pack(side='top', fill='both', expand=True)

button_c = tk.Button(first_frame, text="C")
button_c.pack(side="bottom", fill='both', expand=True)

button_d = tk.Button(second_frame, text="D")
button_d.pack(side="bottom", fill='both', expand=True)

main_window.mainloop()