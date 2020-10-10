#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is linear O(n) as the number of cycles increases at the same rate as the input n grows i.e. directly proportional.


b) This is Quadratic O(n^2) as it grows faster as n is increased due to the nested loops. i.e. 2 = 4 cycles, 3 = 9 cycles, 4 = 12 cycles.


c) bunnyEars will run once for each input above 0 therefore this is Linear O(n) as it grows in direct proportion.

## Exercise II

# n = building_stories
# if >= f, = break
# if < f, != break

I would approach this like a search algo, using binary search.
I would start with the highest floor and if the egg doesn't break, we can stop as we've found f.

If the egg does break from the highest point, given the number of stories n, I would then determine the mid point e.g. if 10 floors, I would start with floor 5 (assuming ground floor is 1 == lowest).
Depending if the egg breaks at floor 5, I would change the mid point accordingly.
i.e. if breaks, I know I need to go lower, if it doesn't break then I need to go higher and rule out the other half.

If the egg doesn't break, the new low would be mid + 1. 
e.g. 6 if started with n of 10. New mid point would be floor 8. I would try again from this floor.

If the egg does break at the new mid point, we know the new high would be mid - 1. 
e.g. if I just dropped from floor 8 and egg broke, I need a new mid point to drop from which would be 6.

I would repeat this until I found  where (f == break) and (f-1 != break), therefore determining the value of f which is the lowest floor the egg will break.

The time complexity is O(log n) as we can narrow it down based on binary search.
