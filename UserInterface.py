import tkinter
from tkinter import *
from tkinter import ttk


def add_apparatus():
    def add_apparatus_ok():
        device_list.insert(0, device_name.get() + ' working at ' + working_mode.get() + ' mode')
        add_window.destroy()

    add_window = Toplevel()
    add_window.geometry('300x200')
    add_window.title('Add Device')
    ok_button = Button(add_window, text="OK", command=add_apparatus_ok, default='active')
    device_name_label = Label(add_window, text='Device name:')
    device_name = Entry(add_window, width=20)
    working_mode_label = Label(add_window, text='Working mode:')
    working_mode = ttk.Combobox(add_window)
    working_mode['value'] = ('Fixed', 'Optimize', 'Chained')

    device_name_label.pack(padx=5, pady=5)
    device_name.pack(padx=10, pady=10)
    working_mode_label.pack(padx=5, pady=5)
    working_mode.pack(padx=10, pady=10)
    ok_button.pack(padx=10, pady=10)
    add_window.mainloop()


def method_confirm():
    wait_time = int(experiment_time.get())
    interval_time = int(sample_interval.get())
    sample_num = int(sample_points.get())
    print('Sampling time:')
    for i in range(sample_num):
        print(wait_time + i * interval_time, 'mins')


if __name__ == '__main__':
    root = Tk()
    root.title('Flow Control')
    root.geometry('800x600')
    notebook = ttk.Notebook(root)  # Notebook是选项卡容器
    # 暂定的四个选项卡
    connection_frame = Frame(notebook)
    method_frame = Frame(notebook)
    parameters_frame = Frame(notebook)
    optimize_frame = Frame(notebook)
    # Connection选项卡内容
    add_device = Button(connection_frame, text='Add Device', command=add_apparatus)
    add_device.pack(padx=10, pady=10)
    device_list = Listbox(connection_frame, width=100, height=20)
    device_list.pack(padx=10, pady=10)

    # Method选项卡内容
    extime_label = Label(method_frame, text="Experiment time(min):")
    experiment_time = Entry(method_frame)
    sampinterval_label = Label(method_frame, text="Sampling interval(min):")
    sample_interval = Entry(method_frame)
    samppoints_label = Label(method_frame, text="Sample points:")
    sample_points = Spinbox(method_frame, increment=1)

    extime_label.pack(padx=5, pady=5)
    experiment_time.pack(padx=5, pady=5)
    sampinterval_label.pack(padx=5, pady=5)
    sample_interval.pack(padx=5, pady=5)
    samppoints_label.pack(padx=5, pady=5)
    sample_points.pack(padx=5, pady=5)
    method_confirm = Button(method_frame, text="Confirm", command=method_confirm)
    method_confirm.pack(padx=5, pady=5)

    #Parameters选项卡内容

    # 加载notebook选项卡组件
    notebook.add(connection_frame, text='Connection')
    notebook.add(method_frame, text='Method')
    notebook.add(parameters_frame, text='Parameters')
    notebook.add(optimize_frame, text='Optimize')
    notebook.pack(padx=10, pady=10, fill=tkinter.BOTH, expand=True)

    root.mainloop()
