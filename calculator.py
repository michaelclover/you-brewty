import recipe
    
def main():

    # load our recipe.
    sample_recipe = recipe.Recipe()
    sample_recipe.load_file("./recipes/SMaSH pale ale.json")

    # calculate the mash volume based on the desired water-to-grist ratio.
    mash_volume = sample_recipe.mash_volume()

    # calculate the sparge volume based on the initial volume minus the mash volume.
    sparge_volume = sample_recipe.sparge_volume()

    # given a mash volume (in us gallons) and weight of fermentables (in lbs), 
    # calculate the remaining liquid after grain absorption.
    pre_boil_volume = sample_recipe.pre_boil_volume()

    # calculate the post boil volume, accounting for water loss to evaporation.
    post_boil_volume = sample_recipe.post_boil_volume()
    
    # given lbs of fermentables, their potential, the final fermenter volume,
    # an efficiency factor based on how much sugar the system can extract
    # from the fermentables, and the attentuation of the brewing yeast used,
    # estimate the final ABV content.
    abv = sample_recipe.estimate_abv()

    # calculate the pre-boil og.
    pre_boil_og = sample_recipe.pre_boil_og()

    # calculate the post-boil og.
    post_boil_og = sample_recipe.post_boil_og()

    # calculate the final gravity.
    fg = sample_recipe.final_gravity()

    # calculate the tinseth bittering units.
    ibu = sample_recipe.tinseth_ibu()

    # calculate the malt colour units and the Morey standard reference method.
    mcu = sample_recipe.malt_colour_units()
    srm = sample_recipe.morey_srm()

    print(f"\nFermentables weight: {sample_recipe.fermentables_weight():.2f}lbs\n\
Target water-to-grist ratio: {sample_recipe.target_water_grist_ratio} ltr/kg\n\
Initial volume: {sample_recipe.initial_volume:.2f}gals\n\
Mash volume: {mash_volume:.2f}gals\n\
Sparge volume: {sparge_volume:.2f}gals\n\
Pre-boil volume: {pre_boil_volume:.2f}gals\n\
Post-boil volume: {post_boil_volume:.2f}gals\n\
Estimated pre-boil og: {pre_boil_og:.3f}\n\
Estimated post-boil og: {post_boil_og:.3f}\n\
Estimated fg: {fg:.3f}\n\
ABV: {abv:.2f}%\n\
IBU: {ibu:.2f}\n\
MCU: {mcu:.2f}\n\
SRM: {srm:.2f}\n")

if __name__ == "__main__":
    main()
