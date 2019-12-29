how_is_python = "awesome."


def simple_func():
    how_is_python = "easy to learn."
    print("Inside func: Python is " + how_is_python)

print("""Outside - before function call: 
Python is """ + how_is_python)

simple_func()

print("""Outside - after function call: 
Python is """ + how_is_python)


def global_keyword_demo_func():
    global how_is_python
    how_is_python = "easy to learn."
    print("Inside func: Python is " + how_is_python)


global_keyword_demo_func()

print("""Outside func when global keyword is used:
Python is """ + how_is_python)

