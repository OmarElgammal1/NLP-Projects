import example
import tkinter
import tkinter.messagebox
import customtkinter

# INSERT YOUR MODEL'S NAME HERE
MODELS = ['NLP 1', 'NLP 2', 'NLP 3', 'NLP 4', 'NLP 5']

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("NLP Text Classification")
        self.geometry(f"{1100}x{580}")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=1060, height=500, command=self.eventTabChange)
        self.tabview.place(x=20, y=10)
        self.tabview.add(MODELS[0])
        self.tabview.add(MODELS[1])
        self.tabview.add(MODELS[2])
        self.tabview.add(MODELS[3])
        self.tabview.add(MODELS[4])
        # self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        # self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        self.tabviewEntries = []
        for i in range(5):
            self.tabviewEntries.append(customtkinter.CTkTextbox(self.tabview.tab(MODELS[i]), width=1030, height=445))
            self.tabviewEntries[i].place(x=10, y=0)

        self.predict_button = customtkinter.CTkButton(self, text="Predict", command=self.eventPredict, width=150, height=40)
        self.predict_button.place(x=930, y=520)

    def eventTabChange(self):
        print(f"Tab changed to {self.tabview.get()} with index {self.tabview.index(self.tabview.get())}")

    def eventPredict(self):
        print(f"Predict button pressed in tab: {self.tabview.get()}, index: {self.tabview.index(self.tabview.get())}")
        example.predict(self.tabviewEntries[self.tabview.index(self.tabview.get())].get('0.0', 'end'))


if __name__ == "__main__":
    app = App()
    app.mainloop()