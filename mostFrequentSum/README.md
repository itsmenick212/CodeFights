The sum of a subtree is the sum of all the node values in that subtree, including its root.

Given a binary tree of integers, find the most frequent sum (or sums) of its subtrees.

Example

For
t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": null
    },
    "right": {
        "value": 3,
        "left": null,
        "right": null
    }
}
the output should be
mostFrequentSum(t) = [2, 3, 6].
1st example

Since all the sum values in this tree occur only once, return all of them in ascending order.

For
t = {
    "value": -2,
    "left": {
        "value": -3,
        "left": null,
        "right": null
    },
    "right": {
        "value": 2,
        "left": null,
        "right": null
    }
}
the output should be
mostFrequentSum(t) = [-3].
2nd example

There are 3 subtree sums for this tree: -2 + (-3) + 2 = -3, -3, and -2. The most frequent sum is -3 since it appears twice.

Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t

A tree of integers.

Guaranteed constraints:
0 ≤ tree size ≤ 105,
-20000 ≤ node value ≤ 20000.

[output] array.integer

The most frequent subtree sum. If there are several such sums, return them sorted in ascending order.
[Python3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name
