import calculate
#import window

fermentables_potential = 38 # the points potential of the fermentables, 1.036 for pale malt
pounds_of_malt = 10 # the amount of malt to use in the recipe, in lbs
malt_lovibond = 3.75 # the lovibond degrees of the chosen malt/fermentable
efficiency_factor = 0.70 # the efficiency factor of the brewing system setup
yeast_attenuation = 0.28 # the attenuation of the yeast used in this recipe
initial_volume = 7 # the volume to use in the mash, in us gals
target_water_grist_ratio = 3 # the target water grist ratio for the mash, ratio in ltr/kg

# the first hop addition.
hop_oz = 1.5
hop_aau = 6.4
hop_boil = 60

# the second hop addition.
hop1_oz = 1
hop1_aau = 4.6
hop1_boil = 15
    
def main():

    # calculate the mash volume based on the desired water-to-grist ratio.
    mash_volume = calculate.mash_water(target_water_grist_ratio, pounds_of_malt)

    # calculate the sparge volume based on the initial volume minus the mash volume.
    sparge_volume = initial_volume - mash_volume

    # given a mash volume (in us gallons) and weight of fermentables (in lbs), 
    # calculate the remaining liquid after grain absorption.
    pre_boil_volume = calculate.post_mash_volume(initial_volume, pounds_of_malt)

    # calculate the post boil volume, accounting for water loss to evaporation.
    post_boil_volume = calculate.post_boil_volume(pre_boil_volume, 1)
    
    # given lbs of fermentables, their potential, the final fermenter volume,
    # an efficiency factor based on how much sugar the system can extract
    # from the fermentables, and the attentuation of the brewing yeast used,
    # estimate the final ABV content.
    abv = calculate.abv(pounds_of_malt, 
                        fermentables_potential, 
                        post_boil_volume, 
                        efficiency_factor, 
                        yeast_attenuation)

    # calculate the pre-boil og.
    pre_boil_og = calculate.og(pounds_of_malt, fermentables_potential, efficiency_factor, pre_boil_volume)

    # calculate the post-boil og.
    post_boil_og = calculate.og(pounds_of_malt, fermentables_potential, efficiency_factor, post_boil_volume)

    # calculate the final gravity.
    fg = calculate.fg(post_boil_og, yeast_attenuation)

    # calculate the tinseth bittering units.
    ibu = calculate.tinseth_ibu(hop_aau, hop_oz, hop_boil, pre_boil_og, post_boil_volume)
    ibu += calculate.tinseth_ibu(hop1_aau, hop1_oz, hop1_boil, pre_boil_og, post_boil_volume)

    # calculate the malt colour units and the Morey standard reference method.
    mcu = calculate.malt_colour_units(pounds_of_malt, malt_lovibond, post_boil_volume)
    srm = calculate.morey_srm(mcu)

    print(f"\nFermentables weight: {pounds_of_malt:.2f}lbs\n\
Target water-to-grist ratio: {target_water_grist_ratio} ltr/kg\n\
Initial volume: {initial_volume:.2f}gals\n\
Mash volume: {mash_volume:.2f}gals\n\
Sparge volume: {sparge_volume:.2f}gals\n\
Pre-boil volume: {pre_boil_volume:.2f}gals\n\
Post-boil volume: {post_boil_volume:.2f}gals\n\
Estimated pre-boil og: {pre_boil_og:.3f}\n\
Estimated post-boil og: {post_boil_og:.3f}\n\
Estimated fg: {fg:.3f}\n\
ABV: {abv:.2f}%\n\
IBU: {ibu:.2f}\n\
SRM: {srm:.2f}\n")

    '''wnd = window.Window(640, 480)
    wnd.title("You Brewty!")
    wnd.centre()
    wnd.mainloop()'''

if __name__ == "__main__":
    main()
