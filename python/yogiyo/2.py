import spacy
import re
nlp = spacy.load("en_core_web_sm")
PERSON = 380


def anonymize_text(sentences):

    doc = nlp(sentences)

    # for ent in doc.ents:
    #     if ent.label == PERSON:
    #         masking_word_set.add(ent.text)

    sentence_list = []
    for sent in doc.sents:
        sub_sentence = sent.text
        masking_words = []
        for ent in sent.ents:
            if ent.label == PERSON:
                masking_words.append(ent.text)

        for masking_word in masking_words:
            sub_sentence = re.sub(masking_word, "X" * len(masking_word), sub_sentence)
        sentence_list.append(sub_sentence)

    return ' '.join(sentence_list)


if __name__ == '__main__':
    print(anonymize_text("John ate an apple Oh John"))
    print(anonymize_text("Mark Oldham ate an apple"))
