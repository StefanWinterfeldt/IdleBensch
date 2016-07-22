Was ist Idle Bensch?
====================
Idle Bensch ist ein wirsches kleines Idle Game - ein Geburtstagsgeschenk für [Bensch](https://www.youtube.com/channel/UCou2p403BI2j9cgvy3SN3Tg).
Nach dem Live-Stream und den Folgen auf Bensch's Channel haben sich viele gewünscht das Spiel selbst zu spielen - hier ist es :)
Das Spiel ist Open Source und steht unter GPLv3.

Wie kriege ich das Spiel zum laufen?
====================================
Ihr braucht:

 * [Python 2.7.x](https://www.python.org/downloads/)
 * [Pygame 1.9.1 für Python 2.7](http://www.pygame.org/download.shtml)
 * Eine Bildschirmauflösung von 1920*1080 Pixeln (das Spiel sollte zwar auch auf anderen Auflösungen starten, aber ich gehe davon aus dass es dann entweder sehr seltsam aussieht oder völlig unbenutzbar wird)

Ich habe das Spiel nur auf Windows getestet, es sollte aber auch auf Linux und Mac laufen.
Wenn ihr Idle Bensch runtergeladen und Python und Pygame installiert habt müsst ihr (auf Windows) nur die run.py doppelklicken.
Falls das nicht funktioniert solltet ihr versuchen über die Kommandozeile zu starten, indem ihr:

 * In der Windows-Suche 'cmd' eingebt - das Öffnet die Kommandozeile
 * in den IdleBensch Ordner navigiert 'cd Pfad/zu/IdleBensch'
 * und den Befehl 'X:\Pfad\zu\python2.7\python.exe run.py' ausführt
 * dabei müsst ihr Pfade mit den jeweiligen Verzeichnissen ersetzen in die ihr Python installiert bzw. Idle Bensch kopiert habt

Was kann ich noch mit dem Spiel machen?
=======================================
Idle Bensch steht unter GPLv3 d.h. grob gesagt und ohne Anspruch auf Vollständigkeit, dass ihr den Quellcode frei verwenden, kopieren, modifizieren und weiter verteilen könnt,
dabei müssen allerdings alle Änderungen wieder unter der GPL veröffentlicht werden.
Außerdem bin ich nicht dafür verantwortlich falls Idle Bensch eure Festplatte frisst oder ein Bewusstsein entwickelt und die Weltherrschaft an sich reißt.
Detailliertere Informationen zur GPLv3 findet ihr [hier](https://www.gnu.org/licenses/quick-guide-gplv3.de.html).

Und sonst?
==========
Das Spiel speichert alle 5 Minuten automatisch, dabei kann es zu Lags kommen. Wenn ihr komplett von vorn beginnen wollt, müsst die den Spielstand (im saveGames Ordner) löschen.
Ich hatte Spaß dabei Idle Bensch zu entwickeln und habe viel mit verschiedenen Konzepten experimentiert, dementsprechend sieht der Quellcode aus :) Ursprünglich hatte ich auch doppelt so viele Upgrades geplant,
aber das Spiel musste rechtzeitig zu Benschs Geburtstag fertig werden und ich hatte keinen Bock noch mehr Icons zu zeichnen.
Im tools Ordner findet sich die Datei 'simulate.py' sie ist ausführbar und simuliert einen kompletten Durchlauf des Spiels innerhalb von ein paar Minuten, anschließend wird angezeigt wie viel Zeit zwischen dem Kauf von Upgrades vergeht.
Ich habe dieses Tool geschrieben um mir das Balancing zu vereinfachen, alles immer wieder manuell durchzuspielen ist nicht drin.

---

What is Idle Bensch?
====================
Idle Bensch is a weird little Idle Game - a birthday present for [Bensch](https://www.youtube.com/channel/UCou2p403BI2j9cgvy3SN3Tg).
After watching the live stream and the episodes on Bensch's channel, lots of his fans wanted to play the game for themselves - here it is :)
The game is Open Source and licensed under GPLv3.

How do I start the game?
========================
You will need:

 * [Python 2.7.x](https://www.python.org/downloads/)
 * [Pygame 1.9.1 für Python 2.7](http://www.pygame.org/download.shtml)
 * A resolution of 1920*1080 pixels (the game should start on other resolutions, but I assume that it will either look strange or be completely unusable)

I tested this game on Windows only but it should work on Linux and Mac as well.
After downloading Idle Bensch and installing Python and Pygame, the game should run just by double clicking the 'run.py' file.
If that fails you should try the command line:

 * In Windows-Search type 'cmd' to open the command line
 * navigate to the IdleBensch folder 'cd path/to/IdleBensch'
 * type in the command 'X:\Pfad\zu\python2.7\python.exe run.py' and execute it
 * the paths in that command need to be replaced by the folders you installed Python and copied Idle Bensch into respectively

What else can I do with this game?
==================================
Idle Bensch is licensed under GLPv3, that means - roughly speaking and without claiming to be exhaustive - you can use, copy, modify and share in whatever way you want, provided all changes are again released unter GPL.
I am also not responsible if Idle Bensch decides to eat your hard drive or becomes conscious and takes over the world.
More detailed Information about the GPL can be found [here](https://www.gnu.org/licenses/quick-guide-gplv3.en.html).

What else?
==========
The game will autosave every 5 minutes, which can cause lags. If you want to start all over again you will need to delete the save file in the saveGames folder.
I had a lot of fun making Idle Bensch and experimented with a lot of different concepts within it, you may notice it in the source code :) Initially I planned on having double the upgrades
but the game had to be ready for Bensch's birthday and I was bored of drawing icons.
In the tools folder you will find 'simulate.py', an executable script that simulates a complete playthrough within a few minutes and show data about the time intervals between upgrades
I wrote this tool to help me with the balancing, manual playthroughs would have taken waaaaay too long.
