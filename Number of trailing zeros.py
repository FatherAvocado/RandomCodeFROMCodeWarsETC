#Write a program that will calculate the number
# of trailing zeros in a factorial of a given number.

#N! = 1 * 2 * 3 * ... * N

#Be careful 1000! has 2568 digits...
#My solution
import math
def zeros(n):
    if n > 0:
        accum = 1
        #for multiplier in range(1, n + 1):
           # accum = accum * multiplier
         #   print(accum)

        accumstr = str(math.factorial(n))
        zerocount = 0
        for numzeros in accumstr[::-1]:
            if numzeros == "0":
                zerocount += 1
            else:
                break
        return zerocount
    elif n == 0:
        return 0
#Other Solution

# """ No factorial is going to have fewer zeros than the factorial of a smallernumber.

    #Each multiple of 5 adds a 0, so first we count how many multiples of 5 are
    #smaller than `n` (`n // 5`).

   # Each multiple of 25 adds two 0's, so next we add another 0 for each multiple
    #of 25 smaller than n.

  #  We continue on for all powers of 5 smaller than (or equal to) n.
   # """
   # pow_of_5 = 5
   # zeros = 0

   # while n >= pow_of_5:
   #     zeros += n // pow_of_5
   #     pow_of_5 *= 5
   #
   # return zeros



print(zeros(6))



