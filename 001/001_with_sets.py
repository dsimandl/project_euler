import cProfile

cProfile.run("sum(set(range(0,1000,3))|set(range(0,1000,5)))")

print sum(set(range(0,1000,3))|set(range(0,1000,5)))