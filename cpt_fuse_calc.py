def calculate_fuse_size(cpt_power_input, cpt_primary_input, cpt_secondary_input):
    cpt_power_input = int(cpt_power_input)
    cpt_primary_input = int(cpt_primary_input)
    cpt_secondary_input = int(cpt_secondary_input)
    
    # Calculating the primary fuse size
    if (cpt_power_input/cpt_primary_input) < 2:
        primary_fuse_size = (cpt_power_input/cpt_primary_input)*3
    elif (cpt_power_input/cpt_primary_input) < 9:
        primary_fuse_size = cpt_power_input*1.67/cpt_primary_input
    else:
        primary_fuse_size = cpt_power_input*1.25/cpt_primary_input
        
    # Calculating the secondary fuse size    
    if (cpt_power_input/cpt_secondary_input) <9:
        secondary_fuse_size = cpt_power_input*1.67/cpt_secondary_input
    else:
        secondary_fuse_size = cpt_power_input*1.25/secondary_fuse_size
        
    return [str(round(primary_fuse_size, 2)), str(round(secondary_fuse_size, 2))]


    