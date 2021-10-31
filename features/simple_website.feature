Feature: Is my website available
  Scenario: Test if django is running
    Given I have django running
    When I go to the website
    Then I see "The install worked successfully" in the title