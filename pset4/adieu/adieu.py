# import module
import inflect

p = inflect.engine()

# tracking name
name_list = ()

while True:
    # input
    try:
        name_list += (input("Name: "),)
    # print
    except EOFError:
        print("Adieu, adieu, to", p.join(name_list))
        break
