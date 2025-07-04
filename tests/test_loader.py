import functionwords as fw

print("Jeux dispo :", fw.available_ids())
fr = fw.load("fr_21c")
print(len(fr.all), "mots outils - français contemporain")
print("'ne' in set ?", 'ne' in fr.all)
subset = fr.subset(["articles", "prepositions"])
print("articles+prépositions :", len(subset))
