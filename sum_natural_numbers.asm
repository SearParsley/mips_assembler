.data
  n: 10
  result: 0
  stack_pointer: 500

.text
main:

  # Load arguments into registers
  lw R1, n
  lw R6, stack_pointer

  # Call the function
  jal sum_natural_numbers
  
  # Store the result in the result variable
  sw R2, result
  
  # Jump to the end of the program
  j end
  
sum_natural_numbers:
  # allocate stack
  addi R6, R6, -8
  sw R7, 4(R6)
  sw R3, 0(R6)

  # Recursive Case
  bne R1, R0, recursive_call
  
  # Base Case
  add R2, R0, R0
  add R1, R0, R0

  j return_sum

recursive_call:
  addi R1, R1, -1 # decrement n
  jal sum_natural_numbers
  add R3, R2, R0 # store result

  # add n to result
  add R2, R1, R3

return_sum:
  # restore stack
  lw R3, 0(R6)
  lw R7, 4(R6)
  addi R6, R6, 8-
  jr R7

end:
