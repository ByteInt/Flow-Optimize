from tkinter import *


def add_apparatus():
    device_list.insert(0, 'Device')


if __name__ == '__main__':
    root = Tk()
    root.title('Flow Control')
    root.geometry('800x600')
    add_device = Button(root, text='Add Device', command=add_apparatus)
    add_device.pack()
    device_list = Listbox(root)
    device_list.pack()
    root.mainloop()
