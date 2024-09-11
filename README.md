# DevProjects
Welcome! This repository contains a collection of mini development projects across various technologies, not limited to Python. If you're interested in exploring larger projects or those focused on analytics and data science, feel free to check out my other repositories.
<br>
# Morse Code Training
<p> Overview: <p>A compact script that you can use to practice the main expressions in Morse code.<p>
Technologies Used: Google Colaboratory<p>
> <a href="https://github.com/bntmzu/PythonDevProjects/blob/555d2eadb6762fdcea80d38636817bbb1cd7cb2f/Morse_%D0%A1ode_Training.ipynb">Project link</a>
<br>
  
# Pomodoro Timer
**Overview:**  
<p>This project is a customizable Pomodoro Timer built with Python using the customtkinter library for modern UI design. The timer helps improve productivity by alternating between work and break intervals based on the Pomodoro technique.<p>
> <a href="https://github.com/bntmzu/MiniDevProjects/blob/main/Pomodoro.py">Project link</a>
<br>
  
**Features:** 
<p>Work intervals are set to 25 minutes by default, with short breaks of 5 minutes and long breaks of 20 minutes.<p>
The timer automatically starts and switches between work and break periods.<p>
A reset button is available to stop the timer and clear the progress.<p>
Displays a visual indication of completed work sessions with checkmarks.<p>
Modern UI with customizable color themes and button hover effects.<p>
Option to display an image for a personalized experience.<p>

**Technologies Used:**
<p>Python<p>
customtkinter for modern UI design.<p>
Pillow (PIL) for image manipulation and display.<p>

**How It Works:**
<p>Click the Start button to begin the Pomodoro session.<p>
The timer alternates between work and break periods, as indicated by the changing labels and colors.<p>
After each work session, a checkmark is displayed to track progress.<p>
The Reset button stops the current timer and resets the count.<p>

###  Product Catalog System

**Overview:**  
This project is a simple **Product Catalog System** implemented in Python. It is designed to manage different types of products, such as smartphones and lawn grass, by creating categories, adding products to these categories, and calculating statistics such as total price and average price. It also demonstrates concepts such as class inheritance, mixins, and abstract base classes.<p>
> <a href="https://github.com/bntmzu/MiniDevProjects/blob/main/Product_Catalog_System.py">Project link</a>
<br>


**Features:**

- **Product Management:**
  - Abstract base class `BaseProduct` defines common attributes and methods for all product types.
  - Two specific product types are implemented: `Smartphone` and `LawnGrass`.
  - Custom behavior for each product type using `__str__`, `__repr__`, and `__eq__` methods.

- **Category System:**
  - Products are organized into categories using the `Category` class.
  - Supports adding multiple products to a category.
  - Each category can calculate the total number of products and the total value of products.
  - Custom `__add__` method allows summing the total value of products in two categories.

- **Mixins and Inheritance:**
  - `InitPrintMixin` for printing class initialization details for debugging purposes.
  - Inheritance structure enables shared functionality while allowing for product-specific behaviors.


**Core Concepts:**

1. **Abstract Base Class (`ABC`):**
   - `BaseProduct` serves as the parent class for all product types and enforces the implementation of certain methods such as `__str__` and `new_product`.

2. **Inheritance and Customization:**
   - Both `Smartphone` and `LawnGrass` inherit from `BaseProduct` and extend its functionality by adding unique attributes (e.g., model, efficiency for `Smartphone` or germination period for `LawnGrass`).

3. **Operator Overloading:**
   - `__add__`: Allows adding products together based on their price and quantity.
   - `__eq__`: Ensures proper comparison between objects of the same class based on their attributes.

4. **Encapsulation:**
   - Products are stored in private attributes (`__products`) inside the `Category` class.
   - Encapsulated the logic for managing the product list inside getter and setter methods.

5. **Error Handling:**
   - Ensures proper validation of input values (e.g., non-negative prices and quantities).
   - Raises custom exceptions when invalid operations are attempted (e.g., adding non-product objects to a category).

**How It Works:**
- **Creating Products:**
  - You can create instances of products like `Smartphone` or `LawnGrass` by specifying their attributes such as name, price, quantity, and other specific properties.
  
- **Adding Products to Categories:**
  - Products are added to a `Category`, which manages the list of products and keeps track of the total product count.
  
- **Statistics:**
  - The system can compute the average price of products in a category.
  - You can calculate the total value of all products across categories by using the `__add__` method.


**Technologies Used:**

- **Python OOP**: Abstract classes, inheritance, mixins, property decorators, operator overloading.
- **Custom error handling** for invalid product data and operations.
- **Flexible design** to extend the system with additional product types if needed.

This project showcases a well-structured approach to building an extensible product catalog system using Python's object-oriented programming features.
