from tkinter.ttk import *
from pdf2image import convert_from_path
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


# Create the main window
master = Tk()
master.title("PDF to Image Converter")
master.geometry("600x200")

# Configure background styling
master.configure(bg="black")

# Create a frame for the content
content_frame = Frame(master, bg="black")
content_frame.pack(pady=20)

# Set the window icon
icon_path = "./pdf2img.png"
icon_image = Image.open(icon_path)
icon_photo = ImageTk.PhotoImage(icon_image)
master.iconphoto(True, icon_photo)

# Function to browse and select a PDF file
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    e1.delete(0, END)
    e1.insert(END, file_path)

# Function to choose the output directory
def choose_output_directory():
    output_directory = filedialog.askdirectory()
    e2.delete(0, END)
    e2.insert(END, output_directory)

# Function to convert PDF to images
def pdf2img():
    try:
        pdf_path = e1.get()
        if not pdf_path:
            messagebox.showinfo("Error", "Please select a PDF file.")
            return

        output_directory = e2.get()
        if not output_directory:
            messagebox.showinfo("Error", "Please select an output directory.")
            return

        images = convert_from_path(pdf_path)
        for i, img in enumerate(images):
            img.save(f"{output_directory}/output_{i}.jpg", "JPEG")

        messagebox.showinfo("Result", "Conversion successful.")
    except Exception as e:
        messagebox.showinfo("Error", str(e))

# Create labels and buttons with styling
label_file = Label(content_frame, text="File Location", bg="black", fg="white", font=("Arial", 12))
label_file.grid(row=0, column=0, padx=10, pady=10, sticky=W)

e1 = Entry(content_frame, width=40, font=("Arial", 12))
e1.grid(row=0, column=1, padx=10, pady=10)

select_button = Button(content_frame, text="Select", command=browse_file, font=("Arial", 12), bg="black", fg="black", bd=2, relief=RAISED)
select_button.grid(row=0, column=2, padx=10, pady=10)

label_output = Label(content_frame, text="Output Directory", bg="black", fg="white", font=("Arial", 12))
label_output.grid(row=1, column=0, padx=10, pady=10, sticky=W)

e2 = Entry(content_frame, width=40, font=("Arial", 12))
e2.grid(row=1, column=1, padx=10, pady=10)

select_directory_button = Button(content_frame, text="Choose Directory", command=choose_output_directory, font=("Arial", 12), bg="black", fg="black", bd=2, relief=RAISED)
select_directory_button.grid(row=1, column=2, padx=10, pady=10)

convert_button = Button(content_frame, text="Convert", command=pdf2img, font=("Arial", 12), bg="black", fg="black", bd=2, relief=RAISED)
convert_button.grid(row=2, column=1, pady=20)

# Start the main event loop
master.mainloop()
