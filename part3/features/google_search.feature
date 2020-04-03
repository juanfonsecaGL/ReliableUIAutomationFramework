Feature: Search Page

  Background: Opening webpage
  Given I navigate to google page

  Scenario: Search into google
    When I search for "python behave"
    And I see "Welcome to behave! — behave 1.2.7.dev1 documentation"
