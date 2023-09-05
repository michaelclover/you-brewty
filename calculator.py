import recipe
import window
    
def output_recipe(recipe):
    print(f"\nFermentables weight: {recipe.fermentables_weight():.2f}lbs\n\
Target water-to-grist ratio: {recipe.target_water_grist_ratio} ltr/kg\n\
Initial volume: {recipe.initial_volume:.2f}gals\n\
Mash volume: {recipe.mash_volume():.2f}gals\n\
Sparge volume: {recipe.sparge_volume():.2f}gals\n\
Pre-boil volume: {recipe.pre_boil_volume():.2f}gals\n\
Post-boil volume: {recipe.post_boil_volume():.2f}gals\n\
Estimated pre-boil og: {recipe.pre_boil_og():.3f}\n\
Estimated post-boil og: {recipe.post_boil_og():.3f}\n\
Estimated fg: {recipe.final_gravity():.3f}\n\
ABV: {recipe.estimate_abv():.2f}%\n\
IBU: {recipe.tinseth_ibu():.2f}\n\
MCU: {recipe.malt_colour_units():.2f}\n\
SRM: {recipe.morey_srm():.2f}\n")

def main():

    # load our recipe.
    sample_recipe = recipe.Recipe()
    sample_recipe.load_file("./recipes/SMaSH pale ale.json")

    output_recipe(sample_recipe)

    win = window.Window(sample_recipe)
    win.mainloop()

if __name__ == "__main__":
    main()
