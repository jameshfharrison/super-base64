import base64 # library for decoding base64
import pyperclip  # library for copying to clipboard


def decodeInput():
    encoded = input("please put text to decode: ")
    decoded = base64.b64decode(encoded)
    decoded = decoded.decode("utf-8")
    print("your text is: {0} \n".format(decoded))
    copy2clip(decoded)


def copy2clip(txt):
    pyperclip.copy(txt)


def main():

    exit = False

    while not exit:
        flag = input("Want to decode some text? (y/n): ")

        if flag.lower() == "y":
            decodeInput()
        elif flag.lower() == "n":
            exit = True
            print("Goodbye! \n")
        else:
            print("Please enter y or n \n")


if __name__ == '__main__':
    main()
