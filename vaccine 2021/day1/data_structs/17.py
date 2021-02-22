# dict
# nesting 


dc = {'batman', 'wonder woman', 'aquaman', 'flash'}

avengers = {'iron man':'suit', 'captain':['shield', 'hammer'],
            'black widow':'energy', 'thor':'hammer', 'hulk':'smash'}

print(avengers)

superheroes = {'dc':dc, 'marvel':avengers}

print(superheroes)

print(superheroes['marvel'])

print(superheroes['marvel']['captain'])

#print(superheroes['marvel']['captain'])

print(superheroes['marvel']['captain'][1])

