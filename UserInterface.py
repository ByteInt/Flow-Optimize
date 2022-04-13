import tkinter
from tkinter import *
from tkinter import ttk


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
    notebook = ttk.Notebook(root)  # Notebook是选项卡容器
    connection_frame = Frame(notebook)
    method_frame = Frame(notebook)
    parameters_frame = Frame(notebook)
    optimize_frame = Frame(notebook)
    # 暂定的四个选项卡
    add_device = Button(connection_frame, text='Add Device', command=add_apparatus)
    add_device.pack(padx=10, pady=10)
    device_list = Listbox(connection_frame)
    device_list.pack(padx=10, pady=10)

    notebook.add(connection_frame, text='Connection')
    notebook.add(method_frame, text='Method')
    notebook.add(parameters_frame, text='Parameters')
    notebook.add(optimize_frame, text='Optimize')
    notebook.pack(padx=10, pady=10, fill=tkinter.BOTH, expand=True)

    root.mainloop()

