
try_smth_with_it = ()
that_is_tuple_list = [(), (1, 2, 3, 4, "smth", 5, "nothing")]

def test_(*test_args):
    simple = False
    if not test_args:
       return 0
    elif type(test_args) == list or type(test_args) == dict or type(test_args) == tuple or type(test_args) ==  set or type(test_args) == bool:
        simple = False
        return simple
    elif type(test_args) == int or type(test_args) == str or type(test_args) == float:
        simple = True
        return simple


def testing(*args):
    if test_(args) == True:
        return args
    if test_(args) == False:
        for i in args:
            