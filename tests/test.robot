*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
This is a test
    [Documentation]  Google test
    [Tags]  regression

    Open Browser  http://www.google.com  chrome
    Close Browser
*** Keywords ***  