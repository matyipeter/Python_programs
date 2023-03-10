# START

i1 = input('Adj meg egy mezőt "A 0" formátumban.\t')
i2 = input('Adj meg egy másik mezőt "A 0" formátumban.\t')

first = (i1.split()[0], int(i1.split()[1]))
second = (i2.split()[0], int(i2.split()[1]))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

class Movements():

    def __init__(self, first_block, second_block, letters):
        self.first_block = first_block
        self.second_block = second_block
        self.letters = letters

    def forward(self):
        if self.first_block[0] == self.second_block[0] and self.first_block[1] != self.second_block[1]:
            return True
        
    def aside(self):
        if self.first_block[1] == self.second_block[1] and self.first_block[0] != self.second_block[0]:
            return True
        
    def cross(self):
        if abs(self.letters.index(self.first_block[0].lower())-self.letters.index(self.second_block[0].lower())) == abs((self.first_block[1]-self.second_block[1])):
            return True


# CREATE OBJECTS

piece = Movements(first, second, letters)

# DEFINE THE PIECES


def pawn_move(obj):
    print('Paraszt:')
    if obj.forward() and obj.first_block[1]+1 == obj.second_block[1]:
        print('Ez egy jó lépés a paraszttal.')
    else:
        print('Nem lehet ilyen lépni')


def rook_move(obj):
    print('Bástya:')
    if obj.forward() or obj.aside():
        print('Ez egy jó lépés a bástyával')
    else:
        print('Nem lehet ilyet lépni')


def king_move(obj):
    print('Kiráy')
    if (obj.forward() and abs(obj.first_block[1] - obj.second_block[1]) == 1) or (obj.aside() and abs(letters.index(first[0].lower()) - letters.index(second[0].lower())) == 1) or (obj.cross() and abs(obj.first_block[1] - obj.second_block[1]) == 1):
        print('Ez egy jó lépés a királlyal.')
    else:
        print('Nem lehet ilyet lépni')


def queen_move(obj):
    print('Királynő')
    if obj.forward() or obj.aside() or obj.cross():
        print('Ez egy jó lépés a királynővel')
    else:
        print('Nem lehet ilyet lépni')


def bishop_move(obj):
    print('Futó')
    if obj.cross():
        print('Ez egy jó lépés a futóval.')
    else:
        print('Nem lehet ilyet lépni.')


def knight_move(obj):
    print('Ló')
    if abs(obj.first_block[1] - obj.second_block[1]) * abs(letters.index(obj.first_block[0].lower()) - letters.index(obj.second_block[0].lower())) == 2:
        print('Ez egy jó lépés a lóval.')
    else:
        print('Nem jó a lépés')


pawn_move(piece)
rook_move(piece)
king_move(piece)
queen_move(piece)
bishop_move(piece)
knight_move(piece)



        
        
