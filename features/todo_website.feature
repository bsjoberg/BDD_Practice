Feature: Is my website available
  Scenario: Test if django is running
    Given I have django running
    When I go to the website
    Then I see "To-Do" in the title

  Scenario: Add an item to my list and retrieve it later
    Given I goto the to-do website
    When I add an item
    Then I see the item on my to-do list

  Scenario: Multiple people create lists and are retrieved
    Given I goto the to-do website
    When I add an item
    And someone else adds an item
    Then I see the item on my to-do list
    And I don't see someone elses item
