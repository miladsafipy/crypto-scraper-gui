import customtkinter as ctk
from tkinter import filedialog
import scraper

class ScraperApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Genaral Features
        self.title("Cryptocurrency Scraping")
        self._set_appearance_mode("light")

        # Main Container
        self.container = ctk.CTkFrame(self)
        self.container.pack(expand= True, fill= "both", ipadx=10, ipady=10)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Frame for Mode
        self.frame0 = ctk.CTkFrame(self.container)
        self.frame0.pack(expand= True, fill= "both", ipadx=10, ipady=10, pady= (10, 10), padx=(10, 10), side= "top")
        self.mode_switch = ctk.CTkSwitch(self.frame0, text="Light Mode", font=("Berlin Sans FB Demi", 12), command=self.change_appearance)
        self.mode_switch.pack(expand=True, side="right", anchor="e")

        # Frame for URL
        self.frame1 = ctk.CTkFrame(self.container)
        self.frame1.pack(expand= True, fill= "both", ipadx=10, ipady=10, pady= (0, 10), padx=(10, 10), side= "top")
        self.url_lable = ctk.CTkLabel(self.frame1, 
                                  text="Choose a Website URL",
                                  font=("Berlin Sans FB Demi", 16))
        self.url_lable.pack(expand=True, side="left")
        self.url_comboBox = ctk.CTkComboBox(self.frame1, 
                                         values=["https://arzdigital.com/coins/"],
                                         width=300,
                                         font=("Berlin Sans FB Demi", 14))
        self.url_comboBox.pack(expand=True, side="right")
        self.url_comboBox.set("Choose URL ...")

        # Frame for Pages
        self.frame2 = ctk.CTkFrame(self.container)
        self.frame2.pack(expand= True, fill= "both", ipadx=10, ipady=10, pady= (0, 10), padx=(10, 10), side= "top")
        self.pages_lable = ctk.CTkLabel(self.frame2, 
                                  text="Number of Pages to Scrap",
                                  font=("Berlin Sans FB Demi", 16))
        self.pages_lable.pack(expand=True, side="left")
        self.pages_comboBox = ctk.CTkComboBox(self.frame2, 
                                         values=[str(i) for i in range(1, 11)],
                                         width=300,
                                         font=("Berlin Sans FB Demi", 14))
        self.pages_comboBox.pack(expand=True, side="right")
        self.pages_comboBox.set("Number of pages ...")

        # Frame for Features CheckBox
        self.frame3 = ctk.CTkFrame(self.container)
        self.frame3.pack(expand= True, fill= "both", ipadx=10, ipady=10, pady= (0, 10), padx=(10, 10), side= "top")
        self.feature_lable = ctk.CTkLabel(self.frame3, 
                                  text="Please check features to add",
                                  font=("Berlin Sans FB Demi", 16))
        self.feature_lable.pack(expand=True, side="left")

            # Frame for checkBoxes
        self.frame_checkBoxes = ctk.CTkFrame(self.frame3)
        self.frame_checkBoxes.pack(expand= True, ipadx=10, ipady=10, pady= (10, 10), padx=(10, 10), side= "right")
        self.name_checkbox = ctk.CTkCheckBox(self.frame_checkBoxes, text="Coin's name", font=("Berlin Sans FB Demi", 14))
        self.name_checkbox.pack(expand=False, side="top", anchor="nw", pady=(5, 5))
        self.price_checkbox = ctk.CTkCheckBox(self.frame_checkBoxes, text="Coin's price", font=("Berlin Sans FB Demi", 14))
        self.price_checkbox.pack(expand=False, side="top", anchor="nw", pady=(0, 5))
        self.market_checkbox = ctk.CTkCheckBox(self.frame_checkBoxes, text="Coin's Mrket Cap", font=("Berlin Sans FB Demi", 14))
        self.market_checkbox.pack(expand=False, side="top", anchor="nw", pady=(0, 5))
        self.volume_checkbox = ctk.CTkCheckBox(self.frame_checkBoxes, text="Coin's Volume", font=("Berlin Sans FB Demi", 14))
        self.volume_checkbox.pack(expand=False, side="top", anchor="nw", pady=(0, 5))

        # Frame for direction and format
        self.frame4 = ctk.CTkFrame(self.container)
        self.frame4.pack(expand= True, fill= "both", ipadx=10, ipady=10, pady= (0, 10), padx=(10, 10), side= "top")
        self.direction_lable = ctk.CTkLabel(self.frame4, 
                                  text="Choose File name and path and format ",
                                  font=("Berlin Sans FB Demi", 16))
        self.direction_lable.pack(expand=True, side="left")
        self.direction_entry = ctk.CTkEntry(self.frame4, 
                                         width=200,
                                         font=("Berlin Sans FB Demi", 14),
                                         placeholder_text="File address to save ...")
        self.direction_entry.pack(expand=True, side="left")
        self.format_comboBox = ctk.CTkComboBox(self.frame4, 
                                         values=["xlsx", "csv"],
                                         width=80,
                                         font=("Berlin Sans FB Demi", 14))
        self.format_comboBox.pack(expand=True, side="left")
        self.format_comboBox.set("format")
        self.browser = ctk.CTkButton(self.frame4,
                                 text="Browser...",
                                 font=("Berlin Sans FB Demi", 20),
                                 corner_radius=10,
                                 width= 80,
                                 hover=True,
                                 command= self.path_to_save)
        self.browser.pack(expand=True, side="right")

        # Frame for Button
        self.frame5 = ctk.CTkFrame(self.container)
        self.frame5.pack(expand= True, fill= "both", ipadx=10, ipady=10, pady= (0, 10), padx=(10, 10), side= "top")
        self.button = ctk.CTkButton(self.frame5,
                                 text="Start Scraping",
                                 font=("Berlin Sans FB Demi", 20),
                                 corner_radius=10,
                                 width= 400,
                                 height=80,
                                 hover=True,
                                 hover_color="red",
                                 command= self.start_scraping)
        self.button.pack(expand=True, anchor="center")



    def change_appearance(self):
        if self.mode_switch.get() == 1:
            self._set_appearance_mode("dark")
            self.mode_switch.configure(text= "Dark Mode")
        else:
            self._set_appearance_mode("light")
            self.mode_switch.configure(text= "Light Mode")



    def path_to_save(self):
        file_direction = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                      filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("All files", "*.*")])
        if file_direction:
            self.direction_entry.delete(0, "end")
            self.direction_entry.insert(0, file_direction)

    def start_scraping(self):
        # Get all data from GUI
        url = self.url_comboBox.get()
        pages = int(self.pages_comboBox.get())
        scrap_name = self.name_checkbox.get()
        scrap_price = self.price_checkbox.get()
        scrap_market = self.market_checkbox.get()
        scrap_volume = self.volume_checkbox.get()
        direction = self.direction_entry.get()
        format = self.format_comboBox.get()

        # For https://arzdigital.com/coins/
        if url == "https://arzdigital.com/coins/":
            scraper.arzdigital_scraper(url= url,
                                           pages= pages,
                                           scrap_name= scrap_name,
                                           scrap_price= scrap_price,
                                           scrap_market= scrap_market,
                                           scrap_volume= scrap_volume,
                                           direction= direction,
                                           format= format)


app = ScraperApp()
app.mainloop()