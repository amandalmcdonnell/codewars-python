def getCount(inputStr):
    num_vowels = 0
    for i in ['a','e','i','o','u']:
        num_vowels=num_vowels+(inputStr.count(i))

    return num_vowels
