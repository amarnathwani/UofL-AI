# Import the necessary packages
import os

# Create the path to the protocol output file 
scriptDir = os.path.dirname(__file__)
outputPathFile = "../output/protocol.txt"
protocolOutPath = os.path.join(scriptDir, outputPathFile)

# Protocol generation
def generate_protocol(chemicals,iterations):
  # Add control drug 
  chemicals.extend(["Morphine"])
  # Open file 
  f = open(protocolOutPath, "w")
  # Write protocol to a file
  for index, chemical in enumerate (chemicals):
    f.write("add(" + chemical + ",plate)\n")

  f.write("\n")
  f.write("move(plate, incubator)\n\n")

  # Iteration file print

  count = 0

  while count < iterations:
    f.write("grow(plate, 20 min)\n")
    f.write("move(plate, reader)\n")
    for index, chemical in enumerate (chemicals):
      f.write("measure_potency(" + chemical + ",reader)\n")
    f.write("move(plate, incubator)\n\n")
    count+=1
  
  f.write("discharge(plate, trash)\n")
  
  # close file 
  f.close()

  print("Successfully wrote experimental protocol to file at:\n")
  print(protocolOutPath,'\n')