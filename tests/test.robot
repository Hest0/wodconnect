*** Settings ***
Documentation  Test login to wodconnect website
Library  SeleniumLibrary

*** Variables ***
${LOGIN URL}  https://www.wodconnect.com/users/sign_in
${BROWSER}  Chrome  

*** Test Cases ***
Test Login
    Open Browser To Login Page
    Input Username  your_email
    Input Password  your_password
    Submit Credentials
    Wait Until Page Contains Element  //span[@class='subline']
    Sleep  10  To see it works
    [Teardown]    Close Browser
    
*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Login | WODconnect

Input Username
    [Arguments]    ${username}
    Input Text    id:user_email    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    id:user_password    ${password}

Submit Credentials
    Press Keys    commit    RETURN

Welcome Page Should Be Open
    Title Should Be    Gym feed | WODconnect
