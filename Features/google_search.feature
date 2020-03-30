Feature: Search Page

  Background: Opening webpage
  Given I navigate to google page

  Scenario: Search page contains 10 navigation result pages
    When I search for "python behave"
    And I see "Tutorial — behave 1.2.7.dev1 documentation - Read the Docs"
