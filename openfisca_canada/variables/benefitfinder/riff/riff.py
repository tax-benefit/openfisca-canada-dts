# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person

class riff__is_eligible(Variable):
    value_type = bool
    entity = Person
    default_value = False
    label = u"Is eligible for riff"
    definition_period = MONTH

    def formula(persons, period, parameters):
        return persons("riff__has_riff", period)
    
class riff__has_riff(Variable):
    value_type = bool
    default_value = False
    entity = Person
    definition_period = MONTH
    label = u"client has a riff?"

