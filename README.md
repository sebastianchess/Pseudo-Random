## Things To Fix 
The code works pretty much with wide ranges, by the repo's name already tells we are referring to Pseudo-Random numbers. It fails to generate variety, random numbers within a low range tend to be repetitive, and this is what stops me from finishing up the `choices` function. I mean I have tried :)


### random_copy.py
```py
# The whole implementation

def choices[T](x: Sequence[T]) -> T:
    return x[randrange(0, len(x))] 
```
### main.py
```py
from random_copy import choices

names = ["Tim", "James", "Nick"]
print(choices(names)) 
```
Notice how it fixates on "Nick" (And I insanely dislike this), it seems the most likely random number from the range `[0, 3]` is `2`. 

### HOWEVER
```py
for _ in range(10):
    print(choices(names))
```
In this case there's variety and I presume it has to do with the effect time has on the program.
