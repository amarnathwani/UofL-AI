# Import the necessary packages
import os
from rdflib import Graph
from PIL import Image                                                                                

# Create the path to the RDF data file 
scriptDir = os.path.dirname(__file__)
dataPathRdf = "../data/domain.owl"
rdfDataPath = os.path.join(scriptDir, dataPathRdf)

# Create the path to the data image
dataPathImage = "../data/domain.png"
imageDataPath = os.path.join(scriptDir, dataPathImage)

# Parse and view information aobut the RDF file
def knowledge_model_construct():
  # Initialise a graph
  graph = Graph()

  # Parse in RDF graph
  graph.parse(rdfDataPath, format='application/rdf+xml')

  print ("------------------------------KNOWLEDGE MODEL DATA-----------------------------\n\n")

  # Loop each triple in the graph
  for index, (sub, pred, obj) in enumerate(graph):
    print(sub,pred,obj)
 
  print ("-------------------------------------------------------------------------------\n\n")
  
  # Print the number of triples (size of the Graph)
  print(f'The graph has {len(graph)} entries\n\n')
  
  # Open and show the data model RDF image
  # Note: The image is not dinamically generated, it is only an example for this ontology
  img = Image.open(imageDataPath)
  img.show() 

  # Pause the function to go back to the main menu
  input("------------PRESS ENTER FOR THE MAIN MENU------------")
