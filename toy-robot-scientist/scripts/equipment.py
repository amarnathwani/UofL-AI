# List of equipment
# Equipment --> function-action --> entity that the function-action can be applied
# e.g. plate(store, cell_culture)
def list_of_equipment():
  equipment = [("plate","store","cell_culture"),
         ("incubator","grow","plate"),
         ("reader","measure_potency","plate"),
         ("trash","discharge","plate")]
  return equipment
