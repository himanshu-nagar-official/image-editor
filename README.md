# Image Editor

## Description
The **Image Editor** project is a software application developed using **Python**, **OpenCV**, **NumPy**, **Pillow**, and **Tkinter**. The purpose of this project is to create a user-friendly image editing tool that allows users to perform basic image processing functions such as cropping, resizing, and applying filters. The application has a modern, **dark mode** look and feel, providing both functionality and aesthetic appeal.

### Features
- **Image Cropping**: Select and crop areas of an image using the mouse, and display the cropped area in a new window.
- **Image Resizing**: Resize images to custom dimensions for various uses like printing, web design, or social media.
- **Filters**: Apply filters such as grayscale, blurring, and sharpening to enhance the appearance of images.
- **User-Friendly GUI**: Built using Tkinter with a sleek dark mode interface.
- **Cross-Platform Compatibility**: Designed to be used across different platforms where Python is supported.

### Target Audience
This tool is beneficial for:
- **Individual users** who wish to edit their personal photos.
- **Creative professionals** working with images in their designs.
- **Educators** and **researchers** needing basic image editing functionalities.
- **Healthcare providers** and others who may require image manipulation for various purposes.

---

## Prerequisites

Ensure the following libraries are installed on your machine:
- **Python 3.x**
- **OpenCV**
- **NumPy**
- **Pillow**
- **Tkinter**

You can install the required libraries using:
```bash
pip install -r requirements.txt
```

---

## Files Overview

### **Python Files**
1. **`imageEditor.py`**: Main Python script that runs the image editor application.
2. **`requirements.txt`**: Lists all the dependencies required to run the project.

### **Assets**
1. **`logo.png`**: Image file used in the GUI.

---

## Installation & Running the Application

### Step 1: Clone the repository
Clone the project repository to your local machine:
```bash
git clone https://github.com/himanshu-nagar-official/image-editor.git
```

### Step 2: Install dependencies
Install the required libraries:
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
Run the image editor application:
```bash
python imageEditor.py
```

---

## File Structure

```
image-editor/
├── imageEditor.py               # Main Python file for the image editor
├── .gitignore                   # Git ignore rules
├── logo.png                     # Image file for the GUI
├── requirements.txt             # List of dependencies
└── README.md                    # Project documentation
```

---

## Limitations
- The project is currently designed as a **single-user system**.
- **Basic editing features** may not be as advanced as other professional image editing software.
- The project is primarily focused on image manipulation and may lack additional advanced features like batch processing or multi-layer editing.
