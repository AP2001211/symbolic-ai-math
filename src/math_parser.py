import spacy


# Load the spaCy model
nlp = spacy.load("en_core_web_sm")



def parse_text(input_text):
    doc = nlp(input_text.lower())
    result = {"operation": "solve", "expression": ""}  # Default operation to 'solve'

    for token in doc:
        if token.lemma_ in ["solve", "differentiate", "integrate"]:
            result["operation"] = token.lemma_
        elif token.like_num or token.is_alpha or token.text in "+-*/^=()xπ":  # Common cases
            result["expression"] += token.text + " "
        elif len(token.text) > 1 and not token.is_stop:  # Multi-character tokens excluding stop words
            result["expression"] += token.text + " "
        else:
            print(f"Unhandled token: {token.text}")  # Debugging for unsupported cases

    # Trim extra spaces and return
    result["expression"] = result["expression"].strip()
    return result