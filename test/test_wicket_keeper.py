from utilities.BaseClass import BaseClass

wicket_keeper_list = []


class TestWicketKeeper(BaseClass):

    def test_wicket_keeper(self):
        self.log = self.custom_Logger()
        self.log.info("The json data = " + str(self.jsondata))
        for player in self.jsondata['player']:
            if player['role'] == 'Wicket-keeper':
                self.log.info(player['name'])
                wicket_keeper_list.append(player['name'])
        self.log.info("The wicket keeper players name = " + str(wicket_keeper_list))
        assert len(wicket_keeper_list) == 1


