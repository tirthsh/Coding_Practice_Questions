class MaxStack:
  def __init__(self):
    self.stack = []
    self.max_stack = []
    self.size = 0

  def push(self, val):
    self.stack.append(val)
    self.size += 1

    #update max stack
    if len(self.max_stack) == 0:
      self.max_stack.append({val: 1})
    else:
      max_val = self.max()
      max_count = self.max_stack[-1][max_val]

      if val > max_val:
        self.max_stack.append({val:1})
      elif val == max_val:
        self.max_stack[-1] = {val: max_count + 1}
    
  def pop(self):
    if self.size == 0:
      raise IndexError("pop from empty list")
    
    pop_val = self.stack[-1]
    self.stack = self.stack[:-1]

    max_val = self.max()
    max_count = self.max_stack[-1][max_val]

    if pop_val == max_val:
      if max_count == 1:
        self.max_stack = self.max_stack[:-1]
      else:
        self.max_stack[-1] = {pop_val: max_count - 1}

  def max(self):
    # Fill this in.
    max_num = list(self.max_stack[-1].keys())[0]

    return max_num

  def __str__(self):
    return "Stack: " + str(self.stack) + ", Max Stack " + str(self.max_stack)
    
max_stack = MaxStack()
max_stack.push(1)
max_stack.push(2)
max_stack.push(2)
max_stack.push(0)
print(max_stack)

max_stack.pop()
print(max_stack)

max_stack.pop()
print(max_stack)

print(max_stack.max())

max_stack.pop()
print(max_stack)

max_stack.push(1)
max_stack.push(1)
print(max_stack)

print(max_stack.max())


