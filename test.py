import unittest

import recipe

class TestCalculations(unittest.TestCase):

    sample_recipe = recipe.Recipe(name="SMaSH pale ale",
                                  efficiency=0.70,
                                  yeast_attenuation=0.28,
                                  initial_volume=7,
                                  target_water_grist_ratio=3,
                                  boil_time=1,
                                  fermentables=[{"weight": 10, "potential": 38, "lovibond": 3.75}],
                                  hops=[{"ounces": 1.5, "aau": 6.4, "boil_time": 60}, 
                                        {"ounces": 1.0, "aau": 4.6, "boil_time": 15}])

    def test_pre_boil_og(self):
        self.assertAlmostEqual(self.sample_recipe.pre_boil_og(), 1.046, 3)

    def test_post_boil_og(self):
        self.assertAlmostEqual(self.sample_recipe.post_boil_og(), 1.053, 3)

    def test_fg(self):
        self.assertAlmostEqual(self.sample_recipe.final_gravity(), 1.015, 3)

    def test_abv(self):
        self.assertAlmostEqual(self.sample_recipe.estimate_abv(), 5.02, 2)

    def test_post_mash_volume(self):
        self.assertAlmostEqual(self.sample_recipe.pre_boil_volume(), 5.8, 2)

    def test_post_boil_volume(self):
        self.assertAlmostEqual(self.sample_recipe.post_boil_volume(), 5.01, 2)

    def test_tinseth_ibu(self):
        self.assertAlmostEqual(self.sample_recipe.tinseth_ibu(), 42.60, 2)

    def test_malt_colour_units(self):
        self.assertAlmostEqual(self.sample_recipe.malt_colour_units(), 7.49, 2)

    def test_morey_srm(self):
        self.assertAlmostEqual(self.sample_recipe.morey_srm(), 5.94, 2)

    def test_mash_water(self):
        self.assertAlmostEqual(self.sample_recipe.mash_volume(), 3.5, 2)

    def sparge_volume(self):
        self.assertAlmostEqual(self.sample_recipe.sparge_volume(), 3.5, 2)

if __name__ == "__main__":
    unittest.main()