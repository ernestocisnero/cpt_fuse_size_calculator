def calculate_fuse_size(cpt_power_input, cpt_primary_input, cpt_secondary_input):

    # Step 2: Calculate Transformer Current
    primary_current = int(cpt_power_input)/int(cpt_primary_input)
    secondary_current = int(cpt_power_input)/int(cpt_secondary_input)

    # Step 3: Select a Fuse Type (Assuming an inrush factor of 1.25)
    primary_fuse_size = primary_current*1.25
    secondary_fuse_size = secondary_current*1.25

    
    return [str(round(primary_fuse_size, 2)), str(round(secondary_fuse_size, 2))]





    