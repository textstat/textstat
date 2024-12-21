SHORT_TEXT = "Cool dogs wear da sunglasses."

PUNCT_TEXT = """
I said: 'This is a test sentence to test the remove_punctuation function.
It's short and not the work of a singer-songwriter. But it'll suffice.'
Your answer was: "I don't know. If I were you I'd write a test; just to make
sure, you're really just removing the characters you want to remove!" Didn't
"""

PUNCT_TEXT_RESULT_W_APOSTR = """
I said This is a test sentence to test the remove_punctuation function
It's short and not the work of a singersongwriter But it'll suffice
Your answer was I don't know If I were you I'd write a test just to make
sure you're really just removing the characters you want to remove Didn't
"""

PUNCT_TEXT_RESULT_WO_APOSTR = """
I said This is a test sentence to test the remove_punctuation function
Its short and not the work of a singersongwriter But itll suffice
Your answer was I dont know If I were you Id write a test just to make
sure youre really just removing the characters you want to remove Didnt
"""

LONG_TEXT = (
    "Playing ... games has always been thought to be "
    "important to the development of well-balanced and "
    "creative children; however, what part, if any, "
    "they should play in the lives of adults has never "
    "been researched that deeply. I believe that "
    "playing games is every bit as important for adults "
    "as for children. Not only is taking time out to "
    "play games with our children and other adults "
    "valuable to building interpersonal relationships "
    "but is also a wonderful way to release built up "
    "tension.\n"
    "There's nothing my husband enjoys more after a "
    "hard day of work than to come home and play a game "
    "of Chess with someone. This enables him to unwind "
    "from the day's activities and to discuss the highs "
    "and lows of the day in a non-threatening, kick back "
    "environment. One of my most memorable wedding "
    "gifts, a Backgammon set, was received by a close "
    "friend. I asked him why in the world he had given "
    "us such a gift. He replied that he felt that an "
    "important aspect of marriage was for a couple to "
    "never quit playing games together. Over the years, "
    "as I have come to purchase and play, with other "
    "couples & coworkers, many games like: Monopoly, "
    "Chutes & Ladders, Mastermind, Dweebs, Geeks, & "
    "Weirdos, etc. I can reflect on the integral part "
    "they have played in our weekends and our "
    '"shut-off the T.V. and do something more '
    'stimulating" weeks. They have enriched my life and '
    "made it more interesting. Sadly, many adults "
    "forget that games even exist and have put them "
    "away in the cupboards, forgotten until the "
    "grandchildren come over.\n"
    "All too often, adults get so caught up in working "
    "to pay the bills and keeping up with the "
    '"Joneses\'" that they neglect to harness the fun '
    "in life; the fun that can be the reward of "
    "enjoying a relaxing game with another person. It "
    'has been said that "man is that he might have '
    'joy" but all too often we skate through life '
    "without much of it. Playing games allows us to: "
    "relax, learn something new and stimulating, "
    "interact with people on a different more "
    "comfortable level, and to enjoy non-threatening "
    "competition. For these reasons, adults should "
    "place a higher priority on playing games in their "
    "lives"
)

EASY_TEXT = (
    "Anna and her family love doing puzzles. Anna is best at "
    "little puzzles. Anna and her brother work on medium size "
    "puzzles together. Anna's Brother likes puzzles with cars "
    "in them. When the whole family does a puzzle, they do really "
    "big puzzles. It can take them a week to finish a really "
    "big puzzle. Last year they did a puzzle with 500 pieces! "
    "Anna tries to finish one small puzzle a day by her. "
    "Her puzzles have about 50 pieces. They all glue their "
    "favorite puzzles together and frame them. The puzzles look "
    "so nice on the wall."
)

LONG_SPANISH_TEXT = (
    "Muchos años después, frente al pelotón de fusilamiento, "
    "el coronel Aureliano Buendía había de recordar aquella "
    "tarde remota en que su padre lo llevó a conocer el hielo. "
    "Macondo era entonces una aldea de veinte casas de barro y "
    "cañabrava construidas a la orilla de un río de aguas "
    "diáfanas que se precipitaban por un lecho de piedras pulidas, "
    "blancas y enormes como huevos prehistóricos. El mundo era tan "
    "reciente, que muchas cosas carecían de nombre, y para mencionarlas "
    "había que señalarlas con el dedo. Todos los años, por el mes de marzo, "
    "una familia de gitanos desarrapados plantaba su carpa cerca "
    "de la aldea, y con un grande alboroto de pitos y timbales daban a "
    "conocer los nuevos inventos. Primero llevaron el imán. "
    "Un gitano corpulento, de barba montaraz y manos de gorrión, que se "
    "presentó con el nombre de Melquíades, hizo una truculenta demostración "
    "pública de lo que él mismo llamaba la octava maravilla de "
    "los sabios alquimistas de Macedonia."
)

