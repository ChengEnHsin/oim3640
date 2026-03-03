"""
Spelling Bee Puzzle Solver

Rules:
- Use only 7 given letters
- Must include the center letter
- Must be at least 4 letters long
"""

from typing import List


def uses_only(word: str, letters: str) -> bool:
    """Does word use only the allowed letters?
    
    Similar to all_digit() - checks if ALL characters meet the condition.
    """
    word_lower = word.lower()
    for letter in word_lower:
        if letter not in letters:
            return False
    return True


def must_use(word: str, center: str) -> bool:
    """Does word include the center letter?
    
    Similar to has_digit() - checks if AT LEAST ONE character meets the condition.
    """
    return center.lower() in word.lower()


def is_long_enough(word: str, min_length: int = 4) -> bool:
    """Does word meet minimum length requirement?"""
    return len(word) >= min_length


import os


def load_dictionary(filepath: str = None) -> List[str]:
    """Load dictionary from file or use fallback list.

    Args:
        filepath: Path to dictionary file. If None, tries to read
            "data/words.txt" relative to workspace root.

    Returns:
        List of words
    """
    # determine default path when none provided
    if filepath is None:
        # assume workspace root is two levels up from this file
        base = os.path.dirname(os.path.dirname(__file__))
        default = os.path.join(base, "data", "words.txt")
        filepath = default
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return [word.strip() for word in f if word.strip()]
    except FileNotFoundError:
        print(f"Dictionary file not found: {filepath}")
        # fallback list if desired (small sample)
        return [
            "able", "bale", "bean", "bear", "lean", "learn", "near", "renal",
            "blear", "blare", "lane", "lobe", "lorn", "earl", "era", "ern", "nab",
            "able", "label", "rebel", "bane", "lane", "leap", "pale", "peal",
        ]


def find_words(word_list: List[str], letters: str, center: str) -> List[str]:
    """Find all valid words from a word list.
    
    Args:
        word_list: List of candidate words
        letters: String of 7 allowed letters
        center: The required center letter
    
    Returns:
        List of valid words sorted by length then alphabetically
    """
    valid = []
    
    for word in word_list:
        if (is_long_enough(word) and 
            uses_only(word, letters) and 
            must_use(word, center)):
            valid.append(word.lower())
    
    # Remove duplicates and sort
    valid = list(set(valid))
    valid.sort(key=lambda w: (-len(w), w))
    
    return valid


def score_words(words: List[str]) -> dict:
    """Calculate score for found words (4-letter = 1pt, longer = length points).
    
    Args:
        words: List of valid words
    
    Returns:
        Dictionary with word -> points mapping and total score
    """
    scores = {}
    total = 0
    
    for word in words:
        if len(word) == 4:
            points = 1
        else:
            points = len(word)
        scores[word] = points
        total += points
    
    return {"words": scores, "total": total}


def display_results(words: List[str], show_score: bool = True) -> None:
    """Display results in a formatted way.
    
    Args:
        words: List of valid words
        show_score: Whether to show scoring
    """
    if not words:
        print("No valid words found.")
        return
    
    print(f"\nFound {len(words)} valid word(s):\n")
    
    if show_score:
        scores = score_words(words)
        for word, points in sorted(scores["words"].items(), key=lambda x: -x[1]):
            print(f"  {word:<15} ({len(word)} letters) = {points} pts")
        print(f"\nTotal Score: {scores['total']} points")
    else:
        for word in words:
            print(f"  {word:<15} ({len(word)} letters)")


def main():
    """Load words, set up puzzle, print results."""
    # Example: letters "bcelnra" with center letter "l"
    letters = "bcelnra"
    center = "l"
    
    print(f"Spelling Bee Puzzle")
    print(f"Letters: {letters.upper()}")
    print(f"Center: {center.upper()}")
    print("=" * 40)
    
    dictionary = load_dictionary()
    valid_words = find_words(dictionary, letters, center)
    display_results(valid_words, show_score=True)
    
    print("\n" + "=" * 40)
    print("Example 2:")
    # Another example
    letters2 = "aeglmnr"
    center2 = "a"
    print(f"Spelling Bee Puzzle")
    print(f"Letters: {letters2.upper()}")
    print(f"Center: {center2.upper()}")
    print("=" * 40)
    
    valid_words2 = find_words(dictionary, letters2, center2)
    display_results(valid_words2, show_score=True)


def solve_puzzle(letters: str, center: str, dict_file: str = None) -> None:
    """Standalone function to solve a specific puzzle."""
    print(f"Spelling Bee Puzzle")
    print(f"Letters: {letters.upper()}")
    print(f"Center: {center.upper()}")
    print("=" * 40)
    
    dictionary = load_dictionary(dict_file)
    valid_words = find_words(dictionary, letters, center)
    display_results(valid_words, show_score=True)


if __name__ == "__main__":
    main()
