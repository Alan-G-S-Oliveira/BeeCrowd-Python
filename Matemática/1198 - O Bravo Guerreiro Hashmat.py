while True:
    try:
        N, M =  map(int, input().split())
        print(abs(N - M))

    except EOFError:
        break