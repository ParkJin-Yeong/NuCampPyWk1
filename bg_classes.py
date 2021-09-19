class char:

    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def receive_dmg(self, damagetaken):
        self.hp -= damagetaken

    def get_dmg(self):
        return self.dmg

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp


class player:

    def __init__(self, name, classtype):
        self.name = name
        self.hp = classtype.hp
        self.dmg = classtype.dmg
        self.type = classtype.get_name()

    def receive_dmg(self, dmg):
        self.hp -= dmg

    def get_dmg(self):
        return self.dmg

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_type_name(self):
        return self.type
