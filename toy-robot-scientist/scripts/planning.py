# Import the necessary packages
import os

# Import custom modules
from .equipment import list_of_equipment
from .materials import list_of_material
from .experimental_protocol import generate_protocol

# Create the path to the hypotheses data file 
scriptDir = os.path.dirname(__file__)
dataPathHypFile = "../output/hypotheses.txt"
hypDataPath = os.path.join(scriptDir, dataPathHypFile)

# Function for the planning agent
def planning():
  # Check if there are no hypotheses (empty hypotheses file)
  if os.stat(hypDataPath).st_size == 0:
    print("There are no valid hypotheses. \nUse the reasoning agent to generate some first.","\n")
    # Pause the function to go back to the main menu if no hypotheses    
    input("------------PRESS ENTER FOR THE MAIN MENU------------")
    return
  
  # --------------------------------Begin planning---------------------------------
  
  # Retrieve hypotheses from file
  with open(hypDataPath) as f:
    hypotheses = list(open(hypDataPath))
  
  # Remove the 'new_line \n' character for each hypotheses  
  hypotheses_list = [hyp[:-1] for hyp in hypotheses]
  
  # Print hypotheses from the file
  print("Hypotheses to test:\n")
  for index, hyp in enumerate (hypotheses_list):
    print("likely drug ("+hyp+")"+"\n")
  
  # Pause the function for the next planning step  
  input("------------PRESS ENTER FOR THE NEXT PLANNING STEP------------\n")
  
  # Translate given hypotheses to testable hypotheses
  print("Testable hypotheses:\n")
  for index, hyp in enumerate (hypotheses_list):
    print("measure_potency ("+ hyp+", high)"+"\n")
  print("Add positive control:")
  print("   measure_potency (Morphine, high)\n")

  # Pause the function for the next planning step  
  input("------------PRESS ENTER FOR THE NEXT PLANNING STEP------------\n")
  
  # Check for available equipment to measure potency
  equipment_available = False

  for index, equipment in enumerate (list_of_equipment()):
    if equipment[1] == "measure_potency":
      equipment_available = True
  
  print("Checking if there is a piece of equipment that can measure potency:\n")

  if(equipment_available):
    print("Equipment to measure potency available\n")
    # Pause the function for the next planning step  
    input("------------PRESS ENTER FOR THE NEXT PLANNING STEP------------\n")
  else:
    print("Equipment to measure potency not available\n")
    # Pause the function to go back to the main menu    
    input("------------PRESS ENTER FOR THE MAIN MENU------------")
    return

  # Check if chemicals are available in the list of materials
  print("Checking if the chemicals are available in the list of materials:\n")
  
  # Convert lists to set
  set_chemicals = set(hypotheses_list)
  set_materials = set(list_of_material())
  # Check if chemicals are in the set of materials
  if(set_chemicals.issubset(set_materials)):
    print("Yes, proceed with generation of protocol\n")
    # Pause the function for the next planning step  
    input("------------PRESS ENTER FOR THE NEXT PLANNING STEP------------\n")
  else:
    print("No, protocol generation rejected\n")
    # Pause the function to go back to the main menu    
    input("------------PRESS ENTER FOR THE MAIN MENU------------")
    return

  # Takes a standard protocol from a knowledge base and adds the required number of chemicals 
  # following the recommended plate design. N = 5
  print("Standard protocol:\n\n")
  print("add(ch, plate)\n")
  print("move(plate, incubator)\n\n")
  print("loop N times:\n")
  print("   grow(plate, 20 min)\n")
  print("   move(plate, reader)\n")
  print("   measure_potency (ch, reader)\n\n")
  print("discharge(plate, trash)\n\n")
  print("Input standard protocol for measuring potency from the knowledge base\n")
  print("Instantiate the protocol for the given hypotheses and default number of iterations: N=5\n")
  
  # Pause the function for the next planning step  
  input("------------PRESS ENTER FOR THE NEXT PLANNING STEP------------\n")

  print("Experimental protocol generation...\n")
  # Generate and print the protocol to a file
  # /output/protocol.txt
  # chemicals -> number of iterations (n = 5)
  generate_protocol(hypotheses_list, 5)

  # Pause the function to go back to the main menu    
  input("------------PRESS ENTER FOR THE MAIN MENU------------")
