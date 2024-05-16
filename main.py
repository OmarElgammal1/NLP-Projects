import example
import tkinter
import tkinter.messagebox
import customtkinter

# INSERT YOUR MODEL'S NAME HERE
MODELS = ['Twitter Sentiment Analysis', 'Movie Review Sentiment Analysis']
MODELCORRESPONDING = ['twitter', 'movie']

MODELRESULTINTERPRETATION = [['Negative 😓', 'Neutral 😑', 'Positive 😁'],[]]

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("NLP Text Classification")
        self.geometry(f"{1100}x{580}")
        self.TLWindow = None
        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=1060, height=500, command=self.eventTabChange)
        self.tabview.place(x=20, y=10)
        self.tabview.add(MODELS[0])
        self.tabview.add(MODELS[1])
        # self.tabview.add(MODELS[2])
        # self.tabview.add(MODELS[3])
        # self.tabview.add(MODELS[4])
        # self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        # self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        self.tabviewEntries = []
        self.checkBoxChoicesCorressponding = [['nb', 'rf', 'dt', 'knn', 'lg'], []]
        self.checkBoxChoices = [
            ['Naive Bayes', 'Random Forest', 'Decision Tree', 'KNN', 'Logistic\nRegression'],
            []
        ]
        for i in range(len(MODELS)):
            self.tabviewEntries.append(customtkinter.CTkTextbox(self.tabview.tab(MODELS[i]), width=870, height=445))
            self.tabviewEntries[i].place(x=10, y=0)

        # self.

            for j in range(len(self.checkBoxChoices[i])):
                self.checkBoxChoices[i].append(customtkinter.CTkCheckBox(self.tabview.tab(MODELS[i]), text=self.checkBoxChoices[i][j], font=("Arial", 16), height=40, width = 100))
                self.checkBoxChoices[i][-1].place(x=900, y=10 + 95*j)


        self.predict_button = customtkinter.CTkButton(self, text="Predict", command=self.eventPredict, width=150, height=40)
        self.predict_button.place(x=930, y=520)

    def eventTabChange(self):
        print(f"Tab changed to {self.tabview.get()} with index {self.tabview.index(self.tabview.get())}")

    def eventPredict(self):
        print(f"Predict button pressed in tab: {self.tabview.get()}, index: {self.tabview.index(self.tabview.get())}")
        modelIndex = self.tabview.index(self.tabview.get())
        dataset_name = MODELCORRESPONDING[modelIndex]
        results = []
        for i in range(len(self.checkBoxChoicesCorressponding[modelIndex])):
            if self.checkBoxChoices[modelIndex][i+5].get() == 1:
                results.append(example.predict(self.tabviewEntries[modelIndex].get('0.0', 'end'), self.checkBoxChoicesCorressponding[modelIndex][i], dataset_name))
        results = [i[0] for i in results]
        print(results)
        # example.predict(self.tabviewEntries[self.tabview.index(self.tabview.get())].get('0.0', 'end'), 'rf', dataset_name)
        self.buildTopWindow()
        self.TLWindow.focus()


    def buildTopWindow(self):
        if self.TLWindow is None or not self.TLWindow.winfo_exists():
            self.TLWindow = customtkinter.CTkToplevel(self, width=400, height=200)
        else:
            self.TLWindow.focus()


if __name__ == "__main__":
    app = App()
    app.mainloop()