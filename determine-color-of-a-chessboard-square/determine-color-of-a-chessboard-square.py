class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if ((ord(coordinates[0]))+int(coordinates[1])) % 2:
            return True
        else:
            return False
        