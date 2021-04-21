def slide(buf, ch):
    #buf is the buffer that will be slided, ch is the character that will be added at the last position after sliding
    for i in range(len(buf)-1):
        buf[i] = buf[i + 1]
    buf[len(buf) - 1] = ch