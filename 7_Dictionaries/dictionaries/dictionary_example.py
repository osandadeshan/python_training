class DictionaryExample:
    #keys and values
    my_dictionary = {"Osanda": 29, "Tom": 19, "David": 30}
    print(my_dictionary.get("Tom"))
    print(my_dictionary.items())
    print(my_dictionary.keys())

    print(my_dictionary.popitem())              #gets the last item of Dict & removes it
    print(my_dictionary)

    print(my_dictionary.setdefault("Tom"))