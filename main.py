import os
import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class FileSelectorViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("File Selector and Viewer")

        self.label = tk.Label(self.root)
        self.label.pack()

        self.button = tk.Button(self.root, text="Select File", command=self.select_file)
        self.button.pack()

    def select_file(self):
        file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File",
                                               filetypes=(("All files", "*.*"),))
        if file_path:
            self.show_media(file_path)

    def show_media(self, file_path):
        file_extension = file_path.split(".")[-1]

        if file_extension.lower() in ["jpg", "jpeg", "png"]:
            self.show_image(file_path)
        elif file_extension.lower() in ["mp4", "avi", "mov"]:
            self.play_video(file_path)
        else:
            print("Unsupported file type")

    def show_image(self, image_path):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.label.config(image=photo)
        self.label.image = photo

    def play_video(self, video_path):
        cap = cv2.VideoCapture(video_path)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(frame)
            self.label.config(image=photo)
            self.label.image = photo
            self.label.update_idletasks()
            self.root.update()

        cap.release()

if __name__ == "__main__":
    root = tk.Tk()
    app = FileSelectorViewer(root)
    root.mainloop()
