import customtkinter
import cpt_fuse_calc


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

main = customtkinter.CTk()
main.geometry("500x300")

# Setting Frame    
frame = customtkinter.CTkFrame(main)
frame.pack(pady=20, padx=10, fill="both", expand=True)

# --------------Widgets----------------------

#Main Label
label = customtkinter.CTkLabel(frame, text="FUSE SIZE CALCULATOR", font=("Helvetica",18)) 
label.pack(pady=12, padx=10)

#CPT Power Entry
cpt_power = customtkinter.CTkEntry(frame, placeholder_text="CPT Power (VA)", width=150)
cpt_power.pack(pady=12, padx=10)


#CPT Primary winding 
cpt_primary = customtkinter.CTkEntry(frame, placeholder_text="CPT Primary Winding", width=150)
cpt_primary.pack(pady=12, padx=10)

#CPT Secondary winding
cpt_secondary = customtkinter.CTkEntry(frame, placeholder_text="CPT Secondary Winding", width=150)
cpt_secondary.pack(pady=12, padx=10)
'''
#Calculate button

def button_click_event():
    dialog = customtkinter.CTkInputDialog(text="Calculate", title="CALCULATE")
    cpt_fuse_calc.calculate_fuse_size()
    print("Number:", dialog.get_input())
'''  
def open_popup():
    top=customtkinter.CTkToplevel(main)
    top.geometry("500x100")
    top.title("Fuse Size Value")
    top.resizable(False, False)
    top.attributes('-topmost', True)
    
    #Get entry inputs
    cpt_power_input = cpt_power.get()
    cpt_primary_input = cpt_primary.get()
    cpt_secondary_input = cpt_secondary.get()
    
    #Function to calcule Fuse Size
    fuse_size = cpt_fuse_calc.calculate_fuse_size(cpt_power_input, cpt_primary_input, cpt_secondary_input)
    
    customtkinter.CTkLabel(top, text=f'Primary: {fuse_size[0]}, Secondary: {fuse_size[1]}').place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)


button = customtkinter.CTkButton(frame, text="Calculate", command=open_popup)
button.pack(pady=15)

    
main.mainloop()
    
    


