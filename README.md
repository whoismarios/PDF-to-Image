# PDF-to-Image

## About the Tool

This Python script provides a simple graphical user interface (GUI) tool for converting PDF files to images. It uses the pdf2image library to convert the PDF files and the tkinter library for creating the GUI.

The tool consists of a window with the following components:

- A label "File Location" indicating the purpose of the entry field next to it.
- An entry field where the user can enter or view the path of the selected PDF file.
- A "Select" button that opens a file dialog for the user to choose a PDF file.
- A "Convert" button that triggers the conversion process from PDF to images.
- A label "Output Directory" indicating the purpose of the entry field next to it.
- An entry field where the user can enter or view the path of the selected output directory.
- A "Choose Directory" button that opens a directory dialog for the user to choose an output directory.

Error and result messages are displayed using message boxes.

When the user clicks the "Select" button, a file dialog opens, allowing them to select a PDF file. The selected file path is then displayed in the entry field.

When the user clicks the "Convert" button, the script retrieves the PDF file path from the entry field. If no path is entered, an error message is displayed. Otherwise, the script uses the convert_from_path function from the pdf2image library to convert each page of the PDF file into an image. The resulting images are saved as JPEG files with names "output_0.jpg", "output_1.jpg", and so on, in the selected output directory. Finally, a message box shows a success message.

If any exception occurs during the conversion process, an error message is displayed with the corresponding error information.

The script runs within a Tkinter Tk instance, and the mainloop function is called to start the GUI event loop, allowing the user to interact with the tool.

## New Functionalities

The updated version of the script includes the following new functionalities:

- Added a label "Output Directory" and an entry field where the user can enter or view the path of the selected output directory.
- Added a "Choose Directory" button that opens a directory dialog for the user to choose an output directory.
- Modified the conversion process to save the resulting images as JPEG files with names "output_0.jpg", "output_1.jpg", and so on, in the selected output directory.
- Improved the UI by adding a label and entry field for the output directory selection.

## Packages and Imports

Make sure you have the following dependencies installed:

- pdf2image: This package is used for converting PDF files to images.
```python
  pip install pdf2image
```
- tkinter: This package is used for creating the graphical user interface (GUI).
  ```python
  pip install tk
```

### Next Steps

To further improve the script, you can consider the following next steps:

Implement more options for output file formats, such as PNG or TIFF.
Include additional customization options, such as image resolution or quality settings.
Create a footer section in the GUI that provides information about the tool, version, and developer.
By implementing these enhancements, the tool can become more versatile and user-friendly, catering to a wider range of user requirements.

Feel free to explore and expand upon the script based on your specific needs and preferences. Happy coding!