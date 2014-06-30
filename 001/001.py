### Known
    ### ALl natural numbers below 10 that are multiples of 3 or 5 are 3, 5, 6, 9.  The sum of these multiples is 23

### Unknown
    ### The sum of all multiples of 3 or 5 below 1,000
import cProfile
num_set = set()

def count(num,multi,end=1000):
    multi *= num
    while multi < end or end == None:
        yield multi
    yield

def num_loop(numbers):
    for num in numbers:
        for i in xrange(1,1000):
            c = count(num, i)
            if c.next() == None:
                break
            else:
                num_set.add(c.next())
    return sum(num_set)

print num_loop((3,5))
cProfile.run("num_loop((3,5))")