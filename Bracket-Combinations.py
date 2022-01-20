def BracketCombinations(num):
  if num == 0:
    sum = 1
  fac = 1
  facn = 1
  facn1 = 1
  for i in range(1,(2*num+1)):
    fac *= i
    if i == num+1:
      facn = fac
    if i == num:
      facn1 = fac
    
    sum = int((fac / ((facn) * facn1)))
  # code goes here
  return sum

# num = input()
# keep this function call here 
print(BracketCombinations(int(input())))
