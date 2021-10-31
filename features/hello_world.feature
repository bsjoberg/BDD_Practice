Feature: make sure things are working
  Scenario: Dev Environment setup
    Given I have an application
    When I say hi
    Then I hear "Hello World"