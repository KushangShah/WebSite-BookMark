import customtkinter as ctk
import webbrowser

# App
class Bookmark(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Title
        self.title("WebPage Bookmark")
        self.geometry("600x500")

        # Creating a frame
        self.frame = ctk.CTkFrame(self)
        self.frame.grid(row=0, column=0, padx=5, pady=5)

        # Label
        self.label = ctk.CTkLabel(self.frame, text="Click the button to open a webpage", font=("Arial", 16))
        self.label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # Buttons
        self.button1 = ctk.CTkButton(self.frame, text="RPS", font=("Arial", 20), command=self.yoututbe_video_downloader)
        self.button1.grid(row=1, column=0, padx=20, pady=15)
        
        self.button2 = ctk.CTkButton(self.frame, text="Heart Disease Prediction", font=("Arial", 20), command=self.heart_disease_prediction)
        self.button2.grid(row=1, column=1, padx=20, pady=15)
        
        self.button3 = ctk.CTkButton(self.frame, text="IP Address", font=("Arial", 20), command=self.ip_address)
        self.button3.grid(row=1, column=2, padx=20, pady=15)
        
        self.button4 = ctk.CTkButton(self.frame, text="Auto Search", font=("Arial", 20), command=self.auto_search_on_browser)
        self.button4.grid(row=2, column=0, padx=20, pady=15)
        
        self.button5 = ctk.CTkButton(self.frame, text="Rock Paper Scissor", font=("Arial", 20), command=self.rock_paper_scissor)
        self.button5.grid(row=2, column=1, padx=20, pady=15)
        
        self.button6 = ctk.CTkButton(self.frame, text="Age calculator", font=("Arial", 20), command=self.age_calculator)
        self.button6.grid(row=2, column=2, padx=20, pady=15)
        
        self.button7 = ctk.CTkButton(self.frame, text="Pancreatic cancer prediction", font=("Arial", 20), command=self.pancreatic_cancer_prediction)
        self.button7.grid(row=3, column=0, padx=20, pady=15)
        
    # open link on new page
    def yoututbe_video_downloader(self):
        webbrowser.open_new_tab("https://github.com/KushangShah/Youtube_Video_Downloder")

    def heart_disease_prediction(self):
        webbrowser.open_new_tab("https://github.com/KushangShah/AlmaBetter-Projects/tree/main/Module%206%20Machine%20Learning/6%20Mid%20Course")

    def ip_address(self):
        webbrowser.open_new_tab("https://github.com/KushangShah/IP-Address-Featch")

    def auto_search_on_browser(self):
        webbrowser.open_new_tab("https://github.com/KushangShah/Auto-Search-on-Browser")

    def rock_paper_scissor(self):
        webbrowser.open_new_tab("https://github.com/KushangShah/Rock-Paper-Scissor")

    def age_calculator(self):
        webbrowser.open_new_tab("https://github.com/KushangShah/Age-Calculator")

    def pancreatic_cancer_prediction(self):
        webbrowser.open_new_tab("https://github.com/KushangShah/Pancreatic-Cancer-Prediction")
    
        
# Run the app
if __name__ == "__main__":
    app = Bookmark()
    app.mainloop()
