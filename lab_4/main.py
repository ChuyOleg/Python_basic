from mySQL import *
from postgreSQL import *
from extra_functions import *
from CRUD.read import *
from CRUD.delete import *
from CRUD.create import *
from CRUD.update import *

root = Tk()

root.geometry('600x600')

active_frame = Frame(root)

active_blocks = []


def read():
    rows = execute_query_sqlite(sqlLite_db, 'SELECT * FROM system')
    destroy_old_blocks(active_blocks)
    render_page_for_reading(rows, active_frame, active_blocks)


def delete():
    destroy_old_blocks(active_blocks)
    render_page_for_deleting(active_blocks, active_frame)


def create():
    destroy_old_blocks(active_blocks)
    render_page_for_creating(active_blocks, active_frame)


def update():
    destroy_old_blocks(active_blocks)
    render_page_for_updating(active_blocks, active_frame)


head = Frame(root)

create_button = Button(head, text="Create", bg='green', activebackground='black', activeforeground='red', width='7', command=create)
read_button = Button(head, text="Read", bg='green', activebackground='black', activeforeground='red', width='7', command=read)
update_button = Button(head, text="Update", bg='green', activebackground='black', activeforeground='red', width='7', command=update)
delete_button = Button(head, text="Delete", bg='green', activebackground='black', activeforeground='red', width='7', command=delete)

create_button.pack(side=LEFT)
read_button.pack(side=LEFT)
update_button.pack(side=LEFT)
delete_button.pack(side=LEFT)

head.pack(pady=10)

root.mainloop()
