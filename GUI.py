# Name: Nir Hemo
# ID: 204288187

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
from PIL import Image, ImageTk
from Image_processing import *


def get_list(event):  # Get the list of imges from the path
    list_img.delete(0, END)
    path_entry.delete(0, END)
    global path
    path = filedialog.askdirectory()  # open a dialog with the computer to choose a diractory
    path_entry.insert(0, path)
    dirc = os.listdir(path)
    counter = 0
    for file in dirc:  # If the file is not from this list it will not add it to the list
        if file[-4:] == ".gif" or file[-4:] == ".bmp" or file[-4:] == ".jpg":
            list_img.insert("end", file)
            counter += 1
    if counter == 0:
        messagebox.showerror("Error","The folder is empty, please select dirctory with photos and type of: gif, bmp, jpg")  # Pop up a msg for the user


def get_name(event):  # Show the img in a new window
    try:
        dirc = os.listdir(path)     # Get list of files from the Path
        global selected_files_list      # List of names of the Selcted pics
        selected_files_list = []
        files_list = []
        items_num = list_img.curselection()
        first_item = list_img.get("active")
        for file in dirc:  # If the file is not from this list it will not add it to the list
            if file[-4:] == ".gif" or file[-4:] == ".bmp" or file[-4:] == ".jpg":
                files_list.append(file)
        name_file = files_list[items_num[0]]
        global first_photo_path         # The Path of the first Image
        first_photo_path = path + "/" + name_file
        for item in items_num:
            selected_files_list.append(files_list[item])
        return photo_preview(name_file)
    except:
        messagebox.showerror("Error", "Please select folder first")


def photo_preview(name):
    global photo_file
    photo_file = Image.open(path + "/" + name)  # Get the full path of the file
    demnsion = photo_file.size  # get the demnsion
    height = demnsion[0]
    width = demnsion[1]  # Calculate the img size to 372x210
    new_height = (372 / float(height)) * float(height)
    new_width = (210 / float(width)) * float(width)
    size = (int(new_height), int(new_width))
    photo_file = photo_file.resize(size)  # Change the size of the img
    photo = ImageTk.PhotoImage(photo_file)
    photo_preview = Label(photoframe, image=photo, bg = "maroon3")
    photo_preview.image = photo
    photo_preview.grid(row=0, column=0)


def quit_app(event):
    root.destroy()


def menu_operation():
    list = ['Rotate', 'Mirror', 'Resize', 'Edge', 'convert_grayscale']      # Insert the function list to the ListBox
    for item in list:
        list_op.insert("end", item)

def get_threshold():
    threshold_label.grid(row=9, column=0)           # Show the threshold
    threshold_entry.grid(row=9, column=1)
    threshold_button.grid(row=10, column=1)


def threshold(event):       # Function for Threshold Preview
    global threshold
    threshold = int(threshold_entry.get())
    img = edge(first_photo_path, "", threshold)
    op_preview(img)


def get_op(event):      # Function that check which operation is active and call the function for preview
    op = list_op.get("active")
    if op == "Rotate":
        try:
            img = rotate_picture(first_photo_path, "")
            op_preview(img)
        except:
            messagebox.showerror("Error","Please select a filter first")
    if op == "Mirror":
        img = mirror_picture(first_photo_path, "")
        op_preview(img)
    if op == "Resize":
        img = resize_picture(first_photo_path, "")
        op_preview(img)
    if op == "Edge":
        get_threshold()
    try:
        if op == "convert_grayscale":
            img = convert_grayscale(first_photo_path, "")
            op_preview(img)
    except:
        messagebox.showerror("Error", "The Image is not editable")


def op_preview(img):
    demnsion = img.size  # get the demnsion
    height = demnsion[0]
    width = demnsion[1]  # Calculate the img size to 372x210
    new_height = (372 / float(height)) * float(height)
    new_width = (210 / float(width)) * float(width)
    size = (int(new_height), int(new_width))
    img = img.resize(size)  # Change the size of the img
    photo = ImageTk.PhotoImage(img)
    photo_preview = Label(op_photo_frame, image=photo, bg = "maroon3")
    photo_preview.image = photo
    photo_preview.grid(row=0, column=0)


def save_browse(event):     # Function for Browse
    global save_path
    save_path_entry.delete(0, END)
    save_path = filedialog.askdirectory()
    save_path_entry.insert(0, save_path)


