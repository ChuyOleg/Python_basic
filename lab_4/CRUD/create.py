from tkinter import *
from SQLite import *


def render_page_for_creating(blocks, parent_frame):
    block_example = Frame(parent_frame)
    block_entry = Frame(parent_frame)

    unit_loc_label = Label(block_example, text='Unit Location', width=15, highlightbackground='black',
                           highlightthickness=1, bd=5)
    depart_loc_label = Label(block_example, text='Department Location', width=20, highlightbackground='black',
                             highlightthickness=1, bd=5)
    employee_label = Label(block_example, text='Employee', width=15, highlightbackground='black', highlightthickness=1,
                           bd=5)
    result_label = Label(parent_frame)

    unit_loc_entry = Entry(block_entry, width=15, highlightbackground='black', highlightthickness=1, bd=5,
                           justify=CENTER)
    depart_loc_entry = Entry(block_entry, width=20, highlightbackground='black', highlightthickness=1, bd=5,
                             justify=CENTER)
    employee_entry = Entry(block_entry, width=15, highlightbackground='black', highlightthickness=1, bd=5,
                           justify=CENTER)

    unit_loc_label.pack(side=LEFT)
    depart_loc_label.pack(side=LEFT)
    employee_label.pack(side=LEFT)

    unit_loc_entry.pack(side=LEFT)
    depart_loc_entry.pack(side=LEFT)
    employee_entry.pack(side=LEFT)

    def add_callback():
        unit_loc_value = unit_loc_entry.get()
        depart_loc_value = depart_loc_entry.get()
        employee_value = employee_entry.get()
        execute_query_sqlite(sqlLite_db, f"""
            INSERT INTO system(unit_location, depart_location, employee)
            VALUES ('{unit_loc_value}', '{depart_loc_value}', '{employee_value}')"""
        )
        result_label['text'] = f"Row ({unit_loc_value}, {depart_loc_value}, {employee_value}) has been successfully created!"

    add_button = Button(parent_frame, text='Create', bg='#7FFF00', fg='black', activebackground='green', command=add_callback)

    blocks.append(block_example)
    blocks.append(block_entry)
    blocks.append(add_button)
    blocks.append(result_label)

    block_example.pack()
    block_entry.pack()
    add_button.pack(pady=5)
    result_label.pack()
    parent_frame.pack()
