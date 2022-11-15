from utilities.BaseClass import BaseClass

player_list = []


class TestForeignPlayer(BaseClass):

    def test_foreign_players(self):
        self.log = self.custom_Logger()
        for player in self.jsondata['player']:
            if player['country'] != 'India':
                self.log.info(player['name'])
                player_list.append(player['name'])
        self.log.info(player_list)
        assert len(player_list) == 4


