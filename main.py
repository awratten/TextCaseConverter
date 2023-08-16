import pyperclip
import keyboard
import time

def convert_to_uppercase():
    original_clipboard = pyperclip.paste()
    keyboard.press_and_release("ctrl+c")
    time.sleep(0.1)
    copied_text = pyperclip.paste()
    uppercased_text = copied_text.upper()
    pyperclip.copy(uppercased_text)
    keyboard.press_and_release("ctrl+v")
    pyperclip.copy(original_clipboard)
    print("uppercase")


def convert_to_lowercase():
    original_clipboard = pyperclip.paste()
    keyboard.press_and_release("ctrl+c")
    time.sleep(0.1)
    copied_text = pyperclip.paste()
    lowercased_text = copied_text.lower()
    pyperclip.copy(lowercased_text)
    keyboard.press_and_release("ctrl+v")
    pyperclip.copy(original_clipboard)
    print("lowercase")


def convert_to_titlecase():
    original_clipboard = pyperclip.paste()
    keyboard.press_and_release("ctrl+c")
    time.sleep(0.1)
    copied_text = pyperclip.paste()
    words = copied_text.split()
    titlecased_text = copied_text.lower()
    titlecased_text = [word.capitalize() for word in words]
    titlecased_text = " ".join(titlecased_text)
    pyperclip.copy(titlecased_text)
    keyboard.press_and_release("ctrl+v")
    pyperclip.copy(original_clipboard)
    print("titlecase")

def main():
    # print("Press Ctrl + Shift + U to convert selected text to uppercase.")
    keyboard.add_hotkey("ctrl+shift+u", convert_to_uppercase)
    keyboard.add_hotkey("ctrl+shift+l", convert_to_lowercase)
    keyboard.add_hotkey("ctrl+shift+t", convert_to_titlecase)
    keyboard.wait("esc")

if __name__ == "__main__":
    main()


