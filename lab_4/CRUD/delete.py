from tkinter import *
from SQLite import *


def render_page_for_deleting(blocks, parent_frame):
    label = Label(parent_frame, text='Write index of row you want to delete')
    entry = Entry(parent_frame, width=5, justify=CENTER)
    result_label = Label(parent_frame)

    def delete_callback():
        index = blocks[1].get()
        rows = execute_query_sqlite(sqlLite_db, f'SELECT * from system where id = {index}')
        pointer = -1
        for row in rows: pointer = row[0]
        if pointer == -1:
            result_label['text'] = f"Row with index ({index}) doesn't exist"
            return
        execute_query_sqlite(sqlLite_db, f"DELETE FROM system WHERE id = {index}")
        result_label['text'] = f"Row with index ({index}) has been deleted"

    button = Button(parent_frame, text='Delete', bg='#FFA07A', fg='black', activebackground='red', command=delete_callback)

    blocks.append(label)
    blocks.append(entry)
    blocks.append(button)
    blocks.append(result_label)

    label.pack()
    entry.pack()
    button.pack(pady=5)
    result_label.pack()
    parent_frame.pack()
