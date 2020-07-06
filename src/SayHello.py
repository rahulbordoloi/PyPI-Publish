class SayHello:
    
    def __init__(self):
        self.name = None
    
    def say_hello(self, name = None):
        if self.name is None:
            return "Hello R-07!"
        else:
            return f"Hello, {self.name}!"