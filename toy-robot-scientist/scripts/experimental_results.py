# Import the necessary packages
import os

# Create the path to the experimental results output file 
scriptDir = os.path.dirname(__file__)
outputPathFile = "../output/experimental_results.txt"
resultOutPath = os.path.join(scriptDir, outputPathFile)

# Experimental results generation
def generate_experimental_results(results):
  # Open file 
  f = open(resultOutPath, "w")
  # Write experimental results to a file
  for result in results:
    for item in result:
      f.write(str(item) + ", ")
    f.write("\n")
  
  # close file 
  f.close()

  print("Successfully wrote experimental results to file at:\n")
  print(resultOutPath,'\n')