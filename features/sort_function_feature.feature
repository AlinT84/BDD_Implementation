Feature: Sort function

  Scenario: Sort the results in ascending price order
    Given user is on the Main Page
    And user searches the product
    When user clicks on the "Ordoneaza" drop-down menu
    And user clicks on the "Pret crescator" button
    Then results are sorted in the ascending price order

  Scenario: Sort the results in descending price order
    Given user is on the Main Page
    And user searches the product
    When user clicks on the "Ordoneaza" drop-down menu
    And user clicks on the "Pret descrescator" button
    Then results are sorted in the descending price order

  Scenario: Sort the results in ascending order by the number of reviews
    Given user is on the Main Page
    And user searches the product
    When user clicks on the "Ordoneaza" drop-down menu
    And user clicks on the "Nr. review-uri" button
    Then results are sorted in ascending order by the number of reviews