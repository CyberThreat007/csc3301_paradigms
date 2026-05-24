# global_scope_demo.py
# using the scope keyword to modify a global variable

counter = 0          # global variable

def increment():
    global counter  # declare that we want to use the global variable
    counter += 1    # modifies the global variable
increment()
increment()
print("Counter:", counter)

# ---------------- NOTES ----------------
# global keyword: tells Python that assignments refer to the module-level name.
# Use sparingly; prefer returning cleaner code.