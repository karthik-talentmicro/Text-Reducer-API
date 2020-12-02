import spacy 
nlp = spacy.load('en_core_web_sm')

def text_tokenizer(introduction_file_text):
    converted_list =[]
    introduction_file_doc =nlp(introduction_file_text)
    converted_text = ""
    for token in introduction_file_doc:
        if not token.is_stop and not token.is_punct:
            if token.pos_ == "NOUN" or token.pos_ == "PROPN" :
                if token.lemma_ not in converted_list:
                    print(token," ",token.lemma_, token.pos_)
                    converted_list.append(token.lemma_.lower()) 
                    converted_text += " "+token.lemma_.lower()

    reduced = int(len(introduction_file_doc) - len(converted_list))
    return converted_list, converted_text, reduced 