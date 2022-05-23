# Import the necessary packages
import os
from tabulate import tabulate

# Create the path to the experimental results output file 
scriptDir = os.path.dirname(__file__)
outputPathFile = "../output/experimental_results.txt"
expResultsOutPath = os.path.join(scriptDir, outputPathFile)


# Function for the toy lab analysis
def results_analysis():
  # Check if there are no experimental results 
  if os.stat(expResultsOutPath).st_size == 0:
    print("There are no valid experimental results. \nUse the toy lab agent to generate them first.","\n")
    # Pause the function to go back to the main menu if no hypotheses    
    input("------------PRESS ENTER FOR THE MAIN MENU------------")
    return
  
  # Generate analysis results table
  print("Generating analysis results table from the experimental results...\n")
  
  # Experimental analysis from experimental results
  # Chemical and confirmation of drug
  analysis = [["Lidocaine", "Confirmed"],
             ["Curcumine", "Confirmed"],
             ["Tetrodotoxin", "Rejected"],
             ["6-Hydroxytrypargine",	"Rejected"],
             ["Morphine",	"Confirmed"]]
  
  # Construct analysis table
  table = tabulate(analysis,headers = ["Chemical", "is a drug?"],tablefmt='orgtbl')
  
  # Print the table
  print(table, '\n')

  # Pause the function to go back to the main menu    
  input("------------PRESS ENTER FOR THE MAIN MENU------------")