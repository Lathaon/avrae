class Attack:
    def __init__(self, name, bonus=None, damage=None, details=None):
        self.name = name
        self.bonus = bonus
        self.damage = damage
        self.details = details

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return {"name": self.name, "bonus": self.bonus, "damage": self.damage, "details": self.details}

    # ---------- main funcs ----------
