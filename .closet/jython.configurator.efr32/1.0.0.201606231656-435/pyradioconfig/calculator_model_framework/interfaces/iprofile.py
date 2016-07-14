from abc import ABCMeta, abstractmethod
from pyradioconfig.pycalcmodel import ModelProfile, ModelVariable, ModelInput, ModelForce, ModelInputType, ModelOutput, \
    ModelOutputType, ModelInputDefaultVisibilityType

"""
Profile interface file
"""
class IProfile(object):

    _profileName = ""
    _category = ""
    _description = ""
    _default = False
    _readable_name = ""
    _activation_logic = ""

    """
    Returns profile readable and searchable nmae
    """
    @abstractmethod
    def getName(self):
        # Since this is used in code to reference the profile, it cannot have white space or spaces
        name = self._profileName.strip()
        name = name.replace(" ", "_")
        return name

    """
    Builds inputs, forced, outputs into modem model
    """
    @abstractmethod
    def buildProfileModel(self, modem_model):
        raise NotImplementedError('Call to abstract method getName()')

    """
    Builds empty profile model
    Returns: Populated profile model
    """
    @abstractmethod
    def _makeProfile(self, modem_model, category=None, description=None,
                     default=None, readable_name=None, activation_logic=None):
        # Build profile from name, category, and description
        if category is None:
            category = self._category
        if description is None:
            description = self._description
        if default is None:
            default = self._default
        if readable_name is None:
            readable_name = self._readable_name
        if activation_logic is None:
            activation_logic = self._activation_logic
        profile_model = ModelProfile(self.getName(), category, description,
                                     default=default, readable_name=readable_name, act_logic=activation_logic)
        modem_model.profiles.append(profile_model)
        return profile_model

    """
    Moves a variable from forces group into inputs group
    """
    def _moveVariableFromForcesIntoInputs(self, profile, varForce, category, default=None, input_name=None, var_value=None,
                                          value_limit_min=None, value_limit_max=None, fractional_digits=None):
        assert isinstance(varForce, ModelVariable), "FATAL ERROR: var is not ModelVariable"
        # Remove from forces
        forces_name = varForce.name
        profile.forces.remove_force(forces_name)
        # Add to inputs
        profile.inputs.append(ModelInput(varForce, category, default, input_name, var_value, value_limit_min, value_limit_max, fractional_digits=fractional_digits ))
        pass

    """
    Moves a variable from input group and inputs forces
    """
    def _moveVariableFromInputsIntoForces(self, profile, varInput, value=None):
        assert isinstance(varInput, ModelVariable), "FATAL ERROR: var is not ModelVariable"
        # Remove from inputs
        # Loop through aliases and find the right var name
        for input in profile.inputs:
            if input.var_name == varInput.name:
                input_alias = input.var_name
                profile.inputs.remove_input(input_alias)
                break
        # Add to forces
        profile.forces.append(ModelForce(varInput, value))
        pass

    """
    Helper function to create lined input/output types
    """
    def make_linked_input_output(self, profile, var, category, default=None, readable_name=None, var_value=None,
                 value_limit_min=None, value_limit_max=None, override=None, fractional_digits=None, deprecated=False, default_visibility=ModelInputDefaultVisibilityType.VISIBLE):
        # Make input
        input = ModelInput(var, category, ModelInputType.LINKED_IO, default, readable_name, var_value,
                           value_limit_min, value_limit_max, fractional_digits=fractional_digits, deprecated=deprecated, default_visibility=default_visibility)
        profile.inputs.append(input)

        # Make output
        output = ModelOutput(var, category, ModelOutputType.LINKED_IO, readable_name,
                             value_limit_min, value_limit_max, override)
        profile.outputs.append(output)
