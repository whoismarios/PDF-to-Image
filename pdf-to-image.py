from pdf2image import convert_from_path
from tkinter import *
from tkinter import filedialog, messagebox

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    e1.delete(0, END)
    e1.insert(END, file_path)

def pdf2img():
    try:
        pdf_path = e1.get()
        if not pdf_path:
            messagebox.showinfo("Error", "Please select a PDF file.")
            return

        images = convert_from_path(pdf_path)
        for i, img in enumerate(images):
            img.save(f"output_{i}.jpg", "JPEG")

        messagebox.showinfo("Result", "Conversion successful.")
    except Exception as e:
        messagebox.showinfo("Error", str(e))

master = Tk()
Label(master, text="File Location").grid(row=0, sticky=W)

e1 = Entry(master)
e1.grid(row=0, column=1)

select_button = Button(master, text="Select", command=browse_file)
select_button.grid(row=0, column=2)

convert_button = Button(master, text="Convert", command=pdf2img)
convert_button.grid(row=1, column=1, pady=10)

mainloop()
