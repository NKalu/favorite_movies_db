from tkinter import Tk, Label, StringVar, Entry, Listbox, Scrollbar, Button, END
from db_operations import MovieDatabase

MovieDB = MovieDatabase("fav_movies.db")

def format_row(row):
    return "{0})   {1}   {2}   {3}   {4}".format(row[0],row[1], row[2], row[3], row[4])

def get_row(event):
    global selected_row
    try:
        index = display_box.curselection()[0]
        selected_row = display_box.get(index)
        selected_row = selected_row.split('  ')
        title_entry.delete(0, END)
        title_entry.insert(END, selected_row[1])
        director_entry.delete(0, END)
        director_entry.insert(END, selected_row[2])
        year_entry.delete(0, END)
        year_entry.insert(END, selected_row[3])
        rating_entry.delete(0, END)
        rating_entry.insert(END, selected_row[4])
    except IndexError:
        pass


def view_all_command():
    display_box.delete(0, END)
    for row in MovieDB.view_all():
        display_box.insert(END, format_row(row))


def search_command():
    display_box.delete(0, END)
    for row in MovieDB.search(title_entry.get(), director_entry.get(), year_entry.get(), rating_entry.get()):
        display_box.insert(END, format_row(row))


def add_command():
    MovieDB.insert(title_entry.get(), director_entry.get(), year_entry.get(), rating_entry.get())
    display_box.delete(0, END)
    display_box.insert(END, (title_entry.get().strip("{}"), director_entry.get().strip("{}"), year_entry.get(), rating_entry.get()))


def update_command():
    MovieDB.update(selected_row[0], title_entry.get(), director_entry.get(), year_entry.get(), rating_entry.get())

def delete_command():
    MovieDB.delete(selected_row[0])
    view_all_command()

def close_command():
    window.destroy()


window = Tk()
window.title("Favorite Movies Database")

#Creates places to input data
movie_title = Label(window, text="Title")
movie_title.grid(row=0, column=0)
movie_title_text = StringVar()
title_entry = Entry(window, textvariable=movie_title_text)
title_entry.grid(row=0, column=1)

movie_director = Label(window, text="Director")
movie_director.grid(row=0, column=2)
movie_director_text = StringVar()
director_entry = Entry(window, textvariable=movie_director_text)
director_entry.grid(row=0, column=3)

movie_year = Label(window, text="Year Released")
movie_year.grid(row=1, column=0)
movie_year_text = StringVar()
year_entry = Entry(window, textvariable=movie_year_text)
year_entry.grid(row=1, column=1)

personal_rating = Label(window, text="Personal Rating")
personal_rating.grid(row=1, column=2)
personal_rating_text = StringVar()
rating_entry = Entry(window, textvariable=personal_rating_text)
rating_entry.grid(row=1, column=3)

scroll_bar = Scrollbar(window)
scroll_bar.grid(row=2, column=2)
display_box = Listbox(window, height=6, width=45)
display_box.grid(row=2, column=0, rowspan=6, columnspan=2)
display_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=display_box.yview())

#Creates a binding to select from display box
display_box.bind('<<ListboxSelect>>', get_row)

view_all = Button(window, text="View Movies", width=15, command=view_all_command)
view_all.grid(row=10, column=0)

search_db = Button(window, text="Search For Movie", width=15, command=search_command)
search_db.grid(row=10, column=1)

add_movie = Button(window, text="Add Movie", width=15, command=add_command)
add_movie.grid(row=10, column=2)

update_movie = Button(window, text="Update Movie Entry", width=15, command=update_command)
update_movie.grid(row=11, column=0)

delete_movie = Button(window, text="Delete Movie", width=15, command=delete_command)
delete_movie.grid(row=11, column=1)

close_app = Button(window, text="Close", width=15, command=close_command)
close_app.grid(row=11, column=2)

window.mainloop()