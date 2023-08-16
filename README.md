# Text Case Converter

This Python script allows you to quickly convert text to different cases (uppercase, lowercase, and title case) using keyboard shortcuts. It utilizes the `pyperclip` and `keyboard` libraries to manipulate clipboard contents and perform case conversions.

## Features

- Convert selected text to uppercase with `Ctrl + Shift + U`
- Convert selected text to lowercase with `Ctrl + Shift + L`
- Convert selected text to title case with `Ctrl + Shift + T`

## Installation

1. Make sure you have Python installed on your system.
2. Install the required libraries by running:
   ```bash
   pip install pyperclip keyboard
   ```
3. Clone or download this repository.

## Usage

1. Run the `main.py` script using the following command:
   ```bash
   python main.py
   ```
2. Once the script is running, you can use the defined keyboard shortcuts to perform the conversions on the selected text.
3. Press `Esc` to exit the script.

## Example

Suppose you have the text "hello world" in your clipboard. Follow these steps:

1. Press `Ctrl + Shift + U` to convert the text to uppercase: "HELLO WORLD"
2. Press `Ctrl + Shift + L` to convert the text to lowercase: "hello world"
3. Press `Ctrl + Shift + T` to convert the text to title case: "Hello World"

Please note that the script temporarily modifies the clipboard contents to perform the conversions and restores the original clipboard data afterward.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
