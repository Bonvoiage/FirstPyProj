h = "tittle"
d = "duration"
t = "time_now"
a = "adult_mode"    

h2 = "tittle2"
d2 = "duration2"
t2 = "time_now2"
a2 = "adult_mode2"

lf = {}
lf[h] = d, t, a
lf[h2] = d2, t2, a2
# print(lf)

print(*lf.values())
print(*lf.keys())

for key, value in lf.items():
    print(key, *value)