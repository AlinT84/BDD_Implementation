Feature: Main menu correct URL navigation

  Scenario: Home logo button redirects to main page
    Given user is on the Main Page
    When user clicks on the home logo button
    Then user is redirected to the main page

  Scenario: The account button redirects to account login page
    Given user is on the Main Page
    When user clicks on the account button
    Then user is redirected to the login page

  Scenario: The favourites button redirects to the user's favourite products list
    Given user is on the Main Page
    When user clicks on the favourites button
    Then user is redirected to the user favourite products list

  Scenario: The shopping cart button redirects to the shopping cart page
    Given user is on the Main Page
    When user clicks on the shopping cart button button
    Then user is redirected to the shopping cart page

  Scenario: The Oferta zilei button redirects to the Genius deals page
    Given user is on the Main Page
    When user clicks on the "Oferta zilei" button
    Then user is redirected to the "Oferta zilei" page

  Scenario: The Genius deals button redirects to the Genius deals page
    Given user is on the Main Page
    When user clicks on the Genius deals button
    Then user is redirected to the Genius deals page

  Scenario: The Genius button redirects to the Genius program page
    Given user is on the Main Page
    When user clicks on the Genius button
    Then user is redirected to the Genius program page

  Scenario: The "Cardul cu idei" button redirects to the details page about this program
    Given user is on the Main Page
    When user clicks on the "Cardul cu idei" button
    Then user is redirected to the details page about "Cardul cu idei" program

  Scenario: The "Rabla" button redirects to the details page about this program
    Given user is on the Main Page
    When user clicks on the "Rabla" button
    Then user is redirected to the details page about "Rabla" program

  Scenario: The "Oferte eMag" button redirects to the details page about this program
    Given user is on the Main Page
    When user clicks on the "Oferte eMag" button
    Then user is redirected to the details page about "Oferte eMag" program
