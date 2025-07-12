def generate_binary_combinations(n):
    res = []

    def backtrack(string):
        if len(string) == n:
            res.append(string)
            return
        backtrack(string + "0")
        backtrack(string + "1")

    backtrack("")
    return res


if __name__ == '__main__':
    res = generate_binary_combinations(2)
    print(res)
