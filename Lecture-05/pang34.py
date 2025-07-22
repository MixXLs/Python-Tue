global_variable = "I'm outside the function"

def my_function():
    local_variable = "I'm inside the function"
    print(local_variable)
    
print(global_variable)
my_function()
print(global_variable)
