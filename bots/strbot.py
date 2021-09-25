def strbot(message):
    strval = [
        [" /`\ ", "|   |", "|___|", "|   |", "|   |"], # A
        ["|```\\", "|   /", "|--< ", "|   \\", "|___/"], # B
        [" /```", "|    ", "|    ", "|    ", " \___"], # C
        ["|``\ ", "|   |", "|   |", "|   |", "|__/ "], # D
        ["|````", "|    ", "|----", "|    ", "|____"], # E
        ["|````", "|    ", "|----", "|    ", "|    "], # F
        [" /```", "|    ", "|  _ ", "|   |", " \__|"], # G
        ["|   |", "|   |", "|---|", "|   |", "|   |"], # H
        ["``|``", "  |  ", "  |  ", "  |  ", "__|__"], # I
        ["``|``", "  |  ", "  |  ", "  |  ", "__/  "], # J
        ["|   /", "|  / ", "|-+  ", "|  \ ", "|   \\"], # K
        ["|    ", "|    ", "|    ", "|    ", "|____"], # L
        ["\   /", "|\ /|", "| \" |", "|   |", "|   |"], # M
        ["|   |", "|\  |", "| \ |", "|  \|", "|   |"], # N
        ["/```\\", "|   |", "|   |", "|   |", "\___/"], # O
        ["/```\\", "|   |", "|___/", "|    ", "|    "], # P
        ["/```\\", "|   |", "|   |", "|  \|", "\___\\"], # Q
        ["/```\\", "|   |", "|___/", "| \  ", "|  \ "], # R
        ["/````", "|    ", "\___ ", "    |", "____/"], # S
        ["``|``", "  |  ", "  |  ", "  |  ", "  |  "], # T
        ["|   |", "|   |", "|   |", "|   |", "|___|"], # U
        ["|   |", "|   |", "|   |", "|   |", " \_/ "], # V
        ["|   |", "|   |", "|   |", "| ^ |", "\/ \/"], # W
        ["\   /", " \ / ", "  +  ", " / \ ", "/   \\"], # X
        ["\   /", " \ / ", "  |  ", "  |  ", "  |  "], # Y
        ["````/", "   / ", "  /  ", " /   ", "/____"], # Z
        ["     ", "     ", "     ", "     ", "     "] # Space
    ]
    val = message.upper()
    ind = []
    for i in range(len(val)):
        if(ord(val[i]) >= 65 and ord(val[i]) <= 90 or ord(val[i]) == 32):
            if(ord(val[i]) == 32):
                ind.append(26)
            else:
                ind.append(ord(val[i]) - ord('A'))
    if(len(ind) == 0):
        return "Give some letters"
    val = "\n"
    for i in range(5):
        for j in range(len(ind)):
            val += strval[ind[j]][i] + " "
        val += "\n"
    return val