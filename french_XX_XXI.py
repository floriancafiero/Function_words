# -*- coding: utf-8 -*-
"""
Extended list of French function words (stop-words), organised by morpho-syntactic type.


from __future__ import annotations

# ---------------------------------------------------------------------------
# Determiners
# ---------------------------------------------------------------------------

ARTICLES_DETERMINERS = frozenset([
    # définis / indéfinis / partitifs
    "le", "la", "l'", "les",
    "un", "une", "des",
    "du", "de la", "de l'",
    "au", "aux",
    # démonstratifs / interrogatifs
    "ce", "cet", "cette", "ces",
    "quel", "quelle", "quels", "quelles",
    # quantifieurs
    "chaque",
    "tout", "toute", "tous", "toutes",
    "quelque", "quelques",
    "aucun", "aucune",
    "certain", "certaine", "certains", "certaines",
    "plusieurs",
    "autre", "autres"
])

POSSESSIVE_DETERMINERS = frozenset([
    "mon", "ma", "mes",
    "ton", "ta", "tes",
    "son", "sa", "ses",
    "notre", "nos",
    "votre", "vos",
    "leur", "leurs"
])

# ---------------------------------------------------------------------------
# Pronouns
# ---------------------------------------------------------------------------

PERSONAL_PRONOUNS = frozenset([
    "je", "j'", "tu", "il", "elle", "on",
    "nous", "vous", "ils", "elles",
    # clitiques
    "me", "m'", "te", "t'", "se", "s'",
    "le", "la", "l'", "les", "lui", "leur",
    "y", "en",
    # toniques
    "moi", "toi", "lui", "elle", "nous", "vous", "eux", "elles"
])

POSSESSIVE_PRONOUNS = frozenset([
    "le mien", "la mienne", "les miens", "les miennes",
    "le tien", "la tienne", "les tiens", "les tiennes",
    "le sien", "la sienne", "les siens", "les siennes",
    "le nôtre", "la nôtre", "les nôtres",
    "le vôtre", "la vôtre", "les vôtres",
    "le leur", "la leur", "les leurs"
])

DEMONSTRATIVE_PRONOUNS = frozenset([
    "ce", "cela", "ça", "ceci",
    "celui", "celle", "ceux", "celles",
    "celui-ci", "celle-ci", "ceux-ci", "celles-ci",
    "celui-là", "celle-là", "ceux-là", "celles-là"
])

INDEFINITE_PRONOUNS = frozenset([
    "chacun", "chacune", "aucun", "aucune",
    "tout", "tous", "toutes",
    "autre", "autres",
    "on",
    "quelqu'un", "quelqu’une", "quelques-uns", "quelques-unes",
    "quelque chose", "rien", "personne",
    "plusieurs",
    "nul", "nulle",
    "autrui"
])

INTERROGATIVE_PRONOUNS = frozenset([
    "qui", "que", "quoi",
    "lequel", "laquelle", "lesquels", "lesquelles",
    "auquel", "auxquels", "auxquelles",
    "duquel", "desquels", "desquelles"
])

# ---------------------------------------------------------------------------
# Prepositions (simple & complex)
# ---------------------------------------------------------------------------

PREPOSITIONS = frozenset([
    # simples
    "à", "de", "dans", "en", "par", "pour", "sans", "sur", "sous",
    "chez", "avec", "entre", "contre", "vers", "selon", "parmi", "via",
    "après", "avant", "depuis", "pendant", "durant", "dès", "lors", "grâce",
    "derrière", "devant", "autour", "hors", "jusque", "jusqu'",
    "dessous", "dessus", "outre",
    # composées fréquentes (restent un seul token si on ne scinde pas sur l’espace)
    "à travers", "vis-à-vis", "auprès de", "quant à", "loin de", "près de"
])

# ---------------------------------------------------------------------------
# Conjunctions & complementisers
# ---------------------------------------------------------------------------

COORD_CONJUNCTIONS = frozenset(["et", "ou", "ni", "mais", "donc", "or", "car"])

SUBORD_CONJUNCTIONS = frozenset([
    "que", "si", "comme", "lorsque", "quand", "puisque",
    "parce que", "alors que", "tandis que",
    "bien que", "quoique", "afin que", "pour que", "de sorte que",
    "avant que", "après que", "dès que", "tant que", "autant que",
    "même si", "sans que",
    "à moins que", "à condition que", "pourvu que",
    "vu que", "attendu que", "dans la mesure où", "comme si"
])

# ---------------------------------------------------------------------------
# Adverbs
# ---------------------------------------------------------------------------

ADVERBS = frozenset([
    # lieu
    "ici", "là", "ailleurs", "partout", "dedans", "dehors",
    # temps
    "aujourd'hui", "hier", "demain", "toujours", "souvent", "parfois",
    "rarement", "jamais", "déjà", "encore", "tôt", "tard",
    # manière / quantité
    "bien", "mal", "mieux", "pis",
    "très", "trop", "assez", "peu", "moins", "davantage", "autant",
    "presque", "quasiment", "simplement", "seulement", "largement",
    "à peine", "beaucoup", "tant", "tellement",
    # affirmation / négation / doute
    "oui", "si", "non", "peut-être",
    # liaison / discours
    "ainsi", "alors", "puis", "ensuite", "cependant", "pourtant",
    "toutefois", "d'ailleurs", "enfin", "bref", "après",
    "aussi"  # adverbe pouvant jouer le rôle de conjonction corrélative
])

# ---------------------------------------------------------------------------
# Negatives
# ---------------------------------------------------------------------------

NEGATIONS = frozenset([
    "ne", "n'", "n",
    "pas", "plus", "jamais", "rien", "personne",
    "guère", "aucun", "aucune",
    "nul", "nulle", "nullement",
    "sans",      # préposition mais marque souvent la négation
    "ni",
    # locutions fréquentes
    "nulle part", "pas du tout", "plus jamais"
])

# ---------------------------------------------------------------------------
# Auxiliaries & modals
# ---------------------------------------------------------------------------

AUX_ETRE = frozenset([
    "être", "étant", "été",
    "suis", "es", "est", "sommes", "êtes", "sont",
    "étais", "était", "étions", "étiez", "étaient",
    "fus", "fut", "fûmes", "fûtes", "furent",
    "serai", "seras", "sera", "serons", "serez", "seront",
    "serais", "serait", "serions", "seriez", "seraient",
    "sois", "soit", "soyons", "soyez", "soient",
    "fusse", "fusses", "fût", "fussions", "fussiez", "fussent"
])

AUX_AVOIR = frozenset([
    "avoir", "ayant", "eu",
    "ai", "as", "a", "avons", "avez", "ont",
    "avais", "avait", "avions", "aviez", "avaient",
    "eus", "eut", "eûmes", "eûtes", "eurent",
    "aurai", "auras", "aura", "aurons", "aurez", "auront",
    "aurais", "aurait", "aurions", "auriez", "auraient",
    "aie", "aies", "ait", "ayons", "ayez", "aient",
    "eusse", "eusses", "eût", "eussions", "eussiez", "eussent"
])

MODAL_VERBS = frozenset([
    # infinitifs
    "pouvoir", "devoir", "vouloir", "savoir", "falloir", "aller", "venir",
    # présent (formes clés)
    "peux", "peut", "peuvent",
    "dois", "doit", "doivent",
    "veux", "veut", "veulent",
    "sais", "sait", "savent",
    "faut",
    "vais", "va", "vont",
    "viens", "vient", "viennent"
])

# ---------------------------------------------------------------------------
# Master dict
# ---------------------------------------------------------------------------

FUNCTION_WORDS: dict[str, frozenset[str]] = {
    "articles": ARTICLES_DETERMINERS,
    "poss_det": POSSESSIVE_DETERMINERS,
    "pers_pron": PERSONAL_PRONOUNS,
    "poss_pron": POSSESSIVE_PRONOUNS,
    "dem_pron": DEMONSTRATIVE_PRONOUNS,
    "indef_pron": INDEFINITE_PRONOUNS,
    "inter_pron": INTERROGATIVE_PRONOUNS,
    "prepositions": PREPOSITIONS,
    "coord_conj": COORD_CONJUNCTIONS,
    "subord_conj": SUBORD_CONJUNCTIONS,
    "adverbs": ADVERBS,
    "negations": NEGATIONS,
    "aux_être": AUX_ETRE,
    "aux_avoir": AUX_AVOIR,
    "modals": MODAL_VERBS
}

# ---------------------------------------------------------------------------
# Convenience flat set
# ---------------------------------------------------------------------------

ALL_FUNCTION_WORDS = frozenset().union(*FUNCTION_WORDS.values())

if __name__ == "__main__":
    print("Total function word types :", len(ALL_FUNCTION_WORDS))
    for k, v in FUNCTION_WORDS.items():
        print(f"{k:>14}: {len(v):3}")
