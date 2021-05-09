from tkinter import *
from SQLite import *


def render_page_for_updating(blocks, parent_frame):
    block_example = Frame(parent_frame)
    block_entry = Frame(parent_frame)

    label = Label(parent_frame, text='Write index of row you want to update and new data')
    entry = Entry(parent_frame, width=5, justify=CENTER)

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

    def update_callback():
        index_value = entry.get()
        if index_value == '':
            result_label['text'] = 'Write index and new data!'
            return
        unit_loc_value = unit_loc_entry.get()
        depart_loc_value = depart_loc_entry.get()
        employee_value = employee_entry.get()

        execute_query_sqlite(sqlLite_db, f"""
            UPDATE system
            SET unit_location = '{unit_loc_value}',
                depart_location = '{depart_loc_value}',
                employee = '{employee_value}'
            WHERE id = {index_value}
        """)
        result_label['text'] = f"Row with index ({index_value}) has been updated"

    button = Button(parent_frame, text='Update', bg='#FFFF66', fg='black', activebackground='yellow', command=update_callback)

    blocks.append(label)
    blocks.append(entry)
    blocks.append(block_example)
    blocks.append(block_entry)
    blocks.append(button)
    blocks.append(result_label)

    label.pack()
    entry.pack(pady=5)
    block_example.pack()
    block_entry.pack()
    button.pack(pady=5)
    result_label.pack()
    parent_frame.pack()
