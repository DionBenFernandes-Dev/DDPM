from tkinter import Tk, filedialog
from PIL import Image

# Hide the main tkinter window
root = Tk()
root.withdraw()

# Open a file dialog and ask the user to select an image file
file_path = filedialog.askopenfilename(title="Select an image file", 
                                       filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])

# Load the image
image = Image.open(file_path)

# Get the mode of the image
mode = image.mode

# Determine the number of channels
if mode == "L":
    channels = 1
elif mode == "RGB":
    channels = 3
elif mode == "RGBA":
    channels = 4
else:
    channels = "unknown"

print(f"The image has {channels} channels.")
