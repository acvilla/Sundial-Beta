from common import InputInterface
from pyradioconfig.calculator_model_framework.CalcManager import CalcManager
from efr32category import Efr32Category

__all__ = ["Efr32CfgInput"]

class Efr32CfgInput(InputInterface):
    """
    Input is a high level container that holds categories.
    Do not get this confused with the actual input kay/value pairs.
    This is just a container for other objects.
    """

    def __init__(self, model_instance):
        
        profile = model_instance.profile
        
        # Stores all categories found
        catagories = set()
        #catagories.add(Efr32Category.OUTPUT_CATEGORY_STRING)  # Place holder for outputs without categories
        
        for input in profile.inputs:
            if input.category is not None:
                if not input.category == "":
                    catagories.add(input.category)
                else:
                    if Efr32Category.NO_CATEGORY_STRING not in catagories:
                        catagories.add(Efr32Category.NO_CATEGORY_STRING)  # Place holder for inputs without categories

        #for output in profile.outputs:
        #    if output.category is not None:
        #        if not output.category == "":
        #            catagories.add(output.category)

        # Add all categories as attributes
        for catagory in catagories:
            setattr(self, str(catagory), Efr32Category(catagory, profile))
        

