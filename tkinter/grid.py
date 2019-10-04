from tkinter import *
from tkinter import filedialog, ttk
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

        self.resultLabel = Label(self, text="")
        self.resultLabel.pack()

        self.imagePanel = Label(self)
        self.imagePanel.pack()

        self.fileLabel = Label(self, text="No file selected", fg="grey")
        self.fileLabel.pack()

        self.startButton = ttk.Button(self, text="Start", command=self.runProg)
        self.startButton.pack(side=BOTTOM, fill=X)

        self.uploadButton = ttk.Button(self, text="Upload Image", command=self.browseFile)
        self.uploadButton.pack(side=BOTTOM, fill=X)


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
            return

        img = readImage(path)

        result, img = detect_copy_move(img)

        if result:
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
    root.configure(background='white')

    GUI(parent=root)

    root.mainloop()

