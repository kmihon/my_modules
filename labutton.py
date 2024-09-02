   
# модуль для создания кнопок из виджета label. 
# Кнопки реагируют на наведение мыши и нажатие.
# Можно привязать действие при нажатии
# кнопка остается нажатой пока не мудет нажата другая.
# Интерфейс построен на библиотеке CustomTkinter но можно реализовать на Tkinter
# для примера созданы виджеты label и помещены в список


import customtkinter as ctk

color_pressed = "#545252"
color_enter = "#727373"
color_leave = "#8b8d8d"

root = ctk.CTk()

# создаем лейблы которые будут имитировать кнопки
label = ctk.CTkLabel(root, width=200, height=50, fg_color=color_leave, text_color="yellow", text="")
label_1 = ctk.CTkLabel(root, width=200, height=50, fg_color=color_leave, text="one")
label_2 = ctk.CTkLabel(root, width=200, height=50, fg_color=color_leave, text="two")
label_3 = ctk.CTkLabel(root, width=200, height=50, fg_color=color_leave, text="tree")
label_4 = ctk.CTkLabel(root, width=200, height=50, fg_color=color_leave, text="four")
label_5 = ctk.CTkLabel(root, width=200, height=50, fg_color=color_leave, text="five")

label.pack()
label_1.pack()
label_2.pack()
label_3.pack()
label_4.pack()
label_5.pack()


list_labels = [label_1, 
               label_2, 
               label_3, 
               label_4, 
               label_5
               ]

def action_on_click(lbl):
    """ принимает лейбл из списка list_labels(кнопок)
        выводит текст нажаой кнопки в label
    """
    label.configure(text=list_labels[lbl]._text)


def bind_events(bind:bool):
    ''' создает события при нажатии ЛКМ'''
    if bind == True:
        for lbl in range(len(list_labels)):
            list_labels[lbl].bind("<ButtonPress-1>",  lambda e, l=[lbl]: pressing_a_buttons(e, l))
            list_labels[lbl].bind("<Enter>", lambda e, l=[lbl]: cursor_on_buttons(e, l)) 
            list_labels[lbl].bind("<Leave>", lambda e, l=[lbl]: cursor_outside_the_buttons(e, l))   
    else:
        return
    

def cursor_outside_the_buttons(event, lbl):
    ''' принимает список лейблов и изменияет цвет когда курсор вне ЛКМ '''
    for index in range(len(lbl)):
        number = lbl[index]
        if list_labels[number]._fg_color == color_pressed:
            list_labels[number].configure(fg_color=color_pressed)
        else:
            list_labels[number].configure(fg_color=color_leave)

def cursor_on_buttons(event, lbl):
    ''' принимает список лейблов и изменияет цвет когда курсор наведен на ЛКМ '''
    for index in range(len(lbl)):
        number = lbl[index]
        if list_labels[number]._fg_color == color_pressed:
            list_labels[number].configure(fg_color=color_pressed)
        else:
            list_labels[number].configure(fg_color=color_enter) 

def pressing_a_buttons(event, lbl):
    """ принимат список лейблов и изменяет цвет при нажати ЛКМ """
    for index in range(len(lbl)):
        number = lbl[index]
        for l in range(len(list_labels)): 
            if l == number:
                action_on_click(l) # принимает label из list_label цикла for/in
                list_labels[l].configure(fg_color=color_pressed)
                list_labels[l].configure(state="disabled")
            else:
                list_labels[l].configure(fg_color=color_leave)
                list_labels[l].configure(state="normal")

bind_events(True)

root.mainloop()
