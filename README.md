# Food Roulette Application Documentation

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Application Structure](#application-structure)
   - [Main Components](#main-components)
   - [Food Categories](#food-categories)
   - [User Interface](#user-interface)
4. [How to Use](#how-to-use)
   - [Random Food Selection](#random-food-selection)
   - [Full Meal Generation](#full-meal-generation)
   - [Custom Food Options](#custom-food-options)
5. [Technical Implementation](#technical-implementation)
   - [Random Selection Logic](#random-selection-logic)
   - [UI Components](#ui-components)
6. [Setup and Installation](#setup-and-installation)
   - [Prerequisites](#prerequisites)
   - [Running the Application](#running-the-application)
7. [Customization](#customization)
   - [Modifying Food Lists](#modifying-food-lists)
   - [UI Customization](#ui-customization)
8. [Troubleshooting](#troubleshooting)

## Overview

Food Roulette is a Python desktop application built with Tkinter that helps users decide what to eat by randomly generating food suggestions. Whether you're looking for a single dish, a drink, or planning a full course meal, this application can provide quick and random food ideas to help with decision-making.

## Features

- **Random Food Selection**: Generate random food suggestions from different categories (normal food, vego options, drinks, desserts)
- **Full Meal Generation**: Create a complete three-course meal with starter, main course, and dessert
- **Custom Food Options**: Add your own food items to a custom list and get random selections from them
- **User-Friendly Interface**: Simple and intuitive design with color-coded buttons for different food categories

## Application Structure

### Main Components

The application consists of a single Python file (`Food.py`) that contains all the necessary code for:
- The graphical user interface
- Food lists and categories
- Random selection logic
- Event handling for user interactions

### Food Categories

The application organizes food items into the following categories:

1. **Starters**: Appetizers like Garlic Bread, Fries, Wings, Salad
2. **Normal Food**: Main courses including Tacos, Hamburger, Meat pie, Soup, Ham Pizza, Chicken Nuggets
3. **Vego Food**: Vegetarian options like Vego tacos, Halloumi Burger, Vegetables pie, Vegetables Soup, Vego Pizza
4. **Drinks**: Beverage options including Wine, Beer, Water, Soda, Vodka, Juice
5. **Desserts**: Sweet options such as Cake, Cup cake, Chocolate, Ice Cream, Milkshake
6. **Custom**: User-added food items

### User Interface

The application window is divided into several sections:
- A main input/output text field at the top
- Food type buttons on the left side
- Full meal generation section on the right side
- Custom food controls at the bottom

## How to Use

### Random Food Selection

1. Click on one of the category buttons:
   - **FOOD**: Generate a random non-vegetarian main course
   - **VEGO**: Generate a random vegetarian main course
   - **DRINK**: Generate a random beverage
   - **DESSERT**: Generate a random dessert option

2. The randomly selected item will appear in the text field at the top of the application.

### Full Meal Generation

1. Click the **FULL MEAL** button to generate a complete three-course meal
2. The application will display:
   - A random starter
   - A random main course (either normal or vegetarian)
   - A random dessert

### Custom Food Options

1. Type a food item into the text field at the top
2. Click the **ADD** button to add it to your custom list
3. Click the **CUSTOM** button to get a random selection from your custom list
4. If your custom list is empty, you'll see "LIST IS EMPTY" when clicking the CUSTOM button

## Technical Implementation

### Random Selection Logic

The application uses Python's `random` module to generate random selections from the various food lists:

```python
def random_value(food_sort):
    if food_sort == 'normal'.lower():
        normal = (len(food_list[1])) - 1
        rd_n = random.randint(0, normal)
        return rd_n
    
    elif food_sort == 'vego':
        vego = (len(food_list[2])) - 1
        rd_v = random.randint(0, vego)
        return rd_v
    
    # Additional conditions for other food types...
```

The `full_course()` function combines random selections from different categories to create a complete meal:

```python
def full_course():
    # Starter Text
    start = random_value('start')
    s_txt = food_list[0][start]
    
    # Main Text (randomly chooses between normal and vego)
    n_v = random.randint(1, 2)
    if n_v == 1:
        main = random_value('normal')
    else:
        main = random_value('vego')
    m_txt = food_list[n_v][main]
    
    # Dessert Text
    desserts = random_value('dessert')
    d_txt = food_list[4][desserts]
    
    # Display results in the appropriate fields
    # ...
```

### UI Components

The application uses Tkinter widgets to create the user interface:
- `Tk`: Main application window
- `Entry`: Text fields for input and output
- `Button`: Interactive buttons for different functions
- `LabelFrame`: Containers for organizing related elements
- `Label`: Text labels for describing sections

## Setup and Installation

### Prerequisites

- Python 3.x installed on your system
- Tkinter library (usually comes bundled with Python)

### Running the Application

1. Save the code as `Food.py`
2. Open a terminal or command prompt
3. Navigate to the directory containing the file
4. Run the command: `python Food.py` (or `python3 Food.py` depending on your system)
5. The Food Roulette application window should appear

## Customization

### Modifying Food Lists

You can easily customize the available food options by editing the `food_list` variable in the code:

```python
food_list = [
    # 0 - Starters
    ['Garlic Bread', 'Fries', 'Wings', 'Sallad'],
    # 1 - Normal Food
    ['Tacos', 'Hamburger', 'Meat pie', 'Soup', 'Ham Pizza', 'Chicken Nuggets'],
    # 2 - Vego Food
    ['Vego tacos', 'Halloumi Burger', 'Vegetables pie', 'Vegetables Soup', 'Vego Pizza'],
    # 3 - Drinks
    ['Wine', 'Beer', 'Water', 'Soda', 'Vodka', 'Juice'],
    # 4 - Desserts
    ['Cake', 'Cup cake', 'Chocolate', 'Ice Cream', 'Milkshake']
]
```

Add or remove items from each sublist to customize the options for each category.

### UI Customization

You can modify several aspects of the user interface:
- Window size: Change the `food_app.geometry("300x400")` parameter
- Colors: Modify the `bg`, `fg` parameters in various widget definitions
- Button sizes: Adjust the `padx` and `pady` parameters
- Text: Modify button labels and section titles

## Troubleshooting

### Common Issues and Solutions

1. **Application doesn't start**
   - Ensure Python is correctly installed
   - Verify that Tkinter is available (try `import tkinter` in a Python interpreter)
   - Check for syntax errors in the code

2. **Custom list not working**
   - Make sure you're clicking the ADD button after typing your custom food item
   - The custom list starts empty and needs items added during each session

3. **UI display issues**
   - If elements appear misaligned or missing, check your screen resolution
   - The application uses a fixed window size that may not display correctly on all screens

4. **Random selection seems repetitive**
   - The application uses true randomness, so repetitions can naturally occur
   - Adding more items to the food lists will increase variety
