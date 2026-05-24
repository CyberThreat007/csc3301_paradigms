# Demontrating Local and Global Scope

x = 10 # Global variable
def show_value():
    x = 5 # Local variable
    print("Inside function:", x)

show_value()
print("Outside function:", x)

# ---------------- NOTES ----------------
#Local Scope: A variable defined inside a function.
# - Exists only while the function runs.
# -Example: x = 5 inside show_value()
# 
# Global Scope: A variable defined outside all function.
# - Accessible from anywhere in the code.
# - Example: x = 10 at the top level.
# 
# Key exam point:
# - If a local variable has the same name as a global variable, 
#   Python uses the local vesion inside the function.


