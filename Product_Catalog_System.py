import warnings
from abc import ABC, abstractmethod

warnings.filterwarnings('ignore')

class InitPrintMixin:
    """Mixin for printing initialization details of a class."""
    def __init_print__(self, *args):
        class_name = self.__class__.__name__
        params = ', '.join([f"'{arg}'" if isinstance(arg, str) else str(arg) for arg in args])
        print(f"{class_name}({params})")

class BaseProduct(ABC):
    """
    Abstract base class for all product types.
    Defines basic properties like name, description, price, and quantity.
    Implements basic validation for quantity and price.
    """
    def __init__(self, name, description, price, quantity):
        if quantity <= 0:
            raise ValueError("A product with zero quantity cannot be added.")
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        super().__init__()

    @property
    def price(self):
        """Getter for price."""
        return self._price

    @price.setter
    def price(self, value):
        """Setter for price, ensures price is greater than 0."""
        if value <= 0:
            raise ValueError("Price must not be zero or negative.")
        self._price = value

    @abstractmethod
    def __str__(self):
        """Abstract method for string representation."""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, products):
        """Abstract method for creating a new product instance."""
        pass

    def __len__(self):
        """Returns the quantity of the product."""
        return self.quantity

    def __add__(self, other):
        """Overloads the + operator to sum the total cost of products."""
        if type(self) is type(other):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Addition error. Can only add instances of the same class.")

class Product(BaseProduct, InitPrintMixin):
    """Concrete implementation of BaseProduct with basic initialization and string representation."""
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.__init_print__(name, description, price, quantity)

    @classmethod
    def new_product(cls, products):
        """Creates a new product instance from a dictionary of product attributes."""
        return cls(**products)

    def __str__(self):
        """String representation of a product."""
        return f"{self.name}, {self.price} rub. Remaining: {self.quantity} pcs."

    def __repr__(self):
        """Representation of the product for debugging."""
        return f"Product('{self.name}', '{self.description}', {self.price}, {self.quantity})"

    def __eq__(self, other):
        """Equality check between two products."""
        if isinstance(other, Product):
            return (self.name == other.name and
                    self.description == other.description and
                    self.price == other.price and
                    self.quantity == other.quantity)
        return False

class Smartphone(Product):
    """Represents a smartphone with additional attributes like model, memory, and color."""
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    @classmethod
    def new_product(cls, products):
        """Creates a new smartphone instance from a dictionary of attributes."""
        return cls(**products)

    def __str__(self):
        """String representation of a smartphone."""
        return f"{self.name} {self.model}, {self.price} rub. Remaining: {self.quantity} pcs. (Color: {self.color}, Memory: {self.memory}GB, Efficiency: {self.efficiency})"

    def __repr__(self):
        """Representation of the smartphone for debugging."""
        return f"Smartphone('{self.name}', '{self.description}', {self.price}, {self.quantity}, '{self.efficiency}', '{self.model}', {self.memory}, '{self.color}')"

    def __eq__(self, other):
        """Equality check between two smartphones."""
        if isinstance(other, Smartphone):
            return (super().__eq__(other) and
                    self.efficiency == other.efficiency and
                    self.model == other.model and
                    self.memory == other.memory and
                    self.color == other.color)
        return False

class LawnGrass(Product):
    """Represents lawn grass with attributes like country of origin, germination period, and color."""
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    @classmethod
    def new_product(cls, products):
        """Creates a new lawn grass instance from a dictionary of attributes."""
        return cls(**products)

    def __str__(self):
        """String representation of lawn grass."""
        return f"{self.name}, {self.price} rub. Remaining: {self.quantity} pcs. (Color: {self.color}, Country: {self.country}, Germination Period: {self.germination_period} days)"

    def __repr__(self):
        """Representation of the lawn grass for debugging."""
        return f"LawnGrass('{self.name}', '{self.description}', {self.price}, {self.quantity}, '{self.country}', {self.germination_period}, '{self.color}')"

    def __eq__(self, other):
        """Equality check between two lawn grass products."""
        if isinstance(other, LawnGrass):
            return (super().__eq__(other) and
                    self.country == other.country and
                    self.germination_period == other.germination_period and
                    self.color == other.color)
        return False

class Category:
    """
    Represents a category of products. Each category can hold multiple products and provides methods to
    add products, calculate the total number of products, and compute the average price of products.
    """
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        """Initializes the category with a name, description, and an optional list of products."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += sum(p.quantity for p in self.__products)

    def add_product(self, product):
        """Adds a product to the category and updates the total product count."""
        if isinstance(product, BaseProduct):
            self.__products.append(product)
            Category.product_count += product.quantity
        else:
            raise TypeError("You can only add objects of type Product or its subclasses (Smartphone/LawnGrass).")

    @property
    def products(self):
        """Returns a formatted string of all products in the category."""
        products = [str(product) for product in self.__products]
        return "\n".join(products) + "\n"

    @products.setter
    def products(self, value):
        """Setter to add a list of products to the category."""
        if isinstance(value, list):
            if all(isinstance(product, BaseProduct) for product in value):
                self.__products = value
            else:
                raise TypeError("You can only add objects of type Product or its subclasses (Smartphone/LawnGrass).")
        elif isinstance(value, BaseProduct):
            self.__products.append(value)
        else:
            raise TypeError("You can only add objects of type Product or its subclasses (Smartphone/LawnGrass).")

    def __str__(self):
        """String representation of the category."""
        total_products_count = sum([p.quantity for p in self.__products])
        return f"{self.name}, total products: {total_products_count} pcs."

    def __add__(self, other):
        """Overloads the + operator to calculate the total cost of all products in two categories."""
        if isinstance(other, Category):
            total_cost = sum(product.price * product.quantity for product in self.__products)
            total_cost += sum(product.price * product.quantity for product in other.__products)
            return total_cost
        raise TypeError("Addition error. Can only add instances of Category.")

    def get_result(self):
        """Returns the list of products in the category."""
        return self.products

    def middle_price(self):
        """Calculates the average price of products in the category."""
        try:
            total_products_count = len(self.__products)
            total_price = sum([float(prod.price) for prod in self.__products])
            return total_price / total_products_count
        except ZeroDivisionError:
            return 0
