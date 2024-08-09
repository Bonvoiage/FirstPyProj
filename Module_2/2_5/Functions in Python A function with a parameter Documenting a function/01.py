# def say_hello(name):
#     print("Hello,", name)
# say_hello("Sam")
# say_hello("Max")
# say_hello("Den")

# import random
# def lottery():
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8]
#     winner = random.choice(tickets)
#     return winner
# winner = lottery()
# print(winner)

# import random
# def days(*args, **kwargs):
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8]
#     winner1 = random.choice(tickets)
#     tickets.remove(winner1)
#     winner2 = random.choice(tickets)
#     winner3 = random.choice(tickets)
#     print(*args)
#     return winner1, winner2
# winner1, winner2 = days(1, 2, 3, 4, 5, 6, 7)
# print(winner1, winner2)

def test(a=2, b=5):
     print(a, b)
# test()
# test(4, False)
# test([1, 2, 3], [12, 4, 6])
# test(*["no", "kod"])
# test(**{"a" : 12, "b" : 16})
