import convert

# weight =        weight of fermentable in lbs
# potential =     potential of fermentable in percent (%) though needs converting to ppm
# volume =        the final liquid volume into the fermenter, in US gallons
# factor =        how efficient the brew system is at extracting all of the sugars
# attenuation =   the attenuation of the yeast being used in percent (%) though needs converting to fraction
def abv(weight, potential, volume, factor, attenuation):
    gp = potential * weight
    gp *= factor
    og = gp / volume
    fg = og * attenuation
    return (convert.to_ppm(og) - convert.to_ppm(fg)) * 131.25

# initial_volume =   the initial mash or strike volume in us gals
# lbs_fermentables = the weight of fermentables in lbs
def post_mash_volume(initial_volume, lbs_fermentables):
    vol_ltrs = convert.us_gallon_to_litre(initial_volume)
    fermentables_kgs = convert.lb_to_kg(lbs_fermentables)
    return convert.litre_to_us_gallon(vol_ltrs - fermentables_kgs)

# initial_volume = the initial pre-boil volume in us gals
# boil duration = the duration of the boil in hours
def post_boil_volume(initial_volume, boil_duration):
    post_volume = convert.us_gallon_to_litre(initial_volume)
    return convert.litre_to_us_gallon(post_volume - (3.0 * boil_duration))