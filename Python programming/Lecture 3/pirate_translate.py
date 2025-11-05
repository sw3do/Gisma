
def change_sentence(text):
    styles = [('hello', 'ahoy'), ('my', 'me'), ('friend', 'matey')]
    for oldText, newText in styles:
        text = text.replace(oldText, newText)
    return text

input_text = str(input("Enter a sentence to translate to pirate speak: "))
output_text = change_sentence(input_text)
print(f"Pirate translation: {output_text}")