import calculate
import window

fermenter_volume = 5 
fermentables_potential = 36
pounds_of_malt = 8
efficiency_factor = 0.70 
yeast_attenuation = 0.28 
mash_volume = 5
    
def main():
    # given a mash volume (in us gallons) and weight of fermentables (in lbs), 
    # calculate the remaining liquid after grain absorption.
    remaining_volume = calculate.post_mash_volume(mash_volume, pounds_of_malt)
    print(f"Mash volume(gals): {mash_volume:.2f}\n\
Fermentables weight(lbs): {pounds_of_malt:.2f}\n\
Water remaining post-mash(gals): {remaining_volume:.2f}\n")
    
    # given lbs of fermentables, their potential, the final fermenter volume,
    # an efficiency factor based on how much sugar the system can extract
    # from the fermentables, and the attentuation of the brewing yeast used,
    # estimate the final ABV content.
    abv = calculate.abv(pounds_of_malt, 
                        fermentables_potential, 
                        fermenter_volume, 
                        efficiency_factor, 
                        yeast_attenuation)
    print(f"ABV: {abv:.2f}%")

    wnd = window.Window(640, 480)
    wnd.mainloop()

if __name__ == "__main__":
    main()
