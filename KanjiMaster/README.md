KanjiMaster is a project made in order to help me learn japanese.
Indeed this project is a quiz where you either have : 
	- a kanji (japanese symbol) and four traduction possibilities
	- a traduction and you have to choose between four kanjis.

This project has an ui wich is made with customtkinter
It uses a database and sqlite3 in order to store and pick all the different kanjis with their traductions
You can choose between (for now) two types of "kanjis" : The basics or the polite ones (cf. https://kakikukeko.fr/)

Until this date (18/11/2022) KanjiMaster still has a lot of bugs.
	- I think the question is not refreshed for whatever reason so it causes a lot of other problems
	- The points score doesn't go to zero when changing of mode (cf. line 2)
