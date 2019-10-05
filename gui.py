from tkinter import *
from tkinter import filedialog, ttk, messagebox
from PIL import ImageTk, Image
from detector_2 import detect_copy_move, readImage

class GUI(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        min_width = 500
        min_height = 500

        max_width = 1000
        max_height = 1000

        parent.minsize(width=min_width, height=min_height)
        parent.maxsize(width=max_width, height=max_height)
        self.pack()

        self.resultLabel = Label(self, text="")  # where to write stuff on the dialog box
        self.resultLabel.pack()

        self.imagePanel = Label(self)
        self.imagePanel.pack()

        self.fileLabel = Label(self, text="No file selected", fg="grey")
        self.fileLabel.pack()

        self.progressBar = ttk.Progressbar(self, length=500, mode="determinate")
        self.progressBar.pack(fill=X)

        self.uploadButton = ttk.Button(self, text="Upload Image", command=self.browseFile)
        self.uploadButton.pack(padx=5, pady=0, side=LEFT)

        self.startButton = ttk.Button(self, text="Start", command=self.runProg)
        self.startButton.pack(padx=5, pady=10, side=LEFT)

        self.exitButton = ttk.Button(self, text="Exit Program", command=self.quit)
        self.exitButton.pack(padx=5, pady=20, side=RIGHT)


    def browseFile(self):
        filename = filedialog.askopenfilename(title="Select an image", filetype=[("Image file", "*.jpg *.png")])

        if filename == "":
            return

        self.fileLabel.configure(text=filename)
        img = Image.open(filename)
        img = img.resize((512, 512), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        self.imagePanel.configure(image=img)
        self.imagePanel.image = img

        self.resultLabel.configure(text="")

    def runProg(self):
        path = self.fileLabel['text']

        if path == "No file selected":
            messagebox.showerror('Error', "Please select image")
            return

        img = readImage(path)

        result, img = detect_copy_move(img)

        if result:
            self.progressBar['value'] = 100
            img = Image.open("results.png")
            # img = img.resize((512, 512), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)

            self.imagePanel.configure(image=img)
            self.imagePanel.image = img

            self.resultLabel.configure(text="COPY-MOVE DETECTED")

        else:
            self.resultLabel.configure(text="ORIGINAL IMAGE")


if __name__ == "__main__":
    root = Tk()
    root.title("Copy-Move Detector")
    root.configure(background='White')

    GUI(parent=root)

    root.mainloop()
