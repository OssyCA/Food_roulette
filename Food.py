from tkinter import *
import random
import time

food_app = Tk()
food_app.title("Food Generator")
food_app.geometry("300x400")  # Size of the window
food_app.configure(bg='grey')

# FOOD LISTS
food_list = [
    # 0
    ['Garlic Bread', 'Fries', 'Wings', 'Sallad'],
    # 1
    ['Tacos', 'Hamburger', 'Meat pie', 'Soup', 'Ham Pizza', 'Chicken Nuggets'],
    # 2
    ['Vego tacos', 'Halloumi Burger', 'Vegetables pie', 'Vegetables Soup', 'Vego Pizza'],
    # 3
    ['Wine', 'Beer', 'Water', 'Soda', 'Vodka', 'Juice'],
    # 4
    ['Cake', 'Cup cake', 'Chocolate', 'Ice Cream', 'Milkshake']
]
Custom = []

# Entry box, Output for food choosen and input for custom foods.
a = Entry(food_app, width=30, borderwidth=5)
a.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Different areas of program
frame = LabelFrame(food_app, text="FOOD TYPES", padx=10, pady=1, fg="red", bg="black")
full_c = LabelFrame(food_app, text="FULL MEAL", padx=10, pady=1, fg="red", bg="grey")

s_e = Entry(full_c, width=15, borderwidth=2)
s_e.grid(row=1, column=0, padx=10, pady=10)

m_e = Entry(full_c, width=15, borderwidth=2, )
m_e.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

d_e = Entry(full_c, width=15, borderwidth=2)
d_e.grid(row=5, column=0, columnspan=3, padx=10, pady=10)


# Give the random part in specific list.
def random_value(food_sort):
    if food_sort == 'normal'.lower():
        normal = (len(food_list[1])) - 1
        rd_n = random.randint(0, normal)
        return rd_n

    elif food_sort == 'vego':
        vego = (len(food_list[2])) - 1
        rd_v = random.randint(0, vego)
        return rd_v

    elif food_sort == 'drink':
        drinks = (len(food_list[3])) - 1
        rd_d = random.randint(0, drinks)
        return rd_d

    elif food_sort == 'dessert':
        desserts = (len(food_list[4])) - 1
        rd_dr = random.randint(0, desserts)
        return rd_dr

    elif food_sort == 'start':
        starts = (len(food_list[0])) - 1
        rd_s = random.randint(0, starts)
        return rd_s

    elif food_sort == 'custom':
        customs = (len(Custom)) - 1
        rd_c = random.randint(0, customs)
        return rd_c


def full_course():
    # Starter Text
    start = random_value('start')
    s_txt = food_list[0][start]

    # Main Text
    n_v = random.randint(1, 2)

    if n_v == 1:
        main = random_value('normal')
    else:
        main = random_value('vego')

    m_txt = food_list[n_v][main]

    # Dessert Text
    desserts = random_value('dessert')
    d_txt = food_list[4][desserts]

    # Starter Text
    s_e.delete(0, END)
    s_e.insert(0, s_txt)
    # Main Text
    m_e.delete(0, END)
    m_e.insert(0, m_txt)
    # Dessert Tex
    d_e.delete(0, END)
    d_e.insert(0, d_txt)


def add_to():
    food = a.get()
    a.delete(0, END)
    Custom.append(food)


def starters():
    pass


def nor_food():
    food = random_value('normal')
    current = food_list[1][food]
    a.delete(0, END)
    a.insert(0, current)


def vego_food():
    food = random_value('vego')
    current = food_list[2][food]
    a.delete(0, END)
    a.insert(0, current)


def drink():
    food = random_value('drink')
    current = food_list[3][food]
    a.delete(0, END)
    a.insert(0, current)


def dessert():
    food = random_value('dessert')
    current = food_list[4][food]
    a.delete(0, END)
    a.insert(0, current)


def custom():
    if not Custom:
        current = 'LIST IS EMPTY'
    else:
        food = random_value('custom')
        current = Custom[food]
    a.delete(0, END)
    a.insert(0, current)


# Buttons
normal_btn = Button(frame, text="FOOD    ", padx=6, pady=5, command=nor_food, fg="black", bg="red")
vego_btn = Button(frame, text="VEGO     ", padx=6, pady=5, command=vego_food, fg="black", bg="green")
drink_btn = Button(frame, text="DRINK    ", padx=5, pady=5, command=drink, fg="black", bg="blue")
dessert_btn = Button(frame, text="DESSERT", padx=5, pady=5, command=dessert, fg="black", bg="yellow")

custom_btn = Button(food_app, text="CUSTOM    ", padx=5, pady=5, command=custom, fg="blue", bg="grey")
add_btn = Button(food_app, text="ADD", padx=5, pady=5, command=add_to, fg="blue", bg="white")
full_c_btn = Button(food_app, text="FULL MEAL", padx=5, pady=5, command=full_course, fg="red", bg="grey")

# Placement:

# Buttons
normal_btn.grid(row=1, column=1, padx=10, pady=5)
vego_btn.grid(row=3, column=1, padx=10, pady=5)
drink_btn.grid(row=5, column=1, padx=10, pady=5)
dessert_btn.grid(row=7, column=1, padx=10, pady=5)

custom_btn.grid(row=12, column=0, pady=5)
full_c_btn.grid(row=10, column=0, pady=5)

add_btn.grid(row=0, column=3)

# Labels
starter_lbl = Label(full_c, text="STARTER:")
starter_lbl.grid(row=0, column=0)

main_lbl = Label(full_c, text="MAIN:")
main_lbl.grid(row=2, column=0)

dessert_lbl = Label(full_c, text="DESSERT:")
dessert_lbl.grid(row=4, column=0)

# Frames
full_c.grid(row=1, column=2, columnspan=3, sticky='N', padx=10, pady=10)
frame.grid(row=1, column=0, padx=10, pady=10)

# Running the program
food_app.mainloop()
