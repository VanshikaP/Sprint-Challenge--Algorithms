#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
<!-- a = 0 -- time complexity - O(1)
    while (a < n * n * n): -- time complexity - O(n^3 / n^2) since value of a is incremented in jumps of n^2
      a = a + n * n 
--> 
In the outer loop, the while loop has a time complexity of n^3, the inner statement increments the value of a in jumps of n^2, that means we are skipping n^2 iterations every time, thus we have to divide the outer runtime of n^3 by n^2 which results in overall runtime complexity of O(n)

b) O(nlog(n))
<!-- O(1) + O(n) * ( O(1) + O(logn) ) ~ O(nlog(n))
sum = 0 -- O(1)
    for i in range(n): -- O(n)
      j = 1 -- O(1)
      while j < n: -- run log(n) times since j is doubled every time
        j *= 2 -- O(1)
        sum += 1 -- O(1)
 -->
The outer loop runs n times in range of 0 to n. Inside the inner loop, we have another loop over j limited to n that doubles the value of it and hence has a runtime of log(n). The inner loop time gets multiplied by the outer loop hence the calculations lead to a time complexity of O(nlog(n))

c) O(bunnies)
<!-- O(bunnies)
def bunnyEars(bunnies):
      if bunnies == 0: -- base case
        return 0 -- time complexity - O(1)

      return 2 + bunnyEars(bunnies-1) -- gets called bunnies number of times untill we reach base case
 -->
The function gets called bunnies number of times since we are reducing the parameter by 1 until we reach the base case. This results in complexity of O(bunnies) or O(n) for simplification

## Exercise II
Understanding - 
    1. n story building
    2. k (assumed to be plenty) number of eggs
    3. Objective - to determine the value of f by dropping the eggs from each suspected floor such that number of broken eggs is minimized

Plan - 
    This building can be understood as an array of floor numbers that is sorted [0, 1, 2, 3 .... n]. We are required to find a specific value f in this array. The indication that egg is broken means that f is lower than the suspected value and if it is not broken , it means f is higher. 
    We are assuming that we have elevator available so that we can switch the floors easily in any order. Thus we have to find the value f in a sorted array of n values in minimum iterations. This translates to a binary search.

    Pseudocode - 
        1. get mid value between highest and lowest floor
        2. drop an egg from that floor
            a. if the egg is broken, limit the max value to that floor. and search again on the lower half of the building
            b. if egg is not broken, limit the starting point to that floor and search in the upper half of the building
            c. if we have only one floor left and egg is not broken, we have the value of f as that floor. If the egg is broken from that floor, we have the value of f as that floor - 1.
        3. The search will be repeated until we have only 1 floor in search and we reach a base case of c.

        Runtime complexity - The code is repeated log(n) times since we are reducing the value of n by half every time. Thus, the complexity is O(log(n)).

