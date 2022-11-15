# rcb_automation

This project help to check if the team has 4 foreign player and one wicket keeper

***The project structure***
- jsonfile = here the json data is kept.
- test = Here test are written
    - conftest.py = Here json file is opened and passed to the test
    - test_4_foreign_players.py = This test checks if the team has 4 foreign players
    - test_wicket_keeper.py = This test check if the team has only one wicket keeper
- Utilities
    - BaseClass.py = Here a logger is written to print logs

Steps to run the test
- Clone the project
- Go inside the project directory
- You can run one test and also all the test in one command
  - To run one test
  > py.test test/test_4_foreign_players.py
  - To run all the tests
  > py.test test/test_*
- We can check the logs in the logfile.log
