from tkinter import *

root = Tk()

root.geometry('600x600')

input_frame = Frame(root).pack()

# make more readable code

input_A_frame = Frame(root)
label_A = Label(input_A_frame, text='Вимір A (1-4)').pack(side=LEFT)
spinbox_A = Spinbox(input_A_frame, width=3, from_=1, to=4)
spinbox_A.pack(side=LEFT)

input_B_frame = Frame(root)
label_B = Label(input_B_frame, text='Вимір B (1-4)').pack(side=LEFT)
spinbox_B = Spinbox(input_B_frame, width=3, from_=1, to=4)
spinbox_B.pack(side=LEFT)

input_C_frame = Frame(root)
label_C = Label(input_C_frame, text='Вимір C (1-4)').pack(side=LEFT)
spinbox_C = Spinbox(input_C_frame, width=3, from_=1, to=4)
spinbox_C.pack(side=LEFT)


def save_input():
    result = {'A': int(spinbox_A.get()), 'B': int(spinbox_B.get()), 'C': int(spinbox_C.get())}
    render_matrix(result['C'])
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


def create_matrix(number, current_num):
    my_padding = get_padding(number, current_num)
    my_side = get_side(number, current_num)
    frame_for_matrix = Frame(root)
    frame = Frame(frame_for_matrix, width=80, height=80, bg='white', highlightbackground='black',
                  highlightcolor='black', highlightthickness=1)
    print(my_padding, my_side)
    frame.pack(side=my_side)
    frame_for_matrix.pack(ipadx=my_padding)
    return frame


def render_matrix(number):
    for num in range(number):
        label = create_matrix(number, num)


matrix_row = Entry(root, width=20)

input_A_frame.pack()
input_B_frame.pack()
input_C_frame.pack()

input_button = Button(input_frame, text='зберегти дані', bg='black', activebackground='black',
                      fg='white', activeforeground='white', cursor='heart', command=save_input).pack()
matrix_row.pack()

root.mainloop()
