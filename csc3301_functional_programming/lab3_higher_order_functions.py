   # Lab 3: Higher-Order Functions 

# Example: Function that takes in another function

def apply_twice(f, x):
    return f(f(x))

print("Apply twice:", apply_twice(lambda x: x + 1, 5))


# Example 2: Function return another function (Factory)

def make_adder(n):
    def adder(x):
        return x + n
    return adder

add5 = make_adder(5)
print("Add5", add5(10))

# Example 3: Custom repeat with Callbacks

def repeat(n, action):
    for i in range(n):
        action(i)

repeat(3, lambda i: print(f"step (i)"))