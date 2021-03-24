from tkinter import *
from get_extra_info import *

root = Tk()

# create window for my program
root.geometry('600x650')

# save spinbox to have access to them from diff funcs
spinbox_dict = {}
# save blocks (for matrix) object to be able destroy it in future
blocks = []
# main matrix (array in array in array)
matrix = []
#
main_best_row = []
#
main_best_col = [[], 0]


# get sum of all elements of array
def get_sum_of_array(row):
    sum = 0
    for el in row:
        sum += el
    return sum


# render best row and best column (red color)
def show_best_row_and_column(row, data):
    global main_best_row
    global main_best_col

    for el in main_best_row:
        el['fg'] = 'black'

    old_block = main_best_col[0]
    old_col = main_best_col[1]
    for y_row in old_block:
        y_row[old_col]['fg'] = 'black'

    for el in row:
        el['fg'] = 'red'

    new_block = data[0]
    new_col = data[1]
    for y_row in new_block:
        y_row[new_col]['fg'] = 'red'

    main_best_row = row
    main_best_col = data


# find best row and best column
def get_result():
    best_row_value = 0
    best_row = matrix[0][0]
    best_column_value = 0
    best_column = [matrix[0], 0]
    for z in matrix:
        for col in range(len(z[0])):
            column = []
            for row in range(len(z)):
                column.append(int(z[row][col].get()))
            col_sum = get_sum_of_array(column)
            if col_sum > best_column_value:
                best_column_value = col_sum
                best_column = [z, col]
        for y in range(len(z)):
            row = []
            for x in range(len(z[y])):
                row.append(int(z[y][x].get()))
            row_sum = get_sum_of_array(row)
            if row_sum > best_row_value:
                best_row_value = row_sum
                best_row = z[y]
    show_best_row_and_column(best_row, best_column)
    BEST_ROW['text'] = 'Найбільший рядок (сума) = ' + str(best_row_value)
    BEST_COLUMN['text'] = 'Найбільша колонка (сума) = ' + str(best_column_value)


#  button to get result
GET_RESULT_BUTTON = Button(root, text='Результат', bg='black', activebackground='black',
                           fg='white', activeforeground='red', cursor='heart', command=get_result)
#  frame for results
RESULTS = Frame(root)
# best row label
BEST_ROW = Label(RESULTS, text='Найбільший рядок (сума) = ?', width=30)
BEST_ROW.pack(side=LEFT)
# best column label
BEST_COLUMN = Label(RESULTS, text='Найбільша колонка (сума) = ?', width=30)
BEST_COLUMN.pack(side=LEFT)


# save input data (size of dimensions)
def save_input_data():
    result = {'A': int(spinbox_dict['A'].get()), 'B': int(spinbox_dict['B'].get()), 'C': int(spinbox_dict['C'].get())}
    global main_best_row
    global main_best_col
    main_best_row = []
    main_best_col = [[], 0]
    render_matrix(result['A'], result['B'], result['C'])
    return result


# render input fields for user`s data
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


#  create and render matrix (used in render_matrix())
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


# render matrix
def render_matrix(a_dim, b_dim, c_dim):
    BEST_ROW['text'] = 'Найбільший рядок (сума) = ?'
    BEST_COLUMN['text'] = 'Найбільша колонка (сума) = ?'
    RESULTS.pack_forget()
    GET_RESULT_BUTTON.pack_forget()
    for block in blocks:
        block.destroy()
    create_matrix(a_dim, b_dim, c_dim)
    RESULTS.pack(pady=10)
    GET_RESULT_BUTTON.pack()


create_input_fields()

root.mainloop()
