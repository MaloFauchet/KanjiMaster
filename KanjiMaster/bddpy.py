import sqlite3

con = sqlite3.connect("kanjis.db")
cur = con.cursor()

# cur.execute("CREATE TABLE Kanjis(id,kanji,level);")
# cur.execute("CREATE TABLE Traductions(id,traduction);")
# cur.execute("INSERT INTO Kanjis VALUES (0,'人','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (1,'男','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (2,'女','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (3,'子','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (4,'日','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (5,'月','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (6,'時','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (7,'水','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (8,'火','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (9,'土','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (10,'風','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (11,'空','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (12,'山','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (13,'川','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (14,'木','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (15,'花','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (16,'雨','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (17,'雪','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (18,'金','intro')")
# cur.execute("INSERT INTO Kanjis VALUES (19,'刀','intro')")
# cur.execute("INSERT INTO Traductions VALUES (0,'La personne')")
# cur.execute("INSERT INTO Traductions VALUES (1,'Un Homme')")
# cur.execute("INSERT INTO Traductions VALUES (2,'la femme')")
# cur.execute("INSERT INTO Traductions VALUES (3,'Un enfant')")
# cur.execute("INSERT INTO Traductions VALUES (4,'Le soleil')")
# cur.execute("INSERT INTO Traductions VALUES (5,'La lune')")
# cur.execute("INSERT INTO Traductions VALUES (6,'Le temps')")
# cur.execute("INSERT INTO Traductions VALUES (7,'Eau')")
# cur.execute("INSERT INTO Traductions VALUES (8,'Le feu')")
# cur.execute("INSERT INTO Traductions VALUES (9,'La terre, (sur le sol)')")
# cur.execute("INSERT INTO Traductions VALUES (10,'Le vent')")
# cur.execute("INSERT INTO Traductions VALUES (11,'Le ciel')")
# cur.execute("INSERT INTO Traductions VALUES (12,'La montagne')")
# cur.execute("INSERT INTO Traductions VALUES (13,'La rivière')")
# cur.execute("INSERT INTO Traductions VALUES (14,'Un arbre')")
# cur.execute("INSERT INTO Traductions VALUES (15,'La fleur')")
# cur.execute("INSERT INTO Traductions VALUES (16,'La pluie')")
# cur.execute("INSERT INTO Traductions VALUES (17,'La neige')")
# cur.execute("INSERT INTO Traductions VALUES (18,'Argent (la monnaie)')")
# cur.execute("INSERT INTO Traductions VALUES (19,'Le sabre')")
# cur.execute("INSERT INTO Traductions VALUES (20,'Oui')")
# cur.execute("INSERT INTO Traductions VALUES (21,'Non')")
# cur.execute("INSERT INTO Traductions VALUES (22,'S il vous plaît')")
# cur.execute("INSERT INTO Traductions VALUES (23,'Merci (version polie)')")
# cur.execute("INSERT INTO Traductions VALUES (24,'Il n y a pas de quoi')")
# cur.execute("INSERT INTO Traductions VALUES (25,'Bonjour (matin et polie)')")
# cur.execute("INSERT INTO Traductions VALUES (26,'Bonjour (journée)')")
# cur.execute("INSERT INTO Traductions VALUES (27,'Bonsoir')")
# cur.execute("INSERT INTO Traductions VALUES (28,'Comment vas-tu (allez-vous)')")
# cur.execute("INSERT INTO Traductions VALUES (29,'Je vais bien')")
# cur.execute("INSERT INTO Traductions VALUES (30,'Au revoir (adieu)')")
# cur.execute("INSERT INTO Traductions VALUES (31,'Au revoir (à la prochaine)')")
# cur.execute("INSERT INTO Traductions VALUES (32,'Bonne nuit (version polie)')")
# cur.execute("INSERT INTO Traductions VALUES (33,'À demain')")
# cur.execute("INSERT INTO Traductions VALUES (34,'Enchanté')")
# cur.execute("INSERT INTO Traductions VALUES (35,'Enchanté (ravi de faire votre connaissance)')")
# cur.execute("INSERT INTO Traductions VALUES (36,'Je vous en prie (allez-y)')")
# cur.execute("INSERT INTO Traductions VALUES (37,'Bon appétit')")
# cur.execute("INSERT INTO Traductions VALUES (38,'Excuse(z)-moi (pour déranger)')")
# cur.execute("INSERT INTO Traductions VALUES (39,'Pardonne(z)-moi (pour s excuser poliment)')")
# cur.execute("INSERT INTO Traductions VALUES (40,'Bon travail')")
# cur.execute("INSERT INTO Traductions VALUES (41,'J y vais (je quitte la maison)')")
# cur.execute("INSERT INTO Traductions VALUES (42,'Bonne journée (bon départ)')")
# cur.execute("INSERT INTO Traductions VALUES (43,'Je suis rentré (on arrive dans la maison)')")
# cur.execute("INSERT INTO Traductions VALUES (44,'Bon retour')")
# cur.execute("INSERT INTO Traductions VALUES (45,'Bienvenue (magasin)')")
# cur.execute("INSERT INTO Traductions VALUES (46,'Bienvenue (en général)')")
# cur.execute("INSERT INTO Traductions VALUES (47,'Je rentre (je me permets de rentrer chez vous)')")
# cur.execute("INSERT INTO Traductions VALUES (48,'Merci')")
# cur.execute("INSERT INTO Traductions VALUES (49,'Bonjour (matin)')")
# cur.execute("INSERT INTO Traductions VALUES (50,'Bonne nuit')")
# cur.execute("INSERT INTO Traductions VALUES (51,'Pardonne(z)-moi (pour s excuser)')")
# cur.execute("INSERT INTO Kanjis VALUES (20,'はい','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (21,'いいえ','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (22,'お願いします','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (23,'ありがとうございます','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (24,'どういたしまして','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (25,'おはようございます','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (26,'こんにちは','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (27,'こんばんは','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (28,'お元気ですか','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (29,'はい、元気です','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (30,'さようなら','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (31,'またね','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (32,'おやすみなさい','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (33,'また明日','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (34,'初めまして','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (35,'どうぞ宜しくお願いします','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (36,'どうぞ','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (37,'いただきます','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (38,'すみません','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (39,'ごめんなさい','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (40,'お疲れ様でした','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (41,'いってきます','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (42,'いってらっしゃい','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (43,'ただいま','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (44,'おかえりなさい','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (45,'いらっしゃいませ','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (46,'ようこそ','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (47,'お邪魔します','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (48,'ありがとう','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (49,'おはよう','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (50,'おやすみ','politesse')")
# cur.execute("INSERT INTO Kanjis VALUES (51,'ごめん','politesse')")

