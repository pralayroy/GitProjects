# Created by Pralay at 09-02-2021
# In terminal run all feature testcase run ....\BackEndAutomation>behave
# In terminal run any particular feature then run as ....\BackEndAutomation>behave features/BookAPI.feature --no-capture
# In terminal run any particular feature with tags then run as ....\BackEndAutomation>behave features/BookAPI.feature --no-capture --tags=smoke

Feature: Verify if Books are added or deleted using Library API
  # Enter feature description here
  @bookAPI
  Scenario: Verify AddBook API functionality
    Given The Book details which needs to be added to Library
    When We execute the AddBook PostAPI method
    Then Book is successfully added
    And Status code of response should be 200

  @bookAPI  #We can tagged the feature as per our requirement and we can run only those tagged features
  Scenario Outline:  Verify AddBook API functionality
    Given The Book details with <isbn> and <aisle>
    When We execute the AddBook PostAPI method
    Then Book is successfully added
    Examples:
      |isbn  |aisle|
      |pra10 |1997 |
      |pra11 |1998 |

