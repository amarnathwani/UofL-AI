# Import the necessary packages
import os
from tabulate import tabulate

# Import custom modules
from .experimental_results import generate_experimental_results


# Create the path to the protocol output file 
scriptDir = os.path.dirname(__file__)
outputPathFile = "../output/protocol.txt"
protocolOutPath = os.path.join(scriptDir, outputPathFile)

# Function for the toy lab agent
def experimental_results():
  # Check if there is no protocol (empty protocol file)
  if os.stat(protocolOutPath).st_size == 0:
    print("There is no valid protocol. \nUse the planning agent to generate it first.","\n")
    # Pause the function to go back to the main menu if no hypotheses    
    input("------------PRESS ENTER FOR THE MAIN MENU------------")
    return
  
  # Generate experimental results table
  print("Generating experimental results table from the protocol...\n")
  print("This table contains the chemicals and their potency values:\n")
  
  # Experimental results from protocol
  # Chemical and list of potency values
  results = [["Lidocaine",	0.8,	0.8,	0.75,	0.76,	0.82,	0.78,	0.8, 0.8,	0.82,	0.81,	0.8,	0.82,	0.85,	0.85,	0.86],
             ["Curcumine",	0.7,	0.72,	0.7,	0.71,	0.73,	0.75,	0.76,	0.71,	0.72,	0.71,	0.75,	0.79,	0.78,	0.8, 0.79],
             ["Tetrodotoxin", 0.2,	0.2,	0.2,	0.19,	0.2,	0.21,	0.23,	0.2,	0.19,	0.15,	0.14,	0.16,	0.14,	0.14,	0.15],
             ["6-Hydroxytrypargine",	0.2,	0.18,	0.2,	0.19,	0.18,	0.21,	0.23,	0.2,	0.19,	0.15,	0.15,	0.16,	0.14,	0.14,	0.15],
             ["Morphine",	0.73,	0.72,	0.75,	0.71,	0.73,	0.76,	0.76,	0.71,	0.72,	0.76,	0.75,	0.79,	0.78,	0.8,	0.81]]
  
  # Construct results table
  table = tabulate(results,tablefmt='orgtbl')
  
  # Print the table
  print(table, '\n')
  
  # Write results to file
  # /output/experimental_results.txt
  generate_experimental_results(results)

  # Pause the function to go back to the main menu    
  input("------------PRESS ENTER FOR THE MAIN MENU------------")