def save(event):    # the function that save the files
    try:
        for i in range (len(selected_files_list)):      # this for function get the each name from the selected files
            name_file= selected_files_list[i]
            save_name_file = selected_files_list[i][:-4]
            op = list_op.get("active")              # Check which op function choos and called the right function
            if op == "Rotate":
                rotate_picture(path +"/" + name_file, save_path + "/" + save_name_file + "rotate_process.gif")
            if op == "Mirror":
                mirror_picture(path +"/" + name_file, save_path + "/" + save_name_file + "mirror_process.gif")
            if op == "Resize":
                resize_picture(path +"/" + name_file, save_path + "/" + save_name_file + "resize_process.gif")
            if op == "Edge":
                edge(path +"/" + name_file, save_path + "/" + save_name_file + "edge_process.gif", threshold)
            if op == "convert_grayscale":
                convert_primary(path + "/" + name_file, save_path + "/" + save_name_file + "convert_grayscale_process.gif")
        messagebox.showinfo("Save Complete", "Your photos saved")
    except:
        messagebox.showerror("Error", "Please select a folder to save the files")


# Root continar

root = Tk()
root.title("InstHemo")
root.geometry("700x720")
photo = Image.open("back.jpeg")
back_photo = ImageTk.PhotoImage(photo)
root.configure(bg="maroon1")

intro = Label(root, text="Welcome to InstHemo",bg ="maroon2")

# choose area
choose_area = Frame(root, bg= "maroon1")


image_path_label = Label(choose_area, text="Please enter image path:", bg = "maroon1")
path_entry = Entry(choose_area, bg = "Plum2")
button_path_choose = Button(choose_area, text="Browse", bg= "maroon3")
list_img = Listbox(choose_area, selectmode=MULTIPLE, width=30, height=12, bg = "plum1")
button_path_choose.bind("<Button-1>", get_list)
list_img_label = Label(choose_area, text="Your image list:", bg = "maroon1")
choose_photos_button = Button(choose_area, text="Choose", background="maroon1")
choose_photos_button.bind("<Button-1>", get_name)
scroll_bar1 = Scrollbar(choose_area, orient=VERTICAL)
scroll_bar1.config(command=list_img.yview)


# threshold area
threshold_entry = Entry(choose_area, bg="Plum1")
threshold_button = Button(choose_area, text="ok")
threshold_label = Label(choose_area,text="Insert your threshold:",bg = "maroon1")
threshold_button.bind("<Button-1>", threshold)

# Operation command
pros_label = Label(choose_area, text="Process operation selection:", bg = "maroon1")
list_op = Listbox(choose_area, width=30, height=12, bg = "plum1")
preview_op_button = Button(choose_area, text="Preview")
preview_op_button.bind("<Button-1>", get_op)
scroll_bar2 = Scrollbar(choose_area)
scroll_bar2.config(command=list_op.yview)

# Save zone command
save_area = Frame(root, bg= "maroon1")
save_label = Label(save_area, text="Please choose save dirctory:", bg = "maroon1")
save_path_entry = Entry(save_area, bg="plum2" )
save_button = Button(save_area, text="Save")
browse_button = Button(save_area, text="Browse")
quitbutton = Button(save_area, text="Quit")
quitbutton.bind("<Button-1>", quit_app)
browse_button.bind("<Button-1>", save_browse)
save_button.bind("<Button-1>", save)

# photo zone
photoframe = Frame(choose_area, bg = "maroon1")
photo_canvas = Canvas(photoframe, height=253, width=400)
photo_canvas.create_rectangle(253, 400, 0, 0)
photoframe.grid(row=3, column=1, rowspan=2, columnspan=2, sticky=S)

# op photo

op_photo_frame = Frame(choose_area, bg = "maroon1")
op_photo_frame.grid(row=7, column=1, rowspan=2, columnspan=2, sticky=N)

# Grid

intro.grid(row=0)  # intro

choose_area.grid(row=1, column=0)
image_path_label.grid(row=0, column=0)  # image path
path_entry.grid(row=0, column=1)
button_path_choose.grid(row=0, column=2)
list_img_label.grid(row=3)
list_img.grid(row=4, column=0)  # listbox for img
choose_photos_button.grid(row=5)
scroll_bar1.grid(row=4, sticky=E, ipady=90)

pros_label.grid(row=6)  # Label
list_op.grid(row=7)
menu_operation()
preview_op_button.grid(row=8)
scroll_bar2.grid(row=7, sticky=E, ipady=90)

# save grid
save_area.grid(row=4)
save_label.grid(row=0, column=3)
save_path_entry.grid(row=1, column=3)
browse_button.grid(row=1, column=4)
save_button.grid(row=1, column=6)
quitbutton.grid(row=1, column=7)

root.mainloop()
