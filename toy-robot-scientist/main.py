# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
import os

# Import custom modules
from scripts.knowledge_model import knowledge_model_construct
from scripts.abduction_reasoning import reasoning
from scripts.planning import planning
from scripts.toy_lab_agent import experimental_results
from scripts.toy_lab_analysis import results_analysis


# Create the path to the Hypotheses data file 
scriptDir = os.path.dirname(__file__)
dataPathHypFile = "./output/hypotheses.txt"
hypDataPath = os.path.join(scriptDir, dataPathHypFile)

# Create the path to the protocol output file 
outputPathFile = "./output/protocol.txt"
protocolOutPath = os.path.join(scriptDir, outputPathFile)

# Create the path to the experimental results output file 
outputResPathFile = "./output/experimental_results.txt"
expResultsOutPath = os.path.join(scriptDir, outputResPathFile)

# Remove hypotheses from file (clean data at every run)
f = open(hypDataPath, "w")
f.write("")
f.close()

# Remove protocol from file (clean data at every run)
f = open(protocolOutPath, "w")
f.write("")
f.close()

# Remove experimental results from file (clean data at every run)
f = open(expResultsOutPath, "w")
f.write("")
f.close()


# Create the menu
main_menu = ConsoleMenu("----------------------- A Toy Robot Scientist -----------------------")

# Knowledge Model menu item (calls the knowledge model function)
function_item_knowledge = FunctionItem("Toy Knowledge Model", knowledge_model_construct,[])
# Reasoning menu item (calls the reasoning function)
function_item_reasoning = FunctionItem("Toy Reasoning", reasoning, [])
# Planning agent menu item (calls the planning function)
function_item_planning = FunctionItem("Toy Planning", planning, [])
# Toy lab agent menu item (calls the experimental_results function)
function_item_toy_lab = FunctionItem("Toy Lab Agent", experimental_results , [])
# Results analysis agent menu item (calls the results_analysis function)
function_item_toy_analysis = FunctionItem("Toy Results Analysis Agent", results_analysis , [])



# Add the items to the menu
main_menu.append_item(function_item_knowledge)
main_menu.append_item(function_item_reasoning)
main_menu.append_item(function_item_planning)
main_menu.append_item(function_item_toy_lab)
main_menu.append_item(function_item_toy_analysis)

# Initialise the main menu
main_menu.show()
