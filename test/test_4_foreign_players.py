from utilities.BaseClass import BaseClass

player_list = []


class TestForeignPlayer(BaseClass):

    def test_foreign_players(self):
        self.log = self.custom_Logger()
        self.log.info("The json data = " + str(self.jsondata))
        for player in self.jsondata['player']:
            if player['country'] != 'India':
                self.log.info(player['name'])
                player_list.append(player['name'])
        self.log.info("The players name which are not from India = " + str(player_list))
        assert len(player_list) == 4


