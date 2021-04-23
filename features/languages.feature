Feature: Languages

  Scenario: English Wikipedia
    Given The Guest is on the Wikipedia Home Page
    When The Guest clicks on English
    Then The Guest should be on the English Home Page

  Scenario: Spanish Wikipedia
    Given The Guest is on the Wikipedia Home Page
    When The Guest clicks on Spanish
    Then The Guest should be on the Spanish Home Page

  Scenario: Italian Wikipedia
    Given The Guest is on the Wikipedia Home Page
    When The Guest clicks on Italian
    Then The Guest should be on the Italian Home Page