import re 
def LongestWord(sen):
  sen = sen.split(" ")
  output = re.split("[ !&]",sen[0])[0]
  
  for i in range(len(sen)):
    new = re.split("[ !&:!]",sen[i])
    
    for k in new:
      if len(k) > len(output):
        output = k 
  
  
  # code goes here
  return output

# keep this function call here 
print(LongestWord(input()))