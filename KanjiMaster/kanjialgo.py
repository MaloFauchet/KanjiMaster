from random import randint
import sqlite3


class KanjiAlgo:
    def __init__(self):
        # variable pour quiz
        self.win_number = 0
        self.lost_number = 0
        self.wanted = [True, True]  # list of kanjis wanted
        self.configkanji = ""  # used in the sql request to confine to the kanjis wanted
        self.testkanji = -1  # last question used to not have repetition
        self.final = []  # returned list: question is [0], different awnsers:[2,3,4,5], [1] is where to put the awnser
        self.who = True  # keeps track of wich mode you're in (true equals kanji_to_trad)
        # base de donnee
        self.con = sqlite3.connect("kanjis.db")
        self.cur = self.con.cursor()
        self.count = self.cur.execute("SELECT MAX(id) FROM Kanjis")
        self.idnumber = int(str(self.count.fetchone())[1:-2])

    def checkbox(self, number):
        self.wanted[number] = not self.wanted[number]

    def get_checkbox_state(self, number):
        return self.wanted[number]

    def quiz(self, mode) -> None:
        """
        The quiz function is the main function of the game. It is called when a player clicks on 'Jouer' in the menu.
        It creates a new window and displays all relevant information to play, such as:
        - The question itself (in French)
        - The 4 possible answers (in French)
        - A button to quit the quiz and return to menu.

        :param self: Access variables that belongs to the class
        :param mode: Know if the user chose 'kanji to trad' or 'trad to kanji'
        :return: None
        """
        self.configkanji = ""
        if self.wanted[0]:
            self.configkanji = "\'intro\'"
        if self.wanted[1]:
            if self.configkanji == "":
                self.configkanji = "\'politesse\'"
            else:
                self.configkanji += " OR level=\'politesse\'"

        self.who = mode

    def get_question(self) -> list:
        """
        The get_question method is a method that will create a list of 5 elements.
        The first element is the question, either in kanji or a traduction depending on the parameter who.
        The second element is an integer between 1 and 4 which represents where to put the answer (in order).
        The third to fifth elements are potential answers, both  kanji or traduction depending on who as well.

        :param self: Give the object access to its own attributes
        :return: None
        """
        self.final = []  # returned list: question is [0], different awnsers:[2,3,4,5], [1] is where to put the awnser
        testlist = []
        lenlistes = self.idnumber
        question = -1

        while question == self.testkanji:
            res = self.cur.execute(f"SELECT MAX(id) FROM Kanjis WHERE level={self.configkanji}")
            resultat = str(res.fetchone())
            resultat = resultat[1:-2]
            question = randint(0, int(resultat))  # pick a kanji in the given list

        self.testkanji = question
        testlist.append(question)

        if self.who:
            print(f"SELECT kanji FROM Kanjis WHERE (id={question} AND level={self.configkanji})")
            res = self.cur.execute(f"SELECT kanji FROM Kanjis WHERE (id={question} AND level={self.configkanji})")
            self.final.append(res.fetchone())
            where = randint(1, 4)  # where to put the anwser
            self.final.append(where)

            for i in range(4):
                if i + 1 == where:
                    res = self.cur.execute(f"SELECT traduction FROM Traductions WHERE id={question}")
                    resultat = str(res.fetchone())
                    if resultat.startswith('('):
                        resultat = resultat[2:-3]
                    self.final.append(resultat)
                    testlist.append(question)
                else:
                    condition = True
                    while condition:
                        tirage = randint(0, lenlistes)
                        if testlist.count(tirage) == 0:
                            testlist.append(tirage)
                            res = self.cur.execute(f"SELECT traduction FROM Traductions WHERE id={tirage}")
                            resultat = str(res.fetchone())
                            if resultat.startswith('('):
                                resultat = resultat[2:-3]
                            self.final.append(resultat)
                            condition = False
        else:
            res = self.cur.execute(f"SELECT traduction FROM Traductions WHERE id={question}")
            resultat = str(res.fetchone())
            if resultat.startswith('('):
                resultat = resultat[2:-3]

            self.final.append(resultat)
            where = randint(1, 4)  # where to put the anwser
            self.final.append(where)

            for i in range(4):
                if i + 1 == where:
                    res = self.cur.execute(f"SELECT kanji FROM Kanjis WHERE (id={question} AND level={self.configkanji})")
                    resultat = str(res.fetchone())
                    if resultat.startswith('('):
                        resultat = resultat[2:-3]

                    self.final.append(resultat)
                    testlist.append(question)
                else:
                    condition = True

                    while condition:
                        tirage = randint(0, lenlistes)
                        if testlist.count(tirage) == 0:
                            testlist.append(tirage)
                            res = self.cur.execute(f"SELECT kanji FROM Kanjis WHERE id={tirage}")
                            resultat = str(res.fetchone())
                            if resultat.startswith('('):
                                resultat = resultat[2:-3]
                            self.final.append(resultat)
                            condition = False
        print(self.final)

        return self.final

    def awnser(self, awnser) -> bool:
        """
        The defawnser1 function is called when the player chooses the first awnser.
        It checks if the player made the right choice by comparid with the second element of the 'final' list.

        :param awnser: wich button was pressed
        :param self: Access the attributes and methods of the class in python
        :return: None
        """
        if self.final[1] == awnser:
            self.winner()
            return True
        else:
            self.loser()
            return False

    def winner(self) -> None:
        """
        The winner function is called when the user wins a question.
        It adds 1 to the win_number attribute, which is used to count how many questions have been answered correctly.

        :param self: Access variables that belongs to the class
        :return: None
        """
        self.win_number += 1

    def get_win_number(self) -> int:
        return self.win_number

    def loser(self) -> None:
        """
        The loser function is called when the user loses a question.
        It adds 1 to the lost_number attribute, which is used to count how many questions have been answered incorrectly.

        :param self: Access the attributes and methods of the class in python
        :return: None
        """
        self.lost_number += 1

    def get_lost_number(self) -> int:
        return self.lost_number
