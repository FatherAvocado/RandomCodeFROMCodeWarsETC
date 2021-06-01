def add():
    currentnum = yield
    while True:
        value = yield currentnum
        currentnum = value + currentnum
