from tkinter import *


def add_apparatus():
    def add_apparatus_ok():
        device_list.insert(0, device_name.get())
        add_window.destroy()
    add_window = Toplevel()
    add_window.geometry('300x200')
    add_window.title('Add Device')
    ok_button = Button(add_window, text="OK", command=add_apparatus_ok, default='active')
    device_name_label = Label(add_window, text='Device name:')
    device_name = Entry(add_window, width=20)
    device_name_label.pack()
    device_name.pack(padx=20, pady=20)
    ok_button.pack(padx=20, pady=20)
    add_window.mainloop()



if __name__ == '__main__':
    root = Tk()
    root.title('Flow Control')
    root.geometry('800x600')
    add_device = Button(root, text='Add Device', command=add_apparatus)
    add_device.pack(padx=20, pady=20)
    device_list = Listbox(root)
    device_list.pack(padx=20, pady=20)
    root.mainloop()

