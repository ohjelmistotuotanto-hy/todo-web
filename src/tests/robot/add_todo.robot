*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
Add Todo With Content
    Set Todo Content  implement robot tests
    Submit Todo
    Home Page Should Be Open
    Page Should Contain  implement robot tests

*** Keywords ***
Set Todo Content
    [Arguments]  ${content}
    Input Text  content  ${content}

Submit Todo
    Click Button  Add todo
