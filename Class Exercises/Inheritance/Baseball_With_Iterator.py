from dataclasses import dataclass
from datetime import datetime

@dataclass
class Player:
    firstName: str = ''
    lastName: str = ''
    position: str = ''
    atBats: int = 0
    hits: int = 0

    @property
    def fullName(self):
        return f'{self.firstName} {self.lastName}'

    @property
    def battingAvg(self) -> float:
        try:
            avg = self.hits / self.atBats
            return avg
        except ZeroDivisionError:
            return 0.0


@dataclass
class Lineup:
    __player_list: list

    @property
    def count(self):
        return len(self.__player_list)

    def addPlayer(self, player: Player):
        self.__player_list.append(player)

    def removePlayer(self, number):
        self.__player_list.pop(number-1)

    def __iter__(self):
        for player in self.__player_list:
            yield player

def diplayPlayers(player_lineup)
    print(f"{'':3}{'Player':40}{'POS':6}{'AB':>6}{'H':>6}{'AVG':>8}")
    for i, player in enumerate(player_lineup, start=1):
        print(f'{i:<3d}{player.fullName:40}{player.position:6}{player.atBats:6d}{player.hits:6d}{player.battingAvg:8.3f}')

def title():
    print(64 * '=')
    print(f"{'Baseball Team Manager':>42}")

def get_date():
    print(f"{'CURRENT DATE:':<17}{datetime.now()}")
    print("GAME DATE:")

def menu_options():
    print('MENU OPTIONS')
    print('1 - Display Lineup')
    print('2 - Add Player')
    print('3 - Remove Player')
    print('4 - Move Player')

    print(' - Exit Program')

def main():
    lineup = Lineup([])
    lineup.addPlayer(Player("Arun", "Rameshbabu", "S", 100, 100))
    lineup.addPlayer(Player("Buster", "Posey", "C", 4575, 1380))


    print("Done")

if __name__ == "__main__":
    main()