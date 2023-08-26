import math
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

# boil_gravity = the gravity of the boil, i.e. the ferment potential x poundage over the boil volume
# intro_time = minutes during the boil the hops are introduced
def tinseth_utilisation(boil_gravity, intro_time):
    fg = 1.65 * math.pow(0.000125, (boil_gravity - 1)) #0.000125(boil_gravity - 1)
    ft = (1 - math.pow(math.e, (-0.04 * intro_time))) / 4.15
    return fg * ft

# aau (alpha acid units) = aau of the hop used
# oz = amount of hops, in ounces, used in the boil
# intro_time = minutes during the boil the hops are introduced
# boil_gravity = the gravity of the boil, i.e. the ferment potential x poundage over the boil volume
# final_volume = the final recipe volume
def tinseth_ibu(aau, oz, intro_time, boil_gravity, final_volume):
    au = aau * oz
    util = tinseth_utilisation(boil_gravity, intro_time)
    tinseth = au * util * (75 / final_volume)
    return math.floor(tinseth)

# weight = the weight of the fermentable in lbs
# lovibond = the degrees lovibond of the fermentable
# vol = the batch volume
def malt_colour_units(weight, lovibond, vol):
    return (weight * lovibond) / vol

# mcu = malt colour units
def morey_srm(mcu):
    return 1.4922 * (math.pow(mcu, 0.6859))