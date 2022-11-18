import random
import tkinter as tk

listintrok = ['人', '男', '女', '子', '日', '月', '時', '水', '火', '土', '風', '空', '山', '川', '木', '花', '雨',
              '雪', '金', '刀']

listintrotrad = ['La personne', "L'homme", 'la femme', "L'enfant", 'Le soleil', 'La lune', 'Le temps', "L'eau",
                 'Le feu', 'La terre, (sur le sol)', 'Le vent', 'Le ciel', 'La montagne', 'La rivière', "L'arbre",
                 'La fleur', 'La pluie', 'La neige', "L'argent (la monnaie)", 'Le sabre']


def get_question(kanjis, trad):
    """
    The get_question function takes two lists as arguments. The first list contains the kanji, and the second list contains their corresponding translations.
    The function then picks a random kanji from the first list, and randomly places its translation in one of four possible positions in a new list called final.
    The position is determined by another random number between 1 and 4 (inclusive). The function returns this new question-and-answer pair.

    :param kanjis: Pick a random kanji from the list of kanji
    :param trad: Get the list of traductions corresponding to a given kanji
    :return: A list of 5 elements: the question, and 4 possible answers
    """
    global final
    final = []  # returned list: question is [0], different awnsers:[2,3,4,5], [1] is where to put the awnser
    testlist = []
    lenlistes = len(kanjis)
    question = random.randint(0, lenlistes - 1)  # pick a kanji in the given list
    testlist.append(question)
    final.append(kanjis[question])
    where = random.randint(1, 4)  # where to put the anwser
    final.append(where)
    for i in range(4):
        if i + 1 == where:
            final.append(trad[question])
            testlist.append(question)
        else:
            condition = True
            while condition:
                tirage = random.randint(0, lenlistes - 1)
                if testlist.count(tirage) == 0:
                    testlist.append(tirage)
                    final.append(trad[tirage])
                    condition = False
    return final


def windowinit():
    return tk.Tk()


def windowparameters():
    window.title('KanjiMaster')
    window.geometry('1280x800')
    window['background'] = '#605B56'


def tomain():
    exitbutton.destroy()
    awnser1.destroy()
    awnser2.destroy()
    awnser3.destroy()
    awnser4.destroy()
    scoretotrad.destroy()
    lostlabel.destroy()
    kanji.destroy()
    mainpage()


def mainpage():
    """
    The mainpage function creates the main page of the program. It displays a greeting and two buttons, one for each other pages.

    :return: The main page of the app
    """
    global greetings
    greetings = tk.Label(
        text='KanjiMaster',
        fg='black',
        bg='#605B56',
        font=('Vivaldi', 68, 'bold'),
        height='2'
    )
    greetings.pack()

    global japanese
    japanese = tk.Label(
        text='漢字のマスター',
        fg='black',
        bg='#605B56',
        font=('Arial', 28, 'italic'),
        height='2'
    )
    japanese.pack()

    global kanjitotrad
    kanjitotrad = tk.Button(text='Find the traduction of the kanjis', font=('Arial', 25), command=pagekanjitotrad)
    kanjitotrad.pack(pady='100')

    global tradtokanji
    tradtokanji = tk.Button(text='Find the kanji of the traduction', font=('Arial', 25), command=pagetradtokanji)
    tradtokanji.pack()


def pagekanjitotrad():
    """
    The pagekanjitotrad (page kanji to trad) function is used to display the kanji, awnsers and exit button.
    It is called when the user clicks on 'Kanji to trad' in the main menu.

    :return: The question, the awnsers and the exit button
    """
    greetings.destroy()
    japanese.destroy()
    kanjitotrad.destroy()
    tradtokanji.destroy()

    questionlist = get_question(listintrok, listintrotrad)

    global scorenumber
    scorenumber = 0
    global lostnumber
    lostnumber = 0

    global kanji
    kanji = tk.Label(
        text=questionlist[0],
        fg='black',
        bg='#605B56',
        font=('Arial', 58),
        height='2'
    )
    kanji.pack(anchor=tk.CENTER)

    global scoretotrad
    scoretotrad = tk.Label(
        text=scorenumber,
        fg='black',
        bg='#605B56',
        font=('Arial', 58),
        height='2'
    )
    scoretotrad.pack(side=tk.LEFT)

    global lostlabel
    lostlabel = tk.Label(
        text=lostnumber,
        fg='black',
        bg='#605B56',
        font=('Arial', 58),
        height='2'
    )
    lostlabel.pack(side=tk.RIGHT)

    global awnser1
    global awnser2
    global awnser3
    global awnser4
    awnser1 = tk.Button(text=questionlist[2], height=2, font=('Arial', 18), command=defawnser1)
    awnser1.pack(pady=25, ipadx=150, anchor=tk.CENTER)
    awnser2 = tk.Button(text=questionlist[3], height=2, font=('Arial', 18), command=defawnser2)
    awnser2.pack(pady=25, ipadx=150, anchor=tk.CENTER)
    awnser3 = tk.Button(text=questionlist[4], height=2, font=('Arial', 18), command=defawnser3)
    awnser3.pack(pady=25, ipadx=150, anchor=tk.CENTER)
    awnser4 = tk.Button(text=questionlist[5], height=2, font=('Arial', 18), command=defawnser4)
    awnser4.pack(pady=25, ipadx=150, anchor=tk.CENTER)

    global exitbutton
    exitbutton = tk.Button(
        text='Quitter',
        command=tomain
    )
    exitbutton.pack(anchor=tk.E, side=tk.BOTTOM, padx=20, pady=20)


def defawnser1():
    if final[1] == 1:
        winner()
    else:
        loser()


def defawnser2():
    if final[1] == 2:
        winner()
    else:
        loser()


def defawnser3():
    if final[1] == 3:
        winner()
    else:
        loser()


def defawnser4():
    if final[1] == 4:
        winner()
    else:
        loser()


def winner():
    global scorenumber
    scorenumber += 1
    scoretotrad.configure(text=scorenumber)
    next_question()


def loser():
    global lostnumber
    lostnumber += 1
    lostlabel.configure(text=lostnumber)
    next_question()


def next_question():
    finalnext = get_question(listintrok, listintrotrad)
    kanji.configure(text=finalnext[0])
    awnser1.configure(text=finalnext[2])
    awnser2.configure(text=finalnext[3])
    awnser3.configure(text=finalnext[4])
    awnser4.configure(text=finalnext[5])


def pagetradtokanji():
    pass


if __name__ == '__main__':
    window = windowinit()
    windowparameters()
    mainpage()
    window.mainloop()
