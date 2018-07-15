A string is a k-palindrome if it can be transformed into a palindrome by removing any amount of characters from 0 to k. Your task is to determine whether the given string s is a k-palindrome.

Example

For s = "abrarbra" and k = 1, the output should be
kpalindrome(s, k) = true.

You can remove one letter, 'r', to obtain the string "abrarba", which is a palindrome.

For s = "adbcdbacdb" and k = 2, the output should be
kpalindrome(s, k) = false.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string containing only lowercase English letters.

Guaranteed constraints:
3 ≤ s.length ≤ 100.

[input] integer k

Guaranteed constraints:
1 ≤ k ≤ 20.

[output] boolean

Return true if it is possible to delete at most k letters from a string s in order to make it palindrome. Return false otherwise.

[Python3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name
