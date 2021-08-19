from nltk import pos_tag, download
from nltk.data import find


class RegularInflections:

    def __init__(self):
        try:
            find('taggers/averaged_perceptron_tagger')
        except LookupError:
            download('averaged_perceptron_tagger')

    def add_regular_inflections(self, words, incl_word_forms=[
                'plural', 'posessive', 'comparative', 'superlative', 'tenses']):
        """Add the regular inflections of words in the set to the set.

        Parameters
        ----------
        words : set
            DESCRIPTION.
        incl_word_forms : list, optional
            DESCRIPTION. The default is ['plural', 'posessive', 'comparative', 'superlative', 'tenses'].

        Returns
        -------
        words : set.

        """
        nouns = [
            word for word, tag in pos_tag(words)
            if tag.startswith('N')]
        adjs_and_advs = [
            word for word, tag in pos_tag(words)
            if (tag.startswith('JJ') or tag.startswith('RB'))
            ]
        verbs = [
            word for word, tag in pos_tag(words)
            if tag.startswith('JJ')
            ]

        if 'plural' in incl_word_forms:
            plurals = [word+'s' for word in nouns
                       if (pos_tag([word+'s'])[0][1] == 'NNS')]
            for plural in plurals:
                words.add(plural)

        if 'posessive' in incl_word_forms:
            # only add the 's form for singular proper nouns (NNP)
            posessives = [word+"'s" for word in nouns
                          if pos_tag([word])[0][1] == 'NNP']
            for posessive in posessives:
                words.add(posessive)

        if 'superlative' in incl_word_forms:
            superlatives = [
                word+'est' for word in adjs_and_advs
                if (pos_tag([word+'est'])[0][1] == 'JJS')
                or (pos_tag([word+'est'])[0][1] == 'RBS')]
            for superlative in superlatives:
                words.add(superlative)

        if 'comparative' in incl_word_forms:
            comparatives = [
                word+'er' for word in adjs_and_advs
                if (pos_tag([word+'er'])[0][1] == 'JJR')
                or (pos_tag([word+'er'])[0][1] == 'RBR')]
            for comparative in comparatives:
                words.add(comparative)

        if 'tenses' in incl_word_forms:

            # verb, present tense, 3rd person singular
            tenses = [
                    word+'s' for word in verbs
                    if (pos_tag([word+'s'])[0][1] == 'VBZ')
                    ]
            tenses += [
                    word[:-1]+'ies' for word in verbs
                    if (word.endswith('y') and
                        pos_tag([word[:-1]+'ies'])[0][1] == 'VBZ')]

            # verb, past tense or past participle
            tenses += [
                word+'ed' for word in verbs
                if (pos_tag([word+'ed'])[0][1] == 'VBD')
                or (pos_tag([word+'ed'])[0][1] == 'VBN')
                ]
            tenses += [
                word[:-1]+'ied' for word in verbs
                if (word.endswith('y') and (
                        (pos_tag([word[:-1]+'ied'])[0][1] == 'VBD') or
                        (pos_tag([word[:-1]+'ied'])[0][1] == 'VBN')
                        ))
                ]

            # verb, present participle or gerund
            tenses += [
                word+'ing' for word in verbs
                if pos_tag([word+'ing']) == 'VBG'
                ]
            for word in tenses:
                words.add(word)

            return words