EASY_SPANISH_TEXT = "Hoy es un lindo día"

LONG_RUSSIAN_TEXT_GUILLEMETS = (
    "Игра ... игры всегда считались важными для развития "
    "уравновешенных и творческих детей; однако, какую роль "
    "они должны играть в жизни взрослых, если таковая имеется, "
    "никогда не исследовалась так глубоко. Я считаю, "
    "что игры для взрослых не менее важны, чем для детей. "
    "Выделение времени для игр с нашими детьми и другими "
    "взрослыми не только ценно для построения межличностных "
    "отношений, но также является прекрасным способом снять "
    "накопившееся напряжение.\n"
    "Ничто не доставляет такого же удовольствие для моего мужа "
    "после тяжелого рабочего дня, как прийти домой и поиграть "
    "с кем-нибудь в шахматы. Это позволяет ему расслабиться от "
    "повседневных дел и обсудить плюсы и минусы дня в спокойной "
    "обстановке. Один из самых запоминающихся свадебных "
    "подарков - набор нардов - получил близкий друг. Я спросила "
    "его, зачем он сделал нам такой подарок. Он ответил, что "
    "считает важным аспектом брака никогда не прекращать "
    "совместные игры. По прошествии лет, когда я "
    "начала покупать и проходить с другими парами и коллегами "
    "многие игры, такие как: Monopoly, Chutes & Ladders, "
    "Mastermind, Dweebs, Geeks, & Weirdos и т.д. Я сознаю их "
    "неотъемлемую роль, которую они сыграли в наши выходные и "
    "в наши недели аля «выключите телевизор и займитесь "
    "чем-нибудь более стимулирующим». Они обогатили мою "
    "жизнь и сделали ее интереснее. К сожалению, многие "
    "взрослые забывают, что игры вообще существуют, а "
    "прячут их в шкафы, о которых забывают, пока не придут "
    "внуки.\n"
    "Слишком часто взрослые настолько увлечены работой, чтобы "
    "платить по счетам и не отставать от «Джонсов», что "
    "пренебрегают радостью жизни; удовольствием, которое может "
    "быть наградой за расслабляющую игру с другим человеком. "
    "Было сказано, что «человек - это для того, чтобы иметь "
    "радость», но слишком часто мы идем по жизни без особой "
    "радости. Игры позволяют нам расслабиться, узнать что-то "
    "новое и интересное, взаимодействовать с людьми на другом, "
    "более комфортном уровне и наслаждаться безопасным "
    "соревнованием. По этим причинам взрослые должны уделять "
    "больше внимания играм в своей жизни"
)

ITALIAN_TEXT = (
    "Roma è un comune italiano, capitale della Repubblica Italiana, "
    "nonché capoluogo dell'omonima città metropolitana e della regione Lazio."
)

DIFFICULT_WORD = "Regardless"
EASY_WORD = "Dog"

EMPTY_STR = ""

