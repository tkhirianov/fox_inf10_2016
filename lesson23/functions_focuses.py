def many_parameters_function(*arguments):
    for arg in arguments:
        print(arg, end='!!!\n')

many_parameters_function(1)
many_parameters_function(10, 20)
many_parameters_function(100, 200, 300)
many_parameters_function("AAAA", "BBB", "Hello")




def changing_global_name_link():
    global link
    print(link)
    link = "new line"
    print(link)

link = "old line"
print(link)
changing_global_name_link()
print(link)
