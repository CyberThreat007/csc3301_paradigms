# nonlocal_scope_demo.py
# Demonstarting nonlocal and closure

def make_counter():
    counter = 0 # enclosed variable

    def increment():
        nonlocal counter # declare that we want to use the enclosed variable
        counter += 1  # modifies the enclosed variable

    return increment
count = make_counter() 
count() # counter is now 1
count() 
count() # counter is now 2
print("counter:", count.__closure__[0].cell_contents) # Accessing the enclosed variables))


# ---------------- NOTES ----------------
# nonlocal: allows inner function to rebind a variable from enclosing (non-global) scope.
# Closures: A function that retains access to its enclosing scope even after the outer function has finished executing.
# In this example, make_counter creates a closure that retains access to the counter variable, allowing increment to modify it across multiple calls.   

