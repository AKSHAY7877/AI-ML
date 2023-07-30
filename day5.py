# import day5_pack.test as test
# test.hi()

# import day5_pack
# day5_pack.test.hi()
# day5_pack.xyz()

# from day5_pack import test
# test.hi()

# from day5_pack import xyz
# xyz()


values = input('Enter the values seperated by comma (,):')
values = [eval(i) for i in values.split(',')]

import day5_lib
print(day5_lib.multiplier(*values))      # we are breaking it down or usko open krke de rhe hai alg alg krke

from day5_lib import multiplier
print(multiplier(*values))

import day5_lib as d5
print(d5.multiplier(*values))

from day5_lib import multiplier as mt, data
print(multiplier(*values))
print(data*3)


#m