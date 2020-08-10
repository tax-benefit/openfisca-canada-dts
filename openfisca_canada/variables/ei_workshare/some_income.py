from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_canada.entities import Person, Family

class has_some_income_1001_or_more_reduced_hours(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person eligible for the EI Workshare?"
    definition_period = MONTH
    reference = u"TODO"
    def formula(persons, period, parameters):
        return persons("some_income__hours_reduced",period) + \
        persons("some_income__1001_or_more",period)

class some_income__1001_or_more(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person making #1001 or more?"
    definition_period = MONTH
    reference = u"TODO"

class some_income__hours_reduced(Variable):
    value_type = bool
    entity = Person
    label = u"This person has some income or hours reduced?"
    definition_period = MONTH
    reference = u"TODO"