from openfisca_core.model_api import  *
import numpy as np
from openfisca_aotearoa.entities import *

class canterbury_rates_capital_valuation(Variable):
    value_type = float
    entity = Titled_Property
    definition_period = YEAR
    label = "Local property valuation: the amount which a property is worth (CV)"
    reference = "https://www.ccc.govt.nz/services/rates-and-valuations/rates-and-valuation-search"


class canterbury_rates_works_and_services(Variable):
    value_type = float
    entity = Titled_Property
    definition_period = YEAR
    label = "Cost of works and services calculation"
    reference = "https://www.ccc.govt.nz/services/rates-and-valuations/rates-and-valuation-search"
    def formula(titled_properties, period):
        return titled_properties('canterbury_rates_capital_valuation', period) * 0.000352


class canterbury_rates_rating_wec_class_f(Variable):
    value_type = float
    entity = Titled_Property
    definition_period = YEAR
    label = "The amount of ratung unit annual charge for a variable"
    reference = "https://www.ccc.govt.nz/services/rates-and-valuations/rates-and-valuation-search"
    def formula(titled_properties, period):
        return titled_properties('canterbury_rates_capital_valuation', period) * 0.000133

class canterbury_rates_general_rate(Variable):
    value_type = float
    entity = Titled_Property
    definition_period = YEAR
    label = "The general rate charge for your capital value"
    reference = "https://www.ccc.govt.nz/services/rates-and-valuations/rates-and-valuation-search"
    def formula(titled_properties, period):
        return titled_properties('canterbury_rates_capital_valuation', period) * 0.035046

class canterbury_rates_civil_defence(Variable):
    value_type = float
    entity = Titled_Property
    definition_period = YEAR
    label = "Rates charge which goes towards civil defence"
    reference = "https://www.ccc.govt.nz/services/rates-and-valuations/rates-and-valuation-search"

    def formula(titled_properties, period):
        return titled_properties('canterbury_rates_capital_valuation', period) * 0.001434

class canterbury_rates_waimak_reg_park(Variable):
    value_type = float
    entity = Titled_Property
    definition_period = YEAR
    label = "cost of rates which go towards the waimak reg park"
    reference = "https://www.ccc.govt.nz/services/rates-and-valuations/rates-and-valuation-search"

    def formula(titled_properties, period):
        return titled_properties('canterbury_rates_capital_valuation', period) * 0.000847

class canterbury_rates_urban_transport_chch(Variable):
    value_type = float
    entity = Titled_Property
    definition_period = YEAR
    label = "cost of rates which go to transport in chch"
    reference = "https://www.ccc.govt.nz/services/rates-and-valuations/rates-and-valuation-search"

    def formula(titled_properties, period):
        return titled_properties('canterbury_rates_capital_valuation', period) * 0.025066


class canterbury_rates_ashley_reg_park(Variable):
    value_type = float
    entity = Titled_Property
    definition_period = YEAR
    label = "rates charge for of wfpp class b"
    reference = "https://www.ccc.govt.nz/services/rates-and-valuations/rates-and-valuation-search"

    def formula(titled_properties, period):
        return titled_properties('canterbury_rates_capital_valuation', period) * 0.000137



class canterbury_rates_wfpp_class_b(Variable):
    value_type = float
    entity = Titled_Property
    definition_period = YEAR
    label = "rates charge for of wfpp class b"
    reference = "https://www.ccc.govt.nz/services/rates-and-valuations/rates-and-valuation-search"

    def formula(titled_properties, period):
        return titled_properties('canterbury_rates_capital_valuation', period) * 0.000193


class canterbury_rates_rating_unit_annual_charge(Variable):
    value_type = float
    entity = Titled_Property
    definition_period = YEAR
    default_value = 24
    label = "Annual charge for each rating unit"
    reference = "https://www.ccc.govt.nz/services/rates-and-valuations/rates-and-valuation-search"

class canterbury_rates_air_quality(Variable):
    value_type = float
    entity = Titled_Property
    definition_period = YEAR
    label = "Environment Canterbury charge for air quality"
    reference = "https://www.ccc.govt.nz/services/rates-and-valuations/rates-and-valuation-search"

    def formula(titled_properties, period):
        return titled_properties('canterbury_rates_capital_valuation', period) * 0.002071


class canterbury_rates_charge(Variable):
    value_type = float
    entity = Titled_Property
    definition_period = YEAR
    label = "Environment Canterbury rates charge"
    reference = "https://www.ccc.govt.nz/services/rates-and-valuations/rates-and-valuation-search"

    def formula(titled_properties, period):
        charges = titled_properties('canterbury_rates_works_and_services', period) + \
            titled_properties('canterbury_rates_rating_wec_class_f', period) + \
            titled_properties('canterbury_rates_general_rate', period) + \
            titled_properties('canterbury_rates_civil_defence', period) + \
            titled_properties('canterbury_rates_waimak_reg_park', period) + \
            titled_properties('canterbury_rates_urban_transport_chch', period) + \
            titled_properties('canterbury_rates_ashley_reg_park', period) + \
            titled_properties('canterbury_rates_wfpp_class_b', period) + \
            titled_properties('canterbury_rates_air_quality', period)
        return charges