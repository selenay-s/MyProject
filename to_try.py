# Homework give a good name for: z,x,y,r,n,function

# this function take the name of a file (z) and return a random line of a file txt
# example 
# file.txt
# 1) ciao
# 2) hi
# 3) selam
# function(file.txt) -> hi or ciao or selam
def function(z):
  x = open(z, "r")
  y = x.readlines()
  r = len(y)
  # random line between 0 to max lines
  n = random.randint(0, r-1)
  return y[n]
