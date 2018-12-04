def arithmetic_sequence_sum(a, r, n):
    start=0
    for i in range(n):
        start=start+a+(r*(i))
    return start
