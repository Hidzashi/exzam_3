# Напишите функцию, которая проверяет: является ли слово палиндромом

def isPalindrome(word: str) -> bool:
    return True if word.lower()[::-1] == word.lower() else False

print(isPalindrome("qwerty"))
print(isPalindrome("qwertytrewq"))