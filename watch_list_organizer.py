import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
import os

# Path to the CSV file
csv_file_path = "movies_list.csv"

def clear_entry(event, entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, tk.END)

def add_movie():
    movie_title = movie_title_entry.get()
    last_date = last_date_entry.get()

    if movie_title and last_date:
        movie_list.insert("", "end", values=(movie_title, last_date))
        save_to_csv()  # Save the list after adding
        movie_title_entry.delete(0, tk.END)
        last_date_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Both fields must be filled!")

def remove_movie():
    selected_item = movie_list.selection()
    if selected_item:
        movie_list.delete(selected_item)
        save_to_csv()  # Save the list after removing
    else:
        messagebox.showwarning("Selection Error", "Please select a movie to remove!")

def open_edit_window():
    selected_item = movie_list.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a movie to edit!")
        return

    movie_title, last_date = movie_list.item(selected_item, 'values')

    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Movie")

    tk.Label(edit_window, text="New Movie Title:").pack(pady=5)
    new_movie_title_entry = tk.Entry(edit_window)
    new_movie_title_entry.pack(pady=5)
    new_movie_title_entry.insert(0, movie_title)

    tk.Label(edit_window, text="New Last Date to Watch:").pack(pady=5)
    new_last_date_entry = tk.Entry(edit_window)
    new_last_date_entry.pack(pady=5)
    new_last_date_entry.insert(0, last_date)

    def update_movie():
        new_movie_title = new_movie_title_entry.get()
        new_last_date = new_last_date_entry.get()
        if new_movie_title and new_last_date:
            movie_list.item(selected_item, values=(new_movie_title, new_last_date))
            save_to_csv()  # Save the list after editing
            edit_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Both fields must be filled!")

    ok_button = tk.Button(edit_window, text="OK", command=update_movie)
    ok_button.pack(pady=5, side=tk.LEFT, padx=10)

    cancel_button = tk.Button(edit_window, text="Cancel", command=edit_window.destroy)
    cancel_button.pack(pady=5, side=tk.RIGHT, padx=10)

def move_up():
    selected_item = movie_list.selection()
    if selected_item:
        index = movie_list.index(selected_item)
        if index > 0:
            movie_list.move(selected_item, movie_list.parent(selected_item), index - 1)
            save_to_csv()  # Save the list after moving
    else:
        messagebox.showwarning("Selection Error", "Please select a movie to move!")

def move_down():
    selected_item = movie_list.selection()
    if selected_item:
        index = movie_list.index(selected_item)
        if index < len(movie_list.get_children()) - 1:
            movie_list.move(selected_item, movie_list.parent(selected_item), index + 1)
            save_to_csv()  # Save the list after moving
    else:
        messagebox.showwarning("Selection Error", "Please select a movie to move!")

def save_to_csv():
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Movie Title", "Last Date to Watch"])
        for row_id in movie_list.get_children():
            row = movie_list.item(row_id)['values']
            writer.writerow(row)

def load_from_csv():
    if os.path.exists(csv_file_path):
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                movie_list.insert("", "end", values=row)

root = tk.Tk()
root.title("Movie Organizer")
root.geometry("600x400")

frame1 = tk.Frame(root)
frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

columns = ("Movie Title", "Last Date to Watch")
movie_list = ttk.Treeview(frame1, columns=columns, show="headings")
movie_list.heading("Movie Title", text="Movie Title")
movie_list.heading("Last Date to Watch", text="Last Date to Watch")
movie_list.pack(fill=tk.BOTH, expand=True)

frame2 = tk.Frame(root)
frame2.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

default_movie_title_text = "Enter movie title"
default_last_date_text = "Enter last date to watch"

movie_title_entry = tk.Entry(frame2)
movie_title_entry.pack(pady=5)
movie_title_entry.insert(0, default_movie_title_text)
movie_title_entry.bind("<FocusIn>", lambda event: clear_entry(event, movie_title_entry, default_movie_title_text))

last_date_entry = tk.Entry(frame2)
last_date_entry.pack(pady=5)
last_date_entry.insert(0, default_last_date_text)
last_date_entry.bind("<FocusIn>", lambda event: clear_entry(event, last_date_entry, default_last_date_text))

add_button = tk.Button(frame2, text="Add", width=20, command=add_movie)
add_button.pack(pady=5)

remove_button = tk.Button(frame2, text="Remove", width=20, command=remove_movie)
remove_button.pack(pady=5)

edit_button = tk.Button(frame2, text="Edit", width=20, command=open_edit_window)
edit_button.pack(pady=5)

up_button = tk.Button(frame2, text="Up", width=20, command=move_up)
up_button.pack(pady=5)

down_button = tk.Button(frame2, text="Down", width=20, command=move_down)
down_button.pack(pady=5)

# Load the movie list from the CSV file if it exists
load_from_csv()

root.mainloop()
