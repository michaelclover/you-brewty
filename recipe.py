import calculate

class Recipe:

    def __init__(self, name, efficiency, yeast_attenuation, initial_volume, 
                 target_water_grist_ratio, boil_time, fermentables, hops):
        self.name = name
        self.efficiency = efficiency
        self.yeast_attenuation = yeast_attenuation
        self.initial_volume = initial_volume
        self.target_water_grist_ratio = target_water_grist_ratio
        self.boil_time = boil_time
        self.fermentables = fermentables
        self.hops = hops

    # private methods

    def fermentables_weight(self):
        lbs = 0.0
        for i in self.fermentables:
            lbs += i["weight"]
        return lbs

    def fermentables_potential(self):
        potential = 0.0
        for i in self.fermentables:
            potential += i["potential"]
        return potential

    # public methods

    def mash_volume(self):
        return calculate.mash_water(self.target_water_grist_ratio, self.fermentables_weight())

    def sparge_volume(self):
        return self.initial_volume - self.mash_volume()

    def pre_boil_volume(self):
        return calculate.post_mash_volume(self.initial_volume, self.fermentables_weight())

    def post_boil_volume(self):
        return calculate.post_boil_volume(self.pre_boil_volume(), self.boil_time)

    def estimate_abv(self):
        return calculate.abv(self.fermentables_weight(), 
                             self.fermentables_potential(),
                             self.post_boil_volume(),
                             self.efficiency,
                             self.yeast_attenuation)

    def pre_boil_og(self):
        return calculate.og(self.fermentables_weight(), 
                            self.fermentables_potential(),
                            self.efficiency,
                            self.pre_boil_volume())

    def post_boil_og(self):
        return calculate.og(self.fermentables_weight(),
                            self.fermentables_potential(),
                            self.efficiency,
                            self.post_boil_volume())

    def final_gravity(self):
        return calculate.fg(self.post_boil_og(), self.yeast_attenuation)

    def tinseth_ibu(self):
        ibu = 0.0
        for i in self.hops:
            ibu += calculate.tinseth_ibu(i["aau"], 
                                         i["ounces"], 
                                         i["boil_time"], 
                                         self.pre_boil_og(), 
                                         self.post_boil_volume())
        return ibu

    def malt_colour_units(self):
        mcu = 0.0
        for i in self.fermentables:
            mcu += calculate.malt_colour_units(i["weight"], i["lovibond"], self.post_boil_volume())
        return mcu

    def morey_srm(self):
        return calculate.morey_srm(self.malt_colour_units())
