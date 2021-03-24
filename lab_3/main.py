from tkinter import *
from get_extra_info import *

root = Tk()

root.geometry('600x600')

# save spinbox to have access to them from diff funcs
spinbox_dict = {}
# save blocks (for matrix) object to be able destroy it in future
blocks = []
# main matrix (array in array in array)
matrix = []


def get_sum_of_row(row):
    sum = 0
    for el in row:
        sum += el
    return sum


def show_best_column(data):
    block = data[0]
    col = data[1]
    for row in block:
        row[col]['fg'] = 'red'


def show_best_row(row):
    for el in row:
        el['fg'] = 'red'


def get_result():
    best_row_value = 0
    best_row = matrix[0][0]
    best_column_value = 0
    best_column = [matrix[0], 0]
    for z in matrix:
        for y in z:
            row = []
            for x in y:
                row.append(int(x.get()))
            row_sum = get_sum_of_row(row)
            if row_sum > best_row_value:
                best_row_value = row_sum
                best_row = y
    show_best_row(best_row)
    show_best_column(best_column)


#  button to get result
GET_RESULT_BUTTON = Button(root, text='Результат', bg='black', activebackground='black',
                           fg='white', activeforeground='red', cursor='heart', command=get_result)


def save_input_data():
    result = {'A': int(spinbox_dict['A'].get()), 'B': int(spinbox_dict['B'].get()), 'C': int(spinbox_dict['C'].get())}
    render_matrix(result['A'], result['B'], result['C'])
    return result


def create_input_fields():
    dimensions = ('A', 'B', 'C')
    input_frames = {}
    for dim in dimensions:
        input_frames[dim] = Frame(root)
        Label(input_frames[dim], text='Вимір ' + dim + ' (1-4)').pack(side=LEFT)
        spinbox_dict[dim] = Spinbox(input_frames[dim], width=3, from_=1, to=4)
        spinbox_dict[dim].pack(side=LEFT)
    for frame in input_frames:
        input_frames[frame].pack(pady=5)
    Button(root, text='зберегти дані', bg='black', activebackground='black',
           fg='white', activeforeground='red', cursor='heart', command=save_input_data).pack(pady=10)


def create_matrix(a_dim, b_dim, c_dim):
    global matrix
    matrix = []
    for current_num in range(c_dim):
        my_padding = get_padding(c_dim, current_num)
        my_side = get_side(c_dim, current_num)
        frame_for_matrix = Frame(root)
        frame = Frame(frame_for_matrix, highlightbackground='black', highlightcolor='black', highlightthickness=1)
        blocks.append(frame_for_matrix)
        matrix.append([])
        for x in range(b_dim):
            row = Frame(frame)
            matrix[len(matrix) - 1].append([])
            for y in range(a_dim):
                cell = Entry(row, width=2, justify=CENTER)
                cell.insert(END, 0)
                cell.pack(side=LEFT)
                matrix[len(matrix) - 1][len(matrix[len(matrix) - 1]) - 1].append(cell)
            row.pack()
        frame.pack(side=my_side)
        frame_for_matrix.pack(ipadx=my_padding, ipady=3)
    matrix = matrix


def render_matrix(a_dim, b_dim, c_dim):
    GET_RESULT_BUTTON.pack_forget()
    for block in blocks:
        block.destroy()
    create_matrix(a_dim, b_dim, c_dim)
    GET_RESULT_BUTTON.pack(pady=10)


create_input_fields()

root.mainloop()
