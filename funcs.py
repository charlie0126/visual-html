from tkinter.filedialog import askopenfilename
from tkinter.font import Font, BOLD, ITALIC
from tkinter.simpledialog import askstring, Label, askinteger
from tkinter import *
import functools



def ask_infos():
    filename = askopenfilename()
    titlename = askstring("Title", "Please enter the title of this html.")
    return filename, titlename


file, title = ask_infos()
level = 1
showing_x = 210
showing_y = 20
bold_font = Font(size=20, weight=BOLD)
italic_font = Font(size=20, slant=ITALIC)
title_font = Font(size=30, weight=BOLD)
current_y = 30
category = 1
std_x = 10
dot = False
order = False
listitem = False
order_num = 1
root = Tk()
RootBtn = functools.partial(Button, master=root)
canvas = Canvas(root, height=600, width=600)
canvas.pack()



# Define functions that write into html files (and supporting functions)
def get_new_y():
    global current_y
    current_y += 30
    return (current_y - 30)+30*(category-1)


def htmlstr(string):
    return string.replace(" ", "&nbsp;").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("™",
                                                                                                                 "&reg;").replace(
        "\"", "&quot;").replace("'", "&apos;")


def lb_write(text, *, font=None):
    global order
    if font is None:
        if dot and listitem:
            label = Label(root, text="•"+text) # • is Alt+8
        elif order and listitem:
            label = Label(root, text=str(order)+"."+text)
        else:
            label = Label(root, text=text)
    else:
        if dot and listitem:
            label = Label(root, text="•"+text, font=font)
        elif order and listitem:
            label = Label(root, text=str(order)+"."+text, font=font)
            order += 1
        else:
            label = Label(root, text=text, font=font)
    label.place(x=showing_x, y=showing_y)


def tab_level():
    return "\t" * level


def std_start():
    with open(file, "w") as f:
        f.write("""<!--This file is created by Visual Html-->
<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>%s</title>
</head>
<body>""" % title)


def write_in_file(stuff):
    with open(file, "a") as f:
        f.write("\n" + tab_level() + stuff)


def text_title(ttl, title_size):
    write_in_file("<h%i>%s</h%i>" % (title_size, htmlstr(ttl),
                                     title_size))


def separate_line():
    write_in_file("<hr>")


def italic_text(text):
    write_in_file("<i>%s</i>" % htmlstr(text))


def bold_text(text):
    write_in_file("<b>%s</b>" % htmlstr(text))


def change_line():
    write_in_file("<br>")


def start_paragraph():
    global level
    level += 1
    write_in_file("<p>")


def end_paragraph():
    global level
    level -= 1
    write_in_file("</p>")


def pure_text(text: str):
    write_in_file(text)


def std_end():
    write_in_file("</body>")


def super_link(text, url):
    write_in_file("<a href=\"%s\">%s</a>" % (url, htmlstr(text)))


def start_dot_list():
    global level, dot
    write_in_file("<ul>")
    level += 1
    dot = True


def end_dot_list():
    global level, dot
    write_in_file("</ul>")
    level -= 1
    dot = False


def start_list_item():
    global level, listitem
    write_in_file("<li>")
    level += 1
    listitem = True


def end_list_item():
    global level, listitem
    write_in_file("</li>")
    level -= 1
    listitem = False


def start_ordered_list():
    global level
    write_in_file("<ol>")
    level += 1


def end_ordered_list():
    global level
    write_in_file("</ol>")
    level -= 1


# Handlers for button clicking
def click_text_title():
    global showing_x
    this_text_title = askstring("Text Title", "Enter the text title:")
    size = askinteger("Size", "Enter the size of this title (1 big-6 small")
    text_title(this_text_title, size)
    lb_write(this_text_title, font=title_font)
    showing_x += len(this_text_title) * 7


def click_separate_line():
    global showing_y, showing_x
    separate_line()
    showing_y += 20
    showing_x = 210
    canvas.create_line(showing_x, showing_y, showing_x + 200, showing_y)


def click_italic_text():
    global showing_x
    text = askstring("Enter", "Enter oblique text:")
    italic_text(text)
    lb_write(text, font=italic_font)
    showing_x += len(text) * 5


def click_bold_text():
    global showing_x
    text = askstring("Enter", "Enter bold text:")
    bold_text(text)
    lb_write(text)
    showing_x += len(text) * 5


def click_change_line():
    global showing_y, showing_x
    change_line()
    showing_y += 20
    showing_x = 210


def click_start_paragraph():
    global showing_y
    start_paragraph()
    showing_y += 15


def click_end_paragraph():
    global showing_y
    end_paragraph()
    showing_y += 15


def click_pure_text():
    global showing_x
    text = askstring("Enter", "Enter pure text:")
    pure_text(text)
    lb_write(text)
    showing_x += len(text) * 5


def click_end_html():
    std_end()
    exit(0)


def click_start_dot_list():
    global level, dot
    start_dot_list()
    level += 1
    dot = True


def click_end_dot_list():
    global level, dot
    end_dot_list()
    level -= 1
    dot = False


def click_super_link():
    global showing_x
    url = askstring("Url", "Enter the url that this link links to:")
    text = askstring("Enter", "Enter text that can be seen by users:")
    super_link(text, url)
    lb_write(text)
    showing_x += len(text) * 5


def click_start_list_item():
    global level
    start_list_item()
    level += 1


def click_end_list_item():
    global level
    end_list_item()
    level -= 1


def click_start_ordered_list():
    global level, order
    start_ordered_list()
    level += 1
    order = True


def click_end_ordered_list():
    global level, order
    end_ordered_list()
    level -= 1
    order = False
