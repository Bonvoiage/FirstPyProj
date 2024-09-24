# print("hello, world") # ASCII
# print(ord("a")) # 97
# print(ord("A")) # 65

# just_test = "hello, world"
# chars = []
# for i in just_test:
#     ord_i = ord(i)
#     chars.append(ord_i)
# print(chars)

# re_just_test = ""
# for i in chars:
#     re_just_test += chr(i)
# print(re_just_test)


# for i in range(128):
#     print(f"{i} = {chr(i)}")

print(hex(ord("h"))) #0x68
bb = b"\x68"
print(type(bb))
print(bb.decode())