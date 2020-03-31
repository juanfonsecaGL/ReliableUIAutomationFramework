Feature: Search Page

  Background: Opening webpage
  Given I navigate to the google page

  Scenario: Search page contains 10 navigation result pages
    When I search for "python behave"
    And I see a search result "Tutorial — behave 1.2.7.dev1 documentation"
