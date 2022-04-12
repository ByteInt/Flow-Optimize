# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    apparatus = [[]]
    ans = 'y'
    optimize_dimension = 0
    while ans.upper() == 'Y':
        print('Please input the apparatus type:')
        apparatus_type = input()
        print('Please input the port of this ')
        apparatus_port = input()
        print('Please input the working mode of this apparatus:\n(F for fixed value, O for optimize, C for chained)')
        working_mode = input()
        if working_mode.upper() == 'F':
            print('Please input this fixed value:')
            fixed_value = input()
            apparatus.append([apparatus_type, apparatus_port, working_mode, fixed_value, 0])
        elif working_mode.upper() == 'O':
            print('Maximum of the optimizing range?')
            optimize_max = input()
            print('Minimum of the optimizing range?')
            optimize_min = input()
            apparatus.append([apparatus_type, apparatus_port, working_mode, optimize_max, optimize_min])
            optimize_dimension += 1
        elif working_mode.upper() == 'C':
            print('ID of chained device?')
            chained_ID = input()
            print('Multiply constant?')
            constant = input()
            apparatus.append([apparatus_type, apparatus_port, working_mode, chained_ID, constant])
        print('Add another apparatus?(y/n)')
        ans = input()
    print('ID\tApparatus type\tPort\tWorking mode\tParam1\tParam2')
    for i in range(len(apparatus)):
        print(i, apparatus[i])
        # 这一步之后，仪器的ID会从1开始，而0的位置为空。

    print("Editing experiment method.")
    # Method部分代码
    print('Balance time in minutes')
    balance_time = input()
    print('Sample points?')
    sample_points = input()
    print('sampling interval?')
    interval = input()
    print('There are', optimize_dimension, 'values to optimize.')



# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
