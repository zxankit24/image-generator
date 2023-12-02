# Image Generator Application

This is a simple Python application built using Tkinter and the Unsplash API to display and download images based on user-selected categories.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)


## Features

- Allows users to select image categories from a dropdown menu.
- Generates and displays random images based on the selected category.
- Provides an option to download the displayed image.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/zxankit24/image-generator.git
    cd image-generator
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
3. Goto 
    ```bash
    https://unsplash.com/developers
    ```
    - And create Your App 
    - Copy Access Key and 
    - Paste it in Main.py at line 27

4. Run the application:

    ```bash
    python image_generator.py
    ```

## Usage

- Upon running the application, a graphical interface will open.
- Choose a category from the dropdown menu and click "Generate Image" to display a random image from that category.
- Click "Download Image" to save the displayed image to your local system.

## Dependencies

- Python 3.x
- `requests`: HTTP library for making API requests
- `Pillow`: Python Imaging Library for image processing
- `ttkbootstrap`: Library for themed Tkinter widgets

## Contributing

Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.


