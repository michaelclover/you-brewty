import unittest
import os

import recipe

generic_recipe = recipe.Recipe(name="SMaSH pale ale",
                               efficiency=0.70,
                               yeast_attenuation=0.28,
                               initial_volume=7,
                               target_water_grist_ratio=3,
                               boil_time=1,
                               fermentables=[{"name": "malt_1", "weight": 10, "potential": 38, "lovibond": 3.75}],
                               hops=[{"name": "hop_1", "ounces": 1.5, "aau": 6.4, "boil_time": 60}, 
                                     {"name": "hop_2", "ounces": 1.0, "aau": 4.6, "boil_time": 15}],
                               notes="A recipe for a basic single malt, single hop pale ale.")

class TestCalculations(unittest.TestCase):

    sample_recipe = generic_recipe

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

    def test_sparge_volume(self):
        self.assertAlmostEqual(self.sample_recipe.sparge_volume(), 3.5, 2)

class TestRecipeClass(unittest.TestCase):

    def test_save_and_load(self):
        save_recipe = generic_recipe

        filepath = "./recipe.json"
        save_recipe.save_file(filepath)

        load_recipe = recipe.Recipe()
        load_recipe.load_file(filepath)
        
        self.assertEqual(load_recipe, save_recipe)

        if(os.path.exists(filepath)):
            os.remove(filepath)

if __name__ == "__main__":
    unittest.main()