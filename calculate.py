import math
import convert

# weight =        weight of fermentable
# potential =     potential of fermentable in percent (%) though needs converting to ppm
# volume =        the final liquid volume into the fermenter
# factor =        how efficient the brew system is at extracting all of the sugars
# attenuation =   the attenuation of the yeast being used in percent (%) though needs converting to fraction
# metric =        if the input is in metric (ltrs/kgs) 
def abv(weight, potential, volume, factor, attenuation, metric):
    if metric is True:
        weight = convert.kg_to_lb(weight)
        volume = convert.litre_to_us_gallon(volume)
    ogg = og(weight, potential, factor, volume, metric, True)
    fgg = fg(ogg, attenuation)
    return (ogg - fgg) * 131.25

# weight =        weight of fermentable
# potential =     potential of fermentable in percent (%) though needs converting to ppm
# volume =        the final liquid volume into the fermenter
# factor =        how efficient the brew system is at extracting all of the sugars
# metric =        if the input is in metric (ltrs/kgs) 
def og(weight, potential, factor, volume, metric, already_converted=False):
    if metric is True and already_converted is False:
        weight = convert.kg_to_lb(weight)
        volume = convert.litre_to_us_gallon(volume)
    gp = potential * weight
    gp *= factor
    if gp > 0 and volume > 0:
        og = gp / volume
    else:
        og = 0.0
    return convert.to_ppm(og)

# og =              the original gravity in ppm
# attenuation =     the attenuation of the yeast being used in percent (%) though needs converting to fraction
def fg(og, attenuation):
    return 1 + (og - 1) * attenuation

# initial_volume =      the initial mash or strike volume
# fermentables_weight = the weight of fermentables
# metric =              if the input is in metric (ltrs/kgs) 
def post_mash_volume(initial_volume, fermentables_weight, metric):
    if metric is True:
        return initial_volume - fermentables_weight
    else:
        initial_volume = convert.us_gallon_to_litre(initial_volume)
        fermentables_weight = convert.lb_to_kg(fermentables_weight)
        return convert.litre_to_us_gallon(initial_volume - fermentables_weight)

# initial_volume =  the initial pre-boil volume
# boil duration =   the duration of the boil in hours
# metric =          if the input is in metric (ltrs/kgs) 
def post_boil_volume(initial_volume, boil_duration, metric):
    if metric is True:
        return initial_volume - (3.0 * boil_duration)
    else:
        initial_volume = convert.us_gallon_to_litre(initial_volume)
        return convert.litre_to_us_gallon(initial_volume - (3.0 * boil_duration))

# boil_gravity = the gravity of the boil, i.e. the ferment potential x poundage over the boil volume
# intro_time =   minutes during the boil the hops are introduced
def tinseth_utilisation(boil_gravity, intro_time):
    fg = 1.65 * math.pow(0.000125, (boil_gravity - 1)) #0.000125(boil_gravity - 1)
    ft = (1 - math.pow(math.e, (-0.04 * intro_time))) / 4.15
    return fg * ft

# aau (alpha acid units) =  aau of the hop used
# weight =                  weight of hops used in the boil
# intro_time =              minutes during the boil the hops are introduced
# boil_gravity =            the gravity of the boil, i.e. the ferment potential x poundage over the boil volume
# final_volume =            the final recipe volume
def tinseth_ibu(aau, weight, intro_time, boil_gravity, final_volume, metric):
    if metric is True:
        weight = convert.grams_to_ounces(weight)
        final_volume = convert.litre_to_us_gallon(final_volume)
    au = aau * weight
    util = tinseth_utilisation(boil_gravity, intro_time)
    tinseth = au * util * (75 / final_volume)
    return tinseth

# weight =      the weight of the fermentable
# lovibond =    the degrees lovibond of the fermentable
# vol =         the batch volume
def malt_colour_units(weight, lovibond, vol, metric):
    if metric is True:
        weight = convert.kg_to_lb(weight)
        vol = convert.litre_to_us_gallon(vol)
    return (weight * lovibond) / vol

# mcu = malt colour units
def morey_srm(mcu):
    return 1.4922 * (math.pow(mcu, 0.6859))

# target =  the target water-to-grist ratio, expressed as either ltr/kg or us gal/lb
# weight =  weight of fermentables
# metric =  if the input is in metric (ltrs/kgs) 
def mash_water(target, weight, metric):
    if metric is True:
        return math.floor((weight * target) * 10) / 10
    else:
        return math.floor(convert.litre_to_us_gallon(convert.lb_to_kg(weight) * target) * 10) / 10