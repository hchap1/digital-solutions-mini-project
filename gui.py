# Calum Faulds
import customtkinter as ctk
def homePage(colour = ""):
    # Create window and set size to 800x800
    window = ctk.CTk()
    window.geometry("800x800")
    # Defining widgets
    frame = ctk.CTkFrame(window, width = 800, height = 800, bg_color= "royalblue4")  #background
    # Positioning widgets on page
    frame.place(relx=0.5, rely=0.5, anchor = "center")
    # Loop Function
    window.mainloop()
homePage()
    