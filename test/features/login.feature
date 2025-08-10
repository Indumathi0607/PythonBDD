Feature: Login
  As a user I want to test the login feature of Zenclass Webportal

   @successful
  Scenario: Successful login
    Validate successful login by passing the hardcoded test data through step definitions
    I replaced my credentials with XXXX, kindly give valid credential to execute the testcase
    Given As a user I launch the Zenclass webportal
    When I login with username "username" and password "password"
    Then Logged in successfully to the "Download App" page
    And I should be able to logout successfully and "Sign in" is available again


  @unsuccessful
  Scenario Outline: Unsuccessful login
    Validating unsuccessful login by using Scenario Outline and Examples
    to pass multiple set of test data
    Given As a user I launch the Zenclass webportal
    When I login with username "<username>" and password "<password>"
    Then login should fail with error message <error message>
  Examples:
    |username       |password   |error message                  |
    |username       |password   |*Incorrect email!              |
    |test@gmail.com |123456789  |Incorrect password!            |