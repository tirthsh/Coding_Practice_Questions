Complexity is always relevant to the size of the input. 
When talking about complexity in CS, we are essentially asking - as our input grows, how effiecient is our algorithm?

In terms of time, how fast is our computation performing given a very large input size. 

Quicksort, for example, sorts a billion items in 90 seconds on my laptop; Insertion Sort, on the other hand, needs 85 seconds for a million items; that would be 85 million seconds for a billion items – or in other words: two years and eight months!

In terms of space, how much extra space do we need, given a very large input size. 



Order of complexity (time):

O(1) -> constant complexity (i.e. accessing a value in a hash map / dictionary)

O(log n) -> logarthmic complexity (i.e. searching for a value via binary search tree (BST))

O(n) -> linear complexity (i.e. going through an array of size N)

O(n log n) -> loglinear complexity, implies that logn operations will occur n times(i.e. )

O(n²) -> quadratic complexity (i.e. for loop, going through a matrix)

2^n -> exponential complexity (i.e. fibanoci sequence / recursion )
