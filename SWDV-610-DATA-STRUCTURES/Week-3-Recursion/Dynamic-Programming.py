def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins


print("recMC([1, 5, 10, 25], 63): ", recMC([1, 5, 10, 25], 63))


def recDC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins


print("recDC([1, 5, 10, 25], 63, [0] * 64): ", recDC([1, 5, 10, 25], 63, [0] * 64))


def iterFib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def recurFib(n):
    if n <= 1:
        return n
    else:
        return recurFib(n - 1) + recurFib(n - 2)


def memoizedFib(n, cache={}):
    if n in cache:
        ans = cache[n]
    elif n <= 2:
        ans = 1
        cache[n] = ans
    else:
        ans = memoizedFib(n - 2) + memoizedFib(n - 1)
        cache[n] = ans
    return ans
