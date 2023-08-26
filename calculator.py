import calculate
import window

batch_volume = 28 # the target batch volume, e.g. the desired amount of water into the fermenter
water_grist_ratio = 3 # target water-to-grist-ratio, in litres per kg of malt
fermenter_volume = 5 # target volume into the fermenter, in us gals
fermentables_potential = 36 # the points potential of the fermentables, 1.036 for pale malt
pounds_of_malt = 10 # the amount of malt to use in the recipe, in lbs
efficiency_factor = 0.70 # the efficiency factor of the brewing system setup
yeast_attenuation = 0.28 # the attenuation of the yeast used in this recipe
mash_volume = 5 # the volume to use in the mash, in us gals

hop_oz = 1.5
hop_aau = 6.4
hop_boil = 60

hop1_oz = 1
hop1_aau = 4.6
hop1_boil = 15

malt_lovibond = 3.75
    
def main():
    # given a mash volume (in us gallons) and weight of fermentables (in lbs), 
    # calculate the remaining liquid after grain absorption.
    pre_boil_volume = calculate.post_mash_volume(mash_volume, pounds_of_malt)

    # calculate the post boil volume, accounting for water loss to evaporation.
    post_boil_volume = calculate.post_boil_volume(pre_boil_volume, 1)
    
    # given lbs of fermentables, their potential, the final fermenter volume,
    # an efficiency factor based on how much sugar the system can extract
    # from the fermentables, and the attentuation of the brewing yeast used,
    # estimate the final ABV content.
    abv = calculate.abv(pounds_of_malt, 
                        fermentables_potential, 
                        fermenter_volume, 
                        efficiency_factor, 
                        yeast_attenuation)

    ibu = calculate.tinseth_ibu(hop_aau, hop_oz, hop_boil, 1.080, 5)
    ibu += calculate.tinseth_ibu(hop1_aau, hop1_oz, hop1_boil, 1.080, 5)

    mcu = calculate.malt_colour_units(pounds_of_malt, malt_lovibond, batch_volume)
    srm = calculate.morey_srm(mcu)

    print(f"\nFermentables weight(lbs): {pounds_of_malt:.2f}\n\
Mash volume(gals): {mash_volume:.2f}\n\
Pre-boil volume(gals): {pre_boil_volume:.2f}\n\
Post-boil volume(gals): {post_boil_volume:.2f}\n\
ABV: {abv:.2f}%\n\
IBU: {ibu}\n\
SRM: {srm:.2f}\n")

    '''wnd = window.Window(640, 480)
    wnd.title("You Brewty!")
    wnd.centre()
    wnd.mainloop()'''

if __name__ == "__main__":
    main()
