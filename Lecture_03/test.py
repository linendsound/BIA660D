import re
import spacy

from pyclausie import ClausIE

# def get_data_from_file(file_path='./trip.txt'):from pyclausie import ClausIre_spaces = re.compile(r'\s+')with open(file_path) as infile:
#     cleaned_lines = [line.strip() for line in infile if (not line.startswith(('$$$', '###', '==='))) and line!='']
#     return cleaned_lines

def preprocess_question(question):
    # remove articles: a, an, the

    q_words = question.split(' ')

    # when won't this work?
    for article in ('a', 'an', 'the'):
        try:
            q_words.remove(article)
        except:
            pass

    return re.sub(re_spaces, ' ', ' '.join(q_words))


def has_question_word(string):
    # note: there are other question words
    for qword in ('who', 'what'):
        if qword in string.lower():
            return True

    return False

# (PERSON, travels, TRIP)  going to|flying to|traveling to|visiting
# (TRIP, departs_on, DATE)
# (TRIP, departs_to, PLACE)

nlp = spacy.load('en_core_web_sm')
re_spaces = re.compile(r'\s+')
# sents = get_data_from_file()
cl = ClausIE.get_instance()


question = "What's the name of Bob's cat?"
q_doc = nlp(unicode(preprocess_question(question)))
if 'what' in [q.text.lower() for q in q_doc] and 'name' in [q.text.lower() for q in q_doc] and 'PERSON' in [token.ent_type_ for token in q_doc]:
     print('True')
     for chunks in q_doc.noun_chunks:
         print([(token.text,token.pos_,token.dep_) for token in chunks])

     # print([token.text for token in q_doc if token.pos_ == 'PROPN'])
# print([q.text for q in q_doc])



p =1