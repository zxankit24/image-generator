import requests
import io
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from ttkbootstrap import Style

# Function to download the image
def download_image():
    if img_data is None:
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
    if file_path:
        try:
            img_url = img_data["urls"]["regular"]
            img_content = requests.get(img_url).content

            with open(file_path, "wb") as file:
                file.write(img_content)
        except Exception as e:
            print(f"Error downloading image: {e}")

# Function to display an image based on the selected category
def display_image(category):
    try:
        url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=ACCESS_KEY"
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for invalid HTTP responses

        img_data = response.json()
        img_url = img_data["urls"]["regular"]
        img_content = requests.get(img_url).content

        photo = ImageTk.PhotoImage(Image.open(io.BytesIO(img_content)).resize((600, 400), resample=Image.LANCZOS))
        label.config(image=photo)
        label.image = photo
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.JSONDecodeError as json_err:
        print(f"JSON decoding error occurred: {json_err}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to enable/disable the "Generate Image" button
def enable_button(*args):
    generate_button.config(state="normal" if category_var.get() != "Choose Category" else "disabled")

# Create the GUI elements
def create_gui():
    global category_var, generate_button, label, img_data

    root = tk.Tk()
    root.title("Image Generator")
    root.geometry("700x500")
    root.config(bg="white")
    root.resizable(False, False)
    style = Style(theme="sandstone")

    img_data = None

    category_var = tk.StringVar(value="Choose Category")
    category_options = ["Choose Category", "Food", "Animals", "People", "Music", "Art", "Vehicles", "Abstract", "Forest", "Fog", "Space", "Galaxy", "Waterfall", "Rainfall", "Flowers", "Random"]
    category_dropdown = ttk.OptionMenu(root, category_var, *category_options, command=enable_button)
    category_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    category_dropdown.config(width=14)

    generate_button = ttk.Button(text="Generate Image", state="disabled", command=lambda: display_image(category_var.get()))
    generate_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    download_button = ttk.Button(text="Download Image", command=download_image)
    download_button.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

    label = tk.Label(root, background="white")
    label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    root.columnconfigure([0, 1, 2], weight=1)
    root.rowconfigure(1, weight=1)
    root.mainloop()

if __name__ == '__main__':
    create_gui()
