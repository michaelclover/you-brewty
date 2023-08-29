import json

import calculate

class Recipe:

    def __init__(self, 
                 name="", 
                 efficiency=0.0, 
                 yeast_attenuation=0.0, 
                 initial_volume=0, 
                 target_water_grist_ratio=0, 
                 boil_time=0, 
                 fermentables=[{}], 
                 hops=[{}],
                 notes=""):
        self.file_version = 1.0
        self.name = name
        self.efficiency = efficiency
        self.yeast_attenuation = yeast_attenuation
        self.initial_volume = initial_volume
        self.target_water_grist_ratio = target_water_grist_ratio
        self.boil_time = boil_time
        self.fermentables = fermentables
        self.hops = hops
        self.notes = notes

    def __eq__(self, other):
        return (isinstance(other, Recipe) and
                self.file_version == other.file_version and
                self.name == other.name and
                self.efficiency == other.efficiency and
                self.yeast_attenuation == other.yeast_attenuation and
                self.initial_volume == other.initial_volume and
                self.target_water_grist_ratio == other.target_water_grist_ratio and
                self.boil_time == other.boil_time and
                self.fermentables == other.fermentables and
                self.hops == other.hops and
                self.notes == other.notes)

    def load_file(self, filepath):
        with open(f"{filepath}", 'r', encoding='utf-8') as f:
            self.__dict__ = json.load(f)

    def save_file(self, filepath):
        with open(f"{filepath}", 'w', encoding='utf-8') as f:
            json.dump(self.__dict__, f, ensure_ascii=False, indent=4)

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
