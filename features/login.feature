Feature: HUDL Login Page

   Scenario: Logo in HUDL login page
     Given open chrome browser
     When navigate to hudl login page
     Then verify hudl logo is present
     And close browser

   Scenario: Email input is present
     Given open chrome browser
     When navigate to hudl login page
     Then verify email input is present
     And close browser

   Scenario: Password input is present
     Given open chrome browser
     When navigate to hudl login page
     Then verify password input is present
     And close browser

   Scenario: Login button works
     Given open chrome browser
     When navigate to hudl login page
     Then click on Login button
     But login error message appear
     And close browser

   Scenario Outline: Try other sections links
     Given open chrome browser
     When navigate to hudl login page
     Then click on <link>
     And verify it navigated to <section>
     And click on <button>
     And verify hudl logo is present
     And close browser

     Scenarios:
     | link                        | section                              | button                         |
     | Need help?                  | Login Help                           | Back Arrow                     |
     | Log In with an Organization | Log into Hudl with your Organization | Back Arrow Org                     |
     | Log In with an Organization | Log into Hudl with your Organization | Log In with Email and Password |

  Scenario: Log in with existing user
    Given open chrome browser
    When navigate to hudl login page
    Then insert email "manuelsg1996@gmail.com"
    And insert password "test1ng2023."
    And click on Login button
    And validate you are in user homepage
    And close browser

  Scenario Outline: log in with wrong data
    Given open chrome browser
    When navigate to hudl login page
    Then insert email <email>
    And insert password <password>
    And click on Login button
    But login error message appear
    And close browser

    Scenarios:
    | email | password |
    | "johndoe@hudl.es" | "thisismypassword" |
    | "$3fekfiw23" | "thisisatest" |
    | "johndoe@hudl.es" | "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sapien nulla, congue in quam a, imperdiet congue est. Suspendisse potenti. Aliquam tempor ipsum id auctor auctor. Nunc posuere turpis urna, eu efficitur sem pulvinar non. Aenean sollicitudin nibh quis justo tristique sodales. Fusce porttitor turpis et viverra consectetur. In consectetur nunc id magna sodales ultricies. Nulla aliquet felis sit amet ante bibendum egestas. Nulla dictum tristique ultricies. Aenean pellentesque placerat auctor. Suspendisse ut sem erat. Vivamus non interdum nulla, nec volutpat quam. Vivamus pharetra quam in purus dictum, quis convallis tortor vehicula. Ut venenatis posuere purus id molestie. Cras ac vulputate urna." |
    | "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sapien nulla, congue in quam a, imperdiet congue est. Suspendisse potenti. Aliquam tempor ipsum id auctor auctor. Nunc posuere turpis urna, eu efficitur sem pulvinar non. Aenean sollicitudin nibh quis justo tristique sodales. Fusce porttitor turpis et viverra consectetur. In consectetur nunc id magna sodales ultricies. Nulla aliquet felis sit amet ante bibendum egestas. Nulla dictum tristique ultricies. Aenean pellentesque placerat auctor. Suspendisse ut sem erat. Vivamus non interdum nulla, nec volutpat quam. Vivamus pharetra quam in purus dictum, quis convallis tortor vehicula. Ut venenatis posuere purus id molestie. Cras ac vulputate urna." | "password"        |
  




