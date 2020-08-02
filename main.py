import pandas as pd

def getWeakness(data):
  # delete pass & WRITE YOUR CODE HERE 
  # HINT: Your code can be just one line!
  pass

def getStrength(data):
  # delete pass & WRITE YOUR CODE HERE 
  # HINT: Your code can be just one line!
  pass

def maxLevel(data):
  # delete pass & WRITE YOUR CODE HERE 
  # HINT: Your code can be just one line!
  pass
  
def meanStats(data):
  # delete pass & WRITE YOUR CODE HERE 
  # HINT: Your code can be just one line!
  pass

def main():
  # Read in the CSV file as a Data Frame and set it to variable 'data'
  data = pd.read_csv('player-data.csv')
  # Pass in Data Frame to all 4 functions
  solution1 = maxLevel(data)
  solution2 = getWeakness(data)
  solution3 = getStrength(data)
  solution4 = meanStats(data)
  
  # Write solution1-solution4 into another file called, 'answers.txt' to turn it in & get out of Jumanji!
  # Remember to close the file once you're done writing into it otherwise it will not be complete & we'll still be stuck!
  # HINT: Go back to File I/O Lesson to see how to write to a file & close
  # YOUR CODE HERE





if __name__ == '__main__':
  main()
