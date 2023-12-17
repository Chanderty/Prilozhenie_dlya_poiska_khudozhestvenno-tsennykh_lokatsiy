import tkinter as tk
from tkinter import scrolledtext

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SnapTag")
        self.geometry("700x300")

        frame_left = tk.Frame(self, borderwidth=10, width=300, height=150)
        frame_left.grid(row=0, column=0)

        frame_right = tk.Frame(self, borderwidth=10, width=300)
        frame_right.grid(row=0, column=1)

        frame_right_right = tk.Frame(self, borderwidth=10, width=300)
        frame_right_right.grid(row=0, column=2)

        self.parser()

        tk.Label(frame_left, text="Желаемые теги через пробел:").pack()

        self.entry = tk.Entry(frame_left)
        self.entry.pack(pady=3, fill=tk.X)

        self.console = scrolledtext.ScrolledText(frame_left, width=20, height=14, wrap="word")
        self.console.pack(pady=6)
        self.add_in_console(self.TAGS)

        self.canvas = tk.Canvas(frame_right, bg='white', height=281, width=281)
        self.canvas.pack()

        start_button = tk.Button(frame_right_right, text="Поиск", command=self.start)
        start_button.pack(padx=3, fill=tk.X)

        self.description = scrolledtext.ScrolledText(frame_right_right, width=20, height=15, wrap="word")
        self.description.pack(pady=5)
        self.add_in_description("")

    def start(self):
        text = self.entry.get().lower()
        if text=="":
            self.add_in_console("Ничего не введено!")
            return
        path, name, descript = self.L.findplace(text.split(" "))
        self.add_in_description(descript)
        print(name, path)
        try:
            from PIL import ImageTk, Image
            image = Image.open(path)
            image.thumbnail((self.canvas.winfo_width(), self.canvas.winfo_height())) #скейлим изображение
            photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.image = photo
        except:
            print("error")
            self.add_in_console("Извините, мы не можем открыть эту картинку :(")
            return


    def add_in_console(self, text):
        self.console.insert(tk.END, text+"\n")
        self.console.yview(tk.END)

    def add_in_description(self, text):
        self.description.delete("1.0", tk.END)
        self.description.insert(tk.END, "Описание:\n"+text)
        self.description.yview(tk.END)

    def parser(self):
        from Logic import logic
        self.L = logic()
        self.TAGS = "Доступные теги: \n"
        tags = self.L.initPlace()
        for ix, i in enumerate(tags):
            self.TAGS += i + " "

app = App()
app.mainloop()
