#Functions with outputs

def format_name(f_name,l_name):
    fcap = f_name.capitalize()
    lcap = l_name.capitalize()

    return fcap + " " + lcap

fstring = input("first name: ")
lstring = input("last name: ")

output = format_name(f_name=fstring,l_name=lstring)
print(output)