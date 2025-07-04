import functionwords as fw

print("Jeux dispo :", fw.available_ids())      # A terme: ['fr_21c', 'en_17c', 'it_19c']
fr = fw.load("fr_21c")
print(len(fr.all), "mots français modernes")
print("'ne' in set ?", 'ne' in fr.all)
subset = fr.subset(["articles", "prepositions"])
print("articles+prépositions :", len(subset))
