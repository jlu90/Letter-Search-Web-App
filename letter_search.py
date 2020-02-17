

def search4vowels(phrase: str) -> set:
    """Display any vowels found in a word"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase.lower()))


def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of letters that are present in the provided phrase"""
    return set(letters.lower()).intersection(set(phrase.lower()))
