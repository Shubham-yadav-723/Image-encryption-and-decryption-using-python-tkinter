from tkinter import *
from tkinter import filedialog
import webbrowser
root = Tk()
root.geometry("500x500")
root.columnconfigure(0, weight=1)  # sets the co-ordinates in center

new = 1
url = "https://www.linkedin.com/in/shubham-y-3852a8184/"


def openweb():
    webbrowser.open(url, new=new)


def file_open():
    global file1
    file1 = filedialog.askopenfile(
        mode="r", filetype=[('jpg file', '*.jpg'), ('png file', '*.png'), ('jpeg file', '*.jpeg')])  # gets the file from device
    filename.delete('1.0', 'end')
    filename.insert(END, file1.name)


def click(event):
    entry1.config(state=NORMAL)
    entry1.delete(0, END)


def encrypt_image():
    if file1 is not None:

        file_name = file1.name
        print(file_name)
        # getting the unique key entered by user
        key = entry1.get()
        print(file_name, key)

        file = open(file_name, 'rb')
        image = file.read()
        file.close()

        image = bytearray(image)    # byte of image in array
        for index, values in enumerate(image):
            # interchanging the key with array using XOR operator
            image[index] = values ^ int(key)
        fle = open(file_name, 'wb')
        fle.write(image)
        fle.close()

        successfull.config(text="Successfully Encrypted the image ",
                           fg="Red", font=("jost", 15, "bold"))

        remember.config(text=("Remember the key for Decryption = "+key))


def decrypt_image():
    if file1 is not None:

        file_name = file1.name
        print(file_name)
        key = entry1.get()  # getting the unique key entered by user
        print(file_name, key)

        file = open(file_name, 'rb')
        image = file.read()
        file.close()

        image = bytearray(image)    # byte of image in array
        for index, values in enumerate(image):
            # interchanging the key with array using XOR operator
            image[index] = values ^ int(key)
        fle = open(file_name, 'wb')
        fle.write(image)
        fle.close()
        successfull.config(text="Successfully Decrypted the image ",
                           fg="green", font=("jost", 15, "bold"))


# for encryption process
welcome_label = Label(root, text="Encrypt and Decrypt the image",
                      font=("jost", 20, "bold"), fg='Blue')
welcome_label.grid()


Btn1 = Button(root, text="Choose the image", command=file_open, font=(
    "jost", 15, "bold"), fg="white", bg='black')
Btn1.grid(pady=10)

support = Label(root, text="** Supports only Jpg, jpeg,and png format **",
                fg='red', font=("jost", 10))
support.place(x=100, y=90)

filename = Text(root, height=1, width=45)
filename.insert(END, "file is not choosen!")

filename.grid(pady=12)


entry1 = Entry(root, width=40)
entry1.insert(0, "Enter an integer key between 0 and 255")  # placeholder
entry1.config(state=DISABLED)
entry1.bind("<Button-1>", click)
entry1.grid(pady=15)

support1 = Label(root, text="**Same Key should be used for encryption and decryption **",
                 fg='red', font=("jost", 10))
support1.place(x=60, y=180)

encrypt = Button(root, text="Encrypt", command=encrypt_image, font=(
    "jost", 15, "bold"), fg="white", bg='red')
encrypt.place(x=130, y=220)

decrypt = Button(root, text="Decrypt", command=decrypt_image, font=(
    "jost", 15, "bold"), fg="white", bg='Green')
decrypt.place(x=260, y=220)

successfull = Label(root, text=" ")
successfull.grid(pady=65)

remember = Label(root, text="", fg="red", font=("jost", 10))
remember.place(x=140, y=320)


developerLabel = Label(root, text="-Shubham yadav",
                       fg="white", bg="black", font=("algeria", 10, "bold"))
developerLabel.grid(pady=15)

linkedin = Button(root, text="Connect to linkedin", fg="purple",
                  bg="skyblue", font=("jost", 13, "bold"), command=openweb)
linkedin.grid(pady=2)


root.mainloop()
