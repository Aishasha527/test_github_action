def is_prime(n):
    """Check if a nber is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sum_of_primes(n):
    """Calculate the sum of all prime numbers up to a given number n."""
    sum_primes = 0
    for i in range(2, n + 1):
        if is_prime(i):
            sum_primes += i
    return sum_primes


def to_title_case(input_string):
    """Convert a string to title case."""
    # Split the string into words, strip leading/trailing spaces and ignore extra spaces
    words = input_string.strip().split()
    # Capitalize the first letter of each word and join them back with a space
    title_cased = ' '.join(word.capitalize() for word in words)
    return title_cased


def group_anagrams(strs):
    """Group anagrams from the list of strings."""
    anagram_map = {}
    for word in strs:
        # Sort the word and use it as a key
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_map:
            anagram_map[sorted_word] = []
        anagram_map[sorted_word].append(word)

    # Return only the grouped anagrams as a list of lists
    return list(anagram_map.values())
