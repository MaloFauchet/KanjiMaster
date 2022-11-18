import kanjialgo
import tkinter as tk
import customtkinter as cs  # used to make the window, but cooler
import time

cs.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
cs.set_default_color_theme("kanjimaster.json")  # Themes: "blue" (standard), "green", "dark-blue"


class Kanjimaster(cs.CTk):

    def __init__(self) -> None:
        """
        The __init__ function is called automatically every time the class is being used to create a new object.
        The self parameter is a Python convention and has to be included in every function definition. It refers to the
        object that will be created from the class, and allows an object t access its own members (variables/functions)

        :param self: Refer to the object instance (similar to this in java)
        :return: None, so it is not necessary to specify a return statement
        """
        super(Kanjimaster, self).__init__()

        # Option de la fenêtre
        self.title('KanjiMaster')
        self.geometry('1920x1080')
        self.state('zoomed')
        self.resizable(width=True, height=True)
        # variable pour tk
        self.sous_titre = cs.CTkLabel()
        self.titre = cs.CTkLabel()
        self.kanji_to_trad_button = cs.CTkButton()
        self.trad_to_kanji_button = cs.CTkButton()
        self.parametres = cs.CTkButton()
        self.check1 = cs.CTkCheckBox()
        self.check2 = cs.CTkCheckBox()
        self.question = cs.CTkLabel()
        self.win_count = cs.CTkLabel()
        self.lost_count = cs.CTkLabel()
        self.awnser4 = cs.CTkButton()
        self.awnser3 = cs.CTkButton()
        self.awnser2 = cs.CTkButton()
        self.awnser1 = cs.CTkButton()
        self.exit_button = cs.CTkButton()

        ############################
        self.algo = kanjialgo.KanjiAlgo()
        self.final = []
        ############################
        # pour quitter
        self.bind("<Escape>", quit)
        ############################
        # Démarrage
        self.creer_titres()
        self.creer_bouttons()

    def creer_titres(self) -> None:
        """
        The creer_titres function creates the title and subtitle of the application.
        It is called in __init__.

        :param self: Access the attributes and methods of the class in python
        :return: None
        """
        self.titre = cs.CTkLabel(self, text="KanjiMaster", height=2, text_font=('Vivaldi', 68, 'bold'), bg='#605B56')
        self.titre.pack(pady=50)
        self.sous_titre = cs.CTkLabel(self, text='漢字のマスター', bg='#605B56', text_font=('Arial', 28, 'italic'), height=2)
        self.sous_titre.pack()

    def creer_bouttons(self) -> None:
        """
        The creer_bouttons function creates the buttons that are used to start the game.
        It creates two buttons, one for kanji to trad and another for trad to kanji.
        The function also creates a button that closes the window.

        :param self: Access the attributes and methods of the class in python
        :return: None
        """
        self.kanji_to_trad_button = cs.CTkButton(
            self,
            text='Trouve la bonne traduction',
            text_font=('Arial', 25),
            text_color="black",
            command=lambda: self.quiz(True)
        )
        self.kanji_to_trad_button.pack(pady=100, ipady=10)

        self.trad_to_kanji_button = cs.CTkButton(
            self,
            text='Trouve le bon kanji',
            text_font=('Arial', 25),
            text_color="black",
            command=lambda: self.quiz(False)
        )
        self.trad_to_kanji_button.pack(ipady=10)

        self.parametres = cs.CTkButton(
            self,
            text='Paramètres',
            text_font=('Arial', 20),
            text_color="black",
            command=self.config_menu
        )
        self.parametres.pack(ipady=10, ipadx=30, pady=150)

        self.exit_button = cs.CTkButton(
            text='Quitter',
            text_font=('Arial', 18),
            text_color="black",
            command=self.destroy
        )
        self.exit_button.pack(ipady=5)

    def quitter_main(self) -> None:
        """
        The quitter_main function is used to quit the main menu and start the quiz.
        It destroys all the widgets on screen.

        :param self: Access the attributes and methods of the class in python
        :return: None
        """
        self.titre.destroy()
        self.sous_titre.destroy()
        self.kanji_to_trad_button.destroy()
        self.trad_to_kanji_button.destroy()
        self.parametres.destroy()
        self.exit_button.destroy()

    def quitter_question(self) -> None:
        """
        The quitter_question function is used to destroy the question window and return to the main page.
        It destroys all the widgets on that page.

        :param self: Access the attributes and methods of the class in python
        :return: None
        """
        self.question.destroy()
        self.win_count.destroy()
        self.lost_count.destroy()
        self.awnser1.destroy()
        self.awnser2.destroy()
        self.awnser3.destroy()
        self.awnser4.destroy()
        self.exit_button.destroy()

        # main page
        self.creer_titres()
        self.creer_bouttons()

    def quitter_parametres(self):
        """
        The quitter_parametres function destroys the widgets in the parametres page and returns to
        the main page.

        :param self: Access variables that belongs to the class
        :return: Nothing
        """
        self.titre.destroy()
        self.check1.destroy()
        self.check2.destroy()
        self.exit_button.destroy()

        # main page
        self.creer_titres()
        self.creer_bouttons()

    def config_menu(self):
        """
        The config_menu function is used to configure the kanji categories that will be used in the quiz.
        The user can choose between two pre-defined categories. The function is called when
        the user clicks on 'Paramètres' from the main menu.

        :param self: Access variables that belong to the class
        :return: The checkbox values
        """
        self.quitter_main()

        self.titre = cs.CTkLabel(
            self,
            text="Quelle catégorie(s) de kanji(s) voulez-vous utiliser ?",
            text_font=('Arial', 38)
        )
        self.titre.pack(pady=100, anchor=tk.CENTER)

        self.check1 = cs.CTkCheckBox(
            self,
            text="Kanji d'Introduction",
            text_font=('Arial', 32),
            command=lambda: self.algo.checkbox(0)
        )
        self.check1.pack(padx=20, pady=10)

        self.check2 = cs.CTkCheckBox(
            self,
            text="Politesse",
            text_font=('Arial', 32),
            command=lambda: self.algo.checkbox(1)
        )
        self.check2.pack(padx=20, pady=10)

        # get the state of the checkboxes
        if self.algo.get_checkbox_state(0):
            self.check1.select()
        if self.algo.get_checkbox_state(1):
            self.check2.select()

        self.exit_button = cs.CTkButton(text="Quitter", text_font=('Arial', 18), text_color="black",
                                        command=self.quitter_parametres)
        self.exit_button.pack(padx=100, pady=100)

    def quiz(self, mode) -> None:
        """
        The quiz function is the main function of the game. It is called when a player clicks on 'Jouer' in the menu.
        It creates a new window and displays all relevant information to play, such as:
        - The question itself (in French or Japanese)
        - The 4 possible answers (in French or Japanese)
        - A button to quit the quiz and return to menu.

        :param mode: let know the program if user chose 'kanji to trad'(True) or 'trad to kanjis'(False)
        :param self: Access variables that belongs to the class
        :return: None
        """
        self.quitter_main()
        self.algo.quiz(mode)
        self.final = self.algo.get_question()

        self.question = cs.CTkLabel(self, text=self.final[0], text_font=('Arial', 58), height=2)
        self.question.pack(pady=100, anchor=tk.CENTER)

        self.win_count = cs.CTkLabel(self, text=f"Gagné : {self.algo.get_win_number()}", bg='#605B56', text_font=('Arial', 18),
                                     height=2)
        self.win_count.pack()
        self.lost_count = cs.CTkLabel(self, text=f"Perdu : {self.algo.get_lost_number()}", bg='#605B56', text_font=('Arial', 18),
                                      height=2)
        self.lost_count.pack()

        self.awnser1 = cs.CTkButton(text=self.final[2], height=2, text_color="black", text_font=('Arial', 18),
                                    command=lambda: self.test_awnser(1))
        self.awnser1.pack(pady=30, ipadx=150, ipady=10, anchor=tk.CENTER)
        self.awnser2 = cs.CTkButton(text=self.final[3], height=2, text_color="black", text_font=('Arial', 18),
                                    command=lambda: self.test_awnser(2))
        self.awnser2.pack(pady=30, ipadx=150, ipady=10, anchor=tk.CENTER)
        self.awnser3 = cs.CTkButton(text=self.final[4], height=2, text_color="black", text_font=('Arial', 18),
                                    command=lambda: self.test_awnser(3))
        self.awnser3.pack(pady=30, ipadx=150, ipady=10, anchor=tk.CENTER)
        self.awnser4 = cs.CTkButton(text=self.final[5], height=2, text_color="black", text_font=('Arial', 18),
                                    command=lambda: self.test_awnser(4))
        self.awnser4.pack(pady=30, ipadx=150, ipady=10, anchor=tk.CENTER)

        self.exit_button = cs.CTkButton(text="Quitter", text_font=('Arial', 18), text_color="black",
                                        command=self.quitter_question)
        self.exit_button.pack(padx=100, pady=100)

    def test_awnser(self, button):
        if self.algo.awnser(button):
            self.win_count.configure(text=f"Gagné : {self.algo.get_win_number()}")
        else:
            self.lost_count.configure(text=f"Perdu : {self.algo.get_lost_number()}")
        self.next_question()

    def next_question(self) -> None:
        """
        The next_question function is used to display the next question in the game.
        It takes no arguments and returns nothing.

        :param self: Access variables that belongs to the class
        :return: None
        """
        self.final = self.algo.get_question()
        self.question.configure(text=self.final[0])
        self.awnser1.configure(text=self.final[2])
        self.awnser2.configure(text=self.final[3])
        self.awnser3.configure(text=self.final[4])
        self.awnser4.configure(text=self.final[5])


if __name__ == "__main__":
    debut = time.time()
    app = Kanjimaster()
    print(time.time() - debut)
    app.mainloop()
