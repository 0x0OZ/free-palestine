#!/usr/bin/python3

import tkinter as tk
import csv

csv_file = "data.csv"
markdown_file = "data.md"


def create_markdown_table(csv_file):
    with open(csv_file, newline="") as csvfile:
        reader = csv.reader(csvfile)
        table = "| " + " | ".join(next(reader)) + " |\n"
        table += "| " + " | ".join(["---"] * len(next(reader))) + " |\n"

        for row in reader:
            table += "| " + " | ".join(row) + " |\n"

    with open(markdown_file, "w") as mdfile:
        mdfile.write(table)


def save_to_csv():
    title = title_entry.get()
    timeline = timeline_entry.get()
    categories = categories_entry.get()
    description = description_entry.get()
    link = link_entry.get()
    link = link.replace("\n", "")
    link = link.replace(",", ".")
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([title, timeline, categories, description, link])

    create_markdown_table(csv_file) 
    # Clear the entry fields after saving
    title_entry.delete(0, tk.END)
    timeline_entry.delete(0, tk.END)
    categories_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    link_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Data Entry Form")

# Labels
tk.Label(root, text="Title:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Timeline:").grid(row=1, column=0, padx=5, pady=5)
tk.Label(root, text="Categories:").grid(row=2, column=0, padx=5, pady=5)
tk.Label(root, text="Description:").grid(row=3, column=0, padx=5, pady=5)
tk.Label(root, text="Link:").grid(row=4, column=0, padx=5, pady=5)

# Entry fields
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1)
timeline_entry = tk.Entry(root)
timeline_entry.grid(row=1, column=1)
categories_entry = tk.Entry(root)
categories_entry.grid(row=2, column=1)
description_entry = tk.Entry(root)
description_entry.grid(row=3, column=1)
link_entry = tk.Entry(root)
link_entry.grid(row=4, column=1)

# Save button
save_button = tk.Button(root, text="Save", command=save_to_csv)
save_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
