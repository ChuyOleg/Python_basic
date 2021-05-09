from tkinter import *


def create_table_row_for_rendering(row, parent_frame, blocks):
    block = Frame(parent_frame)

    border_color = 'red' if (row[0] == 'Id') else 'black'

    id_block = Label(block, text=row[0], width=3, highlightbackground=border_color, highlightthickness=1, bd=5)
    unit_loc_block = Label(block, text=row[1], width=15, highlightbackground=border_color, highlightthickness=1, bd=5)
    depart_loc_block = Label(block, text=row[2], width=20, highlightbackground=border_color, highlightthickness=1, bd=5)
    employee_block = Label(block, text=row[3], width=15, highlightbackground=border_color, highlightthickness=1, bd=5)

    id_block.pack(side=LEFT)
    unit_loc_block.pack(side=LEFT)
    depart_loc_block.pack(side=LEFT)
    employee_block.pack(side=LEFT)

    blocks.append(block)
    block.pack()


def render_page_for_reading(rows, parent_frame, blocks):
    create_table_row_for_rendering(['Id', 'Unit Location', 'Department Location', 'Employee'], parent_frame, blocks)
    for row in rows:
        create_table_row_for_rendering(row, parent_frame, blocks)
    parent_frame.pack(pady=10)
