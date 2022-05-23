# Import the necessary packages
import os
from kanren import *

# Import custom modules
from .facts import list_of_facts
from .rules import list_of_rules

# Create the path to the hypotheses data file 
scriptDir = os.path.dirname(__file__)
dataPathHypFile = "../output/hypotheses.txt"
hypDataPath = os.path.join(scriptDir, dataPathHypFile)

# Function for the abduction reasoning
def reasoning():

    print("----------------ABDUTCION REASONING------------------\n\n")
   
    print("Rules:\n")
    for index, rule in enumerate (list_of_rules()):
        print(index+1,")",rule,"\n")
    
    print("Facts:\n")
    for index, fact in enumerate (list_of_facts()):
        print(index+1,")",fact[0],"is a",fact[1],"\n")

    # Construct the relation (small molecule is a)    
    is_a = Relation()

    # Check for a potential drug (based on facts)
    def likely_drug(x,y): 
        return is_a(x, y)
    
    # Construct the facts
    for fact in list_of_facts():
        facts(is_a, (fact[0],fact[1])) # fact[0] chamical name, fact[1] chemical property
  
    # Which chemical is a drug?
    whichChemicalIsDrug = var()
    # This can be changed to other rules
    chemical_property_rule = "small molecule"
    # Generating the list of potential drugs
    # run (number of answers, response, relation function)
    output = run(0, whichChemicalIsDrug, likely_drug(whichChemicalIsDrug,chemical_property_rule))
    
    # All potential drugs inferred
    potential_drugs = output
    
    print("Potential Drugs:\n")
    for index, potential_drug in enumerate (potential_drugs):
        print(index+1,")",potential_drug,"\n")

    # Save Hypotheses to a file 
    f = open(hypDataPath, "w")
    for index, potential_drug in enumerate (potential_drugs):
        f.write(potential_drug + "\n")
    f.close()
    # /output/hypotheses.txt
    print("Successfully wrote hypotheses to file at:\n")
    print(hypDataPath,'\n')
 
   
    # Pause the function to go back to the main menu    
    input("------------PRESS ENTER FOR THE MAIN MENU------------")