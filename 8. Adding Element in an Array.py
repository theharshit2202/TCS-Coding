def insertBegin(value, arr):
  """Inserts an element at the beginning of the array.

  Args:
      value: The element to insert.
      arr: The array to modify.

  Returns:
      A new list with the element inserted at the beginning.
  """
  return [value] + arr  # Efficiently create a new list with value prepended

def insertEnd(value, arr):
  """Inserts an element at the end of the array.

  Args:
      value: The element to insert.
      arr: The array to modify.

  Returns:
      A new list with the element inserted at the end.
  """
  return arr + [value]  # Efficiently create a new list with value appended

def insertMiddle(value, arr, location):
  """Inserts an element at a specific location in the array.

  Args:
      value: The element to insert.
      arr: The array to modify.
      location: The index where to insert the element (0-based).

  Returns:
      A new list with the element inserted at the specified location.
  """
  return arr[:location] + [value] + arr[location:]  # Efficient slicing

# Sample array
arr = [1, 2, 3, 4, 5, 6]

# Insert at beginning
new_arr = insertBegin(100, arr.copy())  # Use copy to avoid modifying original
print("Inserted at beginning:", new_arr)

# Insert at end
new_arr = insertEnd(200, arr.copy())
print("Inserted at end:", new_arr)

# Insert in middle
new_arr = insertMiddle(90, arr.copy(), 3)
print("Inserted in middle:", new_arr)
