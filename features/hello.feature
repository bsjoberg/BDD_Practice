Feature: Hello World
  Scenario: test if the development environment is working
    Given there is a hello world
    When I say hi
    Then I get "Hello World" message