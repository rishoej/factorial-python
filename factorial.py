def factorial(n):
  result = 1
  while(n >= 1):
    result = result * n
    n = n - 1
  return result

# Example 1: The number of combinations if you have 4 lego bricks and each of them have a difffent color yellow, blue, red and green.
# print factorial(4)

# Example 2: The number of combinations in standard card deck
# print factorial(52)
