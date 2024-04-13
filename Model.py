from textblob import TextBlob
from language_tool_python import LanguageTool

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        self.grammar_check = LanguageTool('en-US')

    def correct_spell(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)

    def correct_grammar(self, text):
        matches = self.grammar_check.check(text)
        found_mistakes = []
        for mistake in matches:
            found_mistakes.append((mistake.ruleId, mistake.replacements))
        found_mistakes_count = len(found_mistakes)
        return found_mistakes, found_mistakes_count

    def display_grammar_mistakes(self, found_mistakes):
        for mistake in found_mistakes:
            print("Mistake:", mistake[0])
            print("Suggestions:", mistake[1])
            print()

if __name__ == "__main__":
    obj = SpellCheckerModule()
    text = "Your sentnece has some grammatical errors."
    grammar_mistakes, count = obj.correct_grammar(text)
    print("Number of grammar mistakes:", count)
    obj.display_grammar_mistakes(grammar_mistakes)
