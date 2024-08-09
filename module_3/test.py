def test(*args):
    # print(args)
    # print(type(args))
    type(args)
    return type(args)



try_smth_with_it = ()
that_is_tuple_list = [(), (1, 2, 3, 4, "smth", 5, "nothing")]

# print(test(that_is_tuple_list))


# if type(that_is_tuple_list) == int:
#     print("sm")
# else:
#     print("doesnt work")
def test_element(*args):
    new_list = []
    for i in args:
        for j in i:
            if not j:
                print("rfnbhetncz rfr none")
                continue
            else:
                print("ne katiruet")
                continue

test_element(that_is_tuple_list)
# print("smth")

# if isinstance(that_is_tuple_list, tuple) == True:
#     print("that work with it")

# dict_ = {(2, 'Urban', ('Urban2', 35))}
# dict_2 = None
# def knowlage(*args):
#     for key, value in args.items():
#         print(key, value)

# print(type(dict_2))
# print(*dict_)
# # print(knowlage(dict))


# smth_net = [{(2, 'Urban', ('Urban2', 35))}]
# def smth_da(smth_net):
#     if type(smth_net) != int or type(smth_net) != str:
#         unlocked_args = (smth_net)
# print(smth_da(*smth_net))