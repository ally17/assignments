txt = "I love apples, apple are my favorite fruit"
y = {}
for i in set(txt):
	a = txt.count(i)
	y[i] = a
print(y)