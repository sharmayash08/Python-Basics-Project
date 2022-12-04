def get_acronym(the_string):
    words = the_string.split(" ")
    return_string = ""
    for i in words:
        return_string += i[0]
    return return_string.upper()

Phrases = ['computer science engineering','geeks for geeks','best friend forever','to be honest']
for a in Phrases:
    print("The acronym is: " + get_acronym(a))
