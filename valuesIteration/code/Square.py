class Square:
    def __init__(self, up, down, right, left, value=0, reward=-1):  # Initializing a square
        self.U = up
        self.D = down
        self.R = right
        self.L = left
        self.val = value
        self.reward = reward

    def __str__(self):
        return str(self.val)