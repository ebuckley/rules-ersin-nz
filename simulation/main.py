from openfisca_aotearoa import CountryTaxBenefitSystem
from openfisca_core.scripts.simulation_generator import make_simulation, randomly_init_variable


def main():
    system = CountryTaxBenefitSystem()
    print "created the system %s" % system

    # SETUP the scenario input data
    # http: // openfisca.org / doc / input_data.html
    scenario = system.new_scenario()

    sim = make_simulation(system, 400, 100)
    randomly_init_variable(sim, 'income_tax__annual_gross_income', 2017, max_value=240000)
    randomly_init_variable(sim, 'income_tax__annual_total_deduction', 2017, max_value=20000)

    res = sim.calculate('income_tax__taxable_income', 2017)
    import pdb
    pdb.set_trace()

if __name__ == '__main__':
    main()