fermenter_volume = 5 
fermentables_potential = 36
pounds_of_malt = 8
efficiency_factor = 0.70 
yeast_attenuation = 0.28 
mash_volume = 5

def kg_to_lb(kg):
    return kg * 2.205

def lb_to_kg(lb):
    return lb / 2.205

def us_gallon_to_litre(gal):
    return gal * 3.785

def litre_to_us_gallon(litre):
    return litre / 3.785

def to_ppm(g):
    return (g / 1000) + 1

# f_weight =        weight of fermentable in lbs
# f_potential =     potential of fermentable in percent (%) though needs converting to ppm
# f_volume =        the final liquid volume into the fermenter, in US gallons
# e_factor =        how efficient the brew system is at extracting all of the sugars
# y_attenuation =   the attenuation of the yeast being used in percent (%) though needs converting to fraction
def calculate_abv(f_weight, f_potential, f_volume, e_factor, y_attenuation):
    gp = f_potential * f_weight
    gp *= efficiency_factor
    og = gp / f_volume
    fg = og * y_attenuation
    return (to_ppm(og) - to_ppm(fg)) * 131.25

# initial_volume =   the initial mash or strike volume in us gals
# lbs_fermentables = the weight of fermentables in lbs
def calculate_post_mash_volume(initial_volume, lbs_fermentables):
    vol_ltrs = us_gallon_to_litre(initial_volume)
    fermentables_kgs = lb_to_kg(lbs_fermentables)
    return litre_to_us_gallon(vol_ltrs - fermentables_kgs)
    
def main():
    # given a mash volume (in us gallons) and weight of fermentables (in lbs), 
    # calculate the remaining liquid after grain absorption.
    remaining_volume = calculate_post_mash_volume(mash_volume, pounds_of_malt)
    print(f"Mash volume(gals): {mash_volume:.2f}\n\
Fermentables weight(lbs): {pounds_of_malt:.2f}\n\
Water remaining post-mash(gals): {remaining_volume:.2f}\n")
    
    # given lbs of fermentables, their potential, the final fermenter volume,
    # an efficiency factor based on how much sugar the system can extract
    # from the fermentables, and the attentuation of the brewing yeast used,
    # estimate the final ABV content.
    abv = calculate_abv(pounds_of_malt, 
                        fermentables_potential, 
                        fermenter_volume, 
                        efficiency_factor, 
                        yeast_attenuation)
    print(f"ABV: {abv:.2f}%")

if __name__ == "__main__":
    main()
