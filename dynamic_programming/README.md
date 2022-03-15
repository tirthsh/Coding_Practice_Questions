1. Which approach is better?

Any DP algorithm can be implemented with either method, and there are reasons for choosing either over the other. However, each method has one main advantage that stands out:

A bottom-up implementation's runtime is usually faster, as iteration does not have the overhead that recursion does.

A top-down implementation is usually much easier to write. This is because with recursion, the ordering of subproblems does not matter, whereas with tabulation, we need to go through a logical ordering of solving subproblems.


2. When to use DP?
The first characteristic that is common in DP problems is that the problem will ask for the optimum value (maximum or minimum) of something, or the number of ways there are to do something. For example:

What is the minimum cost of doing...
What is the maximum profit from...
How many ways are there to do...
What is the longest possible...
Is it possible to reach a certain point...

The second characteristic that is common in DP problems is that future "decisions" depend on earlier decisions. Deciding to do something at one step may affect the ability to do something in a later step. This characteristic is what makes a greedy algorithm invalid for a DP problem - we need to factor in results from previous decisions.