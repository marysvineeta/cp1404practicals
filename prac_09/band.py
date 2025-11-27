class Band:

    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def __str__(self):
        musicians_text = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_text})"

    def __repr__(self):
        return str(vars(self))

    def add(self, musician):
        """Add a Musician to the band."""
        self.musicians.append(musician)

    def play(self):
        lines = []
        for musician in self.musicians:
            lines.append(musician.play())
        return "\n".join(lines)
