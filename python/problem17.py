from itertools import product
def get_letters(x):
    if x == 2:
        return list("abc")
    elif x == 3:
        return list("def")
    elif x == 4:
        return list("ghi")
    elif x == 5:
        return list("jkl")
    elif x == 6:
        return list("mno")
    elif x == 7:
        return list("pqrs")
    elif x == 8:
        return list("tuv")
    elif x == 9:
        return list("wxyz")

def letterCombinations(digits):
    numbers = list(digits)
    all_letters = []
    ans = []
    for num in numbers:
        temp = get_letters(int(num))
        all_letters.append(temp)
    combo = list(product(*all_letters))
    print(combo)
    for comb in combo:
        ans.append(''.join(comb))
    print(ans)

letterCombinations("23")
