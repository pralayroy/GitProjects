# Created by Pralay at 09-03-2021
Feature: Github API validation
  # Enter feature description here

  Scenario: Session management check
    Given I have Github auth credentials
    When I hit getRepo API of Github
    Then Status code of response should be 401
    # Enter steps here