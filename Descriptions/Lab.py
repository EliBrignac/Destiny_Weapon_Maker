import tkinter as tk
import os
from PIL import Image, ImageTk
import csv

class ImageDescriptionTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Description Tool")
        self.image_path = ""
        self.image_description = ""
        self.image_list = []
        self.current_image_index = 0

        self.load_images()
        self.create_widgets()

    def load_images(self):
        folder_path = "images"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        self.image_list = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        self.current_image_index = 0

    def create_widgets(self):
        self.image_label = tk.Label(self.root, padx=10, pady=10)
        self.image_label.pack()

        self.image_name_label = tk.Label(self.root, text="", padx=10, pady=5)  # Label to display the image file name
        self.image_name_label.pack()

        self.description_entry = tk.Text(self.root, width=50, height=10)  # Larger text box
        self.description_entry.pack(pady=10)

        self.load_button = tk.Button(self.root, text="Load Image", command=self.load_image,
                                width=12, height=4)
        self.load_button.pack()

        self.save_button = tk.Button(self.root, text="Save Description", command=self.save_description,
                                width=12, height=4)
        self.save_button.pack()

        self.update_image()

    def update_image(self):
        if self.image_list:
            image = Image.open(self.image_list[self.current_image_index])
            image = image.resize((600, 400), Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.photo)

            image_name = os.path.basename(self.image_list[self.current_image_index])
            self.image_name_label.config(text=image_name)

    def load_image(self):
        if self.image_list:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_list)
            self.update_image()

    def save_description(self):
        self.image_description = self.description_entry.get("1.0", "end-1c")  # Get the whole content of the text box
        if self.image_list and self.image_description:
            image_name = os.path.basename(self.image_list[self.current_image_index])
            with open("image_descriptions.csv", "a", newline="") as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([image_name, self.image_description])
            self.description_entry.delete("1.0", "end")  # Clear the text box

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageDescriptionTool(root)
    root.mainloop()
