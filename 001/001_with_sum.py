import cProfile

cProfile.run("sum([x for x in range(1,1000) if x % 3 == 0 or x % 5 == 0])")
print sum([x for x in range(1,1000000) if x % 3 == 0 or x % 5 == 0])