EASY_ARABIC_TEXT = "ذهب هند وأحمد الى المدرسة. هند تحب الرسم والمطالعة"
HARD_ARABIC_TEXT = "\u062a\u062a\u0631\u0643\u0632 \u0623\u0633\u0633 \
    \u0627\u0644\u0641\u064a\u0632\u064a\u0627\u0621 \
    \u0627\u0644\u0646\u0648\u0648\u064a\u0629 \u0628\u0634\u0643\u0644 \
    \u0639\u0627\u0645 \u0639\u0644\u064a \u0627\u0644\u0630\u0631\u0629 \
    \u0648\u0645\u0643\u0648\u0646\u0627\u062a\u0647\u0627 \
    \u0627\u0644\u062f\u0627\u062e\u0644\u064a\u0629 \
    \u0648\u0627\u0644\u062a\u0639\u0627\u0645\u0644 \
    \u0645\u0639 \u062a\u0644\u0643 \u0627\u0644\u0630\u0631\u0629 \
    \u0648\u0627\u0644\u0639\u0646\u0627\u0635\u0631 \
    \u0648\u062d\u064a\u062b \u0627\u0646 \u0647\u0630\u0627 \u0647\u0648 \
    \u0627\u0644\u0645\u0628\u062d\u062b \u0627\u0644\u0639\u0627\u0645 \
    \u0644\u0644\u0641\u064a\u0632\u064a\u0627\u0621 \
    \u0627\u0644\u0646\u0648\u0648\u064a\u0629 \u0641\u0627\u0646\u0647 \
    \u0627\u062d\u064a\u0627\u0646\u0627 \u0645\u0627 \
    \u064a\u0637\u0644\u0642 \u0639\u0644\u064a\u0647\u0627 \
    \u0627\u0644\u0641\u064a\u0632\u064a\u0627\u0621 \
    \u0627\u0644\u0630\u0631\u064a\u0629 \
    \u0627\u0644\u0627 \u0623\u0646 \u0645\u062c\u0627\u0644 \
    \u0627\u0644\u0641\u064a\u0632\u064a\u0627\u0621 \
    \u0627\u0644\u0646\u0648\u0648\u064a\u0629 \
    \u0623\u0639\u0645 \u0648\u0627\u0634\u0645\u0644 \u0645\u0646 \
    \u0627\u0644\u0641\u064a\u0632\u064a\u0627\u0621 \
    \u0627\u0644\u0630\u0631\u064a\u0629 \u0648\u0643\u0630\u0644\u0643 \
    \u0627\u0644\u0641\u064a\u0632\u064a\u0627\u0621 \
    \u0627\u0644\u0630\u0631\u064a\u0629 \u062a\u0647\u062a\u0645 \
    \u0628\u062f\u0627\u0631\u0633\u0629 \
    \u0627\u0644\u0630\u0631\u0629 \u0641\u0649 \
    \u062d\u0627\u0644\u0627\u062a\u0647\u0627 \
    \u0648\u062a\u0641\u0627\u0639\u0644\u0627\u062a\u0647\u0627 \
    \u0627\u0644\u0645\u062e\u062a\u0644\u0641\u0629"

# Hungarian tests

EASY_HUNGARIAN_TEXT = "A ló zabot eszik és én a csillagos ég alatt alszom ma."

EASY_HUNGARIAN_TEXT2 = """
    Mondok neked egy nyelvtani fejtöröt.Melyik több?
    Hat tucat tucat vagy fél tucat tucat?
    """

HARD_HUNGARIAN_TEXT = """
    A mai fagylalt elődjének számító hideg édességet több ezer éve
    készítettek először. Egyes feljegyzések szerint az ó kori kínaiak a
    mézzel édesített gyümölcsleveket hóval, jéggel hűtötték, és ezen hideg
    édességeket szolgálták fel a kiváltságosoknak. Annyi bizonyos, hogy a
    római császárok kedvelt csemegéi voltak a hegyekből hozatott hóval
    kevert gyümölcs levek, melyek sűrűn folyó, hideg, fagylaltszerű
    italkülönlegességet eredményeztek.
    """

HARD_ACADEMIC_HUNGARIAN_TEXT = """
    Az Amerikai Egyesült Államokban már a múlt század közepétől
    alkalmazzák az angol nyelv matematikai elemzésére szolgáló olvashatósági
    formulákat. Ezek közül hármat a neveléstudomány is használ a tengerentúli
    oktatásban,a különböző rendeltetési célú szövegek elemzésére. A
    vizsgálatok célja az, hogy meghatározzák a tanítási folyamatban használt
    könyvek és tankönyvek érthető megfogalmazásának korcsoport vagy iskolai
    osztályok alapján besorolható szintjét. Figyelembe véve az elméleti
    hátteret, magyar szövegeken is teszteltük a formulákat, hogy
    megállapítsuk, érvényesek-e az angol nyelvű szövegek következtetései.
    Az olvashatósági tesztek eredeti célja meghatározni azt a fogalmazási
    szintet, amely a legtöbb embernek érthető, és elkerüli az
    olvasásértelmezést zavaró szakkifejezéseket, illetve bonyolult szavak
    alkalmazását. Az 1920-as évektől kezdődően Edward Thorndike a tankönyvek
    olvasásának nehézségi fokát vizsgálta, és különböző szószedeteket
    javasolt iskolai használatra, az életkornak és az iskolai évfolyamoknak
    megfelelően.
    """

GERMAN_SAMPLE_A = """
    Alle meine Entchen schwimmen auf dem See, Köpfchen unters Wasser,
    Schwänzchen in die Höh.
    """

GERMAN_SAMPLE_B = """
    Alle Parteien widmen dem Thema rein quantitativ betrachtet nennenswerte
    Aufmerksamkeit, die Grünen wenig überraschend am meisten.
    """