con.commit()

con.close()

# listpolitessetrad = ['oui', 'non', "s'il vous plaît", 'merci (version polie)', "il n'y a pas de quoi",
#                      'bonjour (matin et polie)', 'bonjour (journée)', 'bonsoir', 'comment vas-tu (allez-vous)',
#                      'je vais bien', 'au revoir (adieu)', 'au revoir (à la prochaine)', 'bonne nuit (version polie)',
#                      'à demain', 'enchanté', 'enchanté (ravi de faire votre connaissance)',
#                      'je vous en prie (allez-y)', 'bon appétit', 'excuse(z)-moi (pour déranger)',
#                      "pardonne(z)-moi (pour s'excuser poliment)", 'bon travail', "j'y vais (je quitte la maison)",
#                      'bonne journée (bon départ)', 'je suis rentré (on arrive dans la maison)', 'bon retour',
#                      'bienvenue (magasin)', 'bienvenue (en général)', 'je rentre (je me permets de rentrer chez vous)',
#                      'merci', 'bonjour (matin)', 'bonne nuit', "pardonne(z)-moi (pour s'excuser)"]
#
# listpolitessejapan = ['はい', 'いいえ', 'お願いします', 'ありがとうございます', 'どういたしまして', 'おはようございます', 'こんにちは', 'お元気ですか', 'はい、元気です',
#                       'さようなら', 'またね', 'おやすみなさい', 'また明日', '初めまして', 'どうぞ宜しくお願いします', 'どうぞ', 'いただきます', 'すみません',
#                       'ごめんなさい', 'お疲れ様でした', 'いってきます', 'いってらっしゃい', 'ただいま', 'おかえりなさい', 'いらっしゃいませ', 'ようこそ', 'お邪魔します',
#                       'ありがとう', 'おはよう', 'おやすみ', 'ごめん']

# listintrok = ['人', '男', '女', '子', '日', '月', '時', '水', '火', '土', '風', '空', '山', '川', '木', '花', '雨', '雪', '金',
#               '刀']
# listintrotrad = ['La personne', "L'homme", 'la femme', "L'enfant", 'Le soleil', 'La lune', 'Le temps', "L'eau",
#                  'Le feu', 'La terre, (sur le sol)', 'Le vent', 'Le ciel', 'La montagne', 'La rivière', "L'arbre",
#                  'La fleur', 'La pluie', 'La neige', "L'argent (la monnaie)", 'Le sabre']
#
# ch = ""
# for i in range(len(listpolitessejapan)):
#     ch = "INSERT INTO Traductions VALUES (" + str(i+20) + ",'" + listpolitessejapan[i] + "," + "'politesse')"
#     print(f'cur.execute("{ch}")')
