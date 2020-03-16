def is_multiple(n, m):
    return n % m == 0


print(
        "n = mi for some integer i: ",
        is_multiple(
            int(input("n: ")),
            int(input("m: "))
        )
      )
