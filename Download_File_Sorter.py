import tkinter
import customtkinter
import os 
import shutil
from pathlib import Path
from functools import partial
from tkinter import ttk
import time


# ------------Funtions--------------------


def move_file(file, folder_path):
    file_path = Download_folder + "\\" + file

    try: 
     os.mkdir(folder_path)
    except:
     pass

    try:
     shutil.move(file_path,folder_path)
    except: 
       print("Error in moving file: " + str(file))

def counter(file_list):
   
    # This counts the number of pdfs, documents, and multimedia content given the list of files.
    Total_count = 0
    multi_med_count = 0
    documents_count = 0
    pdf_count = 0
    OtherFile_count = 0

    for file in file_list:
        filename, extension = os.path.splitext(file)
        Total_count = Total_count + 1 
        

        if extension in doc_extensions:
            documents_count = documents_count +1

        elif extension in multiMed_extensions:
            multi_med_count = multi_med_count +1
        
        elif extension in pdf_extensions:
            pdf_count = pdf_count +1

        else: 
            OtherFile_count = OtherFile_count +1

    
    movable_files = multi_med_count + documents_count + pdf_count

    return Total_count, movable_files, documents_count, multi_med_count, pdf_count



def move_files(file_list, movable_files):

    
    tasks = movable_files

    for file in file_list:

        moved = 0
        time.sleep(0.025)
        filename, extension = os.path.splitext(file)

        # The loop. 
        if extension in doc_extensions:
            move_file(file, doc_folder_path)
            moved+=1
            my_progress['value']+=(moved/tasks)*100
            

        elif extension in multiMed_extensions:
            move_file(file,multi_folder_path)
            moved+=1
            my_progress['value']+=(moved/tasks)*100

        elif extension in pdf_extensions:
            move_file(file,pdf_folder_path)
            moved+=1
            my_progress['value']+=(moved/tasks)*100

        else: 
            pass

        app.update_idletasks()
    percent.set(f"{tasks} files moved successfully!")



def Display_count(Total_count, documents_count, multi_med_count, pdf_count):
    output_lable.config(text = "Total files: " + str(Total_count) + "\n" + "documents: " + str(documents_count) + "\n" + "Multimedia files: " + str(multi_med_count) + "\n" + "PDF files: " + str(pdf_count) + "\n" + "Other FIles: " + str(pdf_count))
# ------------------------------------------------------------------- main-----------------------------------




  #finding the download folder
Download_folder = str(Path.home()/"Downloads").replace("\\","\\\\")


# The name of the 3 folders"
doc_folder = "Sorted_doc_Files"
multimedia_folder = "Sorted_Multimedia_files"
pdf_folder = "Sorted_pdf_files"


# List all the files in the test directory to be parsed into folders.
Files = os.listdir(Download_folder)


# create a new folder path to be created.
doc_folder_path = os.path.join(Download_folder,doc_folder)
multi_folder_path = os.path.join(Download_folder,multimedia_folder)
pdf_folder_path = os.path.join(Download_folder,pdf_folder)


# The list of extensions.
multiMed_extensions = [".jpeg", ".jpg", ".jped", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".svg", ".ico", ".mov", ".mp4"]
doc_extensions = [".epub", ".docx", ".txt", ".csv", ".doc", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods", ".odp"]
pdf_extensions = [".pdf"]


Total_count, movable_files, documents_count, multi_med_count, pdf_count = counter(Files)

# --------------- THE GUI ------------------


app = customtkinter.CTk()
app.geometry("720x480")
app.title("File Sorter")
percent = tkinter.StringVar()


# adding UI ellements
title = customtkinter.CTkLabel(app, text="Sort pdf files, documents and multimedia in your downloads folder, \n Accordingly three new folders will be created in your Download folder and the files will be sorted. ")
title.pack(padx=10, pady=10)

count_button = tkinter.Button(app, text = "Count Files in Downloads", height=2,width=20, font=("Arial", 16, "bold"), command=lambda:Display_count(Total_count, documents_count, multi_med_count, pdf_count))
count_button.pack(padx=10, pady=10)

output_lable = tkinter.Label(app,text="", font = ("Arial,14"))
output_lable.pack()

sort_button = tkinter.Button(app, text = "Sort Files", height=2,width=20, font=("Arial", 16, "bold"), command=lambda:move_files(Files, movable_files))
sort_button.pack(padx=10, pady=10)

my_progress = ttk.Progressbar(app, orient="horizontal", length=640, mode="determinate")
my_progress.pack(pady=10)

percentLable = ttk.Label(app, textvariable=percent).pack()

# Run loop
app.mainloop()

