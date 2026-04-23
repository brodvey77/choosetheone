def hash_function(obj):
    # Step 1: convert object to string
    s = str(obj)
    n = len(s)

    # Step 1: temp1 = sum of products of symmetric characters
    temp1 = 0
    for i in range(n // 2):
        temp1 += ord(s[i]) * ord(s[n - 1 - i])
    if n % 2 == 1:  # middle character if odd length
        temp1 += ord(s[n // 2])

    # Step 2: temp2 = alternating sum with increasing multipliers
    temp2 = 0
    for i in range(n):
        if i % 2 == 0:  # even index: positive
            temp2 += ord(s[i]) * (i + 1)
        else:           # odd index: negative
            temp2 -= ord(s[i]) * (i + 1)

    # Step 3: final value modulo
    result = (temp1 * temp2) % 123456791
    return result

    