class sayHello:
    def __init__(self, target="World"):
        self.target = target
    
    def say(self):
        print(f"Hello, {self.target}!!")

if __name__ == '__main__':
    app = sayHello()
    app.say()
    app = sayHello("Someone")
    app.say()