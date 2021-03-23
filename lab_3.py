from tkinter import *

root = Tk()

root.geometry('600x600')

input_frame = Frame(root).pack()

input_frames = {}
spinbox_dict = {}
matrix = []
get_result_button = Button(root, text='Результат', bg='black', activebackground='black',
                           fg='white', activeforeground='red', cursor='heart')


def create_input_fields():
    dimensions = ('A', 'B', 'C')
    for dim in dimensions:
        input_frames[dim] = Frame(root)
        Label(input_frames[dim], text='Вимір ' + dim + ' (1-4)').pack(side=LEFT)
        spinbox_dict[dim] = Spinbox(input_frames[dim], width=3, from_=1, to=4)
        spinbox_dict[dim].pack(side=LEFT)


def save_input():
    result = {'A': int(spinbox_dict['A'].get()), 'B': int(spinbox_dict['B'].get()), 'C': int(spinbox_dict['C'].get())}
    render_matrix(result['A'], result['B'], result['C'])
    return result


def get_padding(number, current_num):
    if number == 4:
        if current_num == 0 or current_num == 3:
            return 120
        else:
            return 40
    elif number == 3:
        if current_num == 0 or current_num == 2:
            return 80
        else:
            return 0
    elif number == 2:
        return 40
    else:
        return 0


def get_side(number, current_num):
    if number == 4:
        if current_num == 0 or current_num == 1:
            return 'right'
        else:
            return 'left'
    elif number == 3:
        if current_num == 0:
            return 'right'
        else:
            return 'left'
    elif number == 2:
        if current_num == 0:
            return 'right'
        else:
            return 'left'
    else:
        return 'left'


def create_matrix(a_dim, b_dim, c_dim, current_num):
    my_padding = get_padding(c_dim, current_num)
    my_side = get_side(c_dim, current_num)
    frame_for_matrix = Frame(root)
    frame = Frame(frame_for_matrix, highlightbackground='black', highlightcolor='black', highlightthickness=1)
    matrix.append(frame_for_matrix)
    for x in range(b_dim):
        row = Frame(frame)
        for y in range(a_dim):
            cell = Entry(row, width=2)
            cell.pack(side=LEFT)
        row.pack()
    frame.pack(side=my_side)
    frame_for_matrix.pack(ipadx=my_padding, ipady=3)
    return frame


def render_matrix(a_dim, b_dim, c_dim):
    get_result_button.pack_forget()
    for block in matrix:
        block.destroy()
    for num in range(c_dim):
        create_matrix(a_dim, b_dim, c_dim, num)
    get_result_button.pack(pady=10)


create_input_fields()
input_frames['A'].pack(pady=5)
input_frames['B'].pack(pady=5)
input_frames['C'].pack(pady=5)

input_button = Button(input_frame, text='зберегти дані', bg='black', activebackground='black',
                      fg='white', activeforeground='red', cursor='heart', command=save_input).pack(pady=10)

root.mainloop()
