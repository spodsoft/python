
class sku:
    
    # Initialiser
    def __init__(self, code, quantity=0):
        self.code = code
        self.quantity = quantity
        
    def __str__(self):
        return f"{self.code}={self.quantity}"
        
    def __repr__(self):
        return f"<{self.__class__.__name__} code={self.code}, quantity={self.quantity}>"
    
    def onsale(self):
        return self.quantity > 0

onsale = lambda x: "Yes" if x.onsale() else "No"


# Main
if __name__ == "__main__":
    
    sku1 = sku("ab123")
    sku2 = sku("ab124",10)
    
    print("------------------")
    print(sku1)
    print(onsale(sku1))
    print(sku2)
    print(onsale(sku2))

    print (sku1.__repr__())
    print(dir(sku1))
    print(type(sku))
    print(type(5))

    
    # A simple decorator function
    def decorator(func):
    
        def wrapper():
            print("Before calling the function.")
            func()
            print("After calling the function.")
        return wrapper

    # Applying the decorator to a function
    @decorator

    def greet():
        print("Hello, World!")

    greet()
    
    