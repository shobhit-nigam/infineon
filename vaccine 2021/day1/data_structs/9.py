# lists
# nesting
# references and copy


dc_heroes = ['batman', 'wonder woman', 'aquaman']
dc = ['joker', 'gordon', dc_heroes]

avengers = ['iron man', 'captain', 'black widow', 'thor', 'hulk']
xmen = ['magneto', 'wolverine']

marvel = [avengers, xmen]

superheroes = [dc, marvel]

listc = [5, 43.2, "hi", "", [6, 7, 9]]

print("superheroes =", superheroes)

print("-----")
team = avengers.copy()

print("avengers = ",avengers)
print("team = ",team)

avengers.pop()
avengers.sort()
avengers.remove("captain")

print("avengers = ",avengers)
print("team = ",team)

print("-----")
print("superheroes =", superheroes)
