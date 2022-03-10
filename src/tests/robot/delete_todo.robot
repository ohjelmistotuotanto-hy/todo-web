*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create Todo And Go To Home Page

*** Test Cases ***
Delete Todo
    Page Should Contain  Test todo
    Click Button  Delete
    Home Page Should Be Open
    Page Should Not Contain  Test Todo

*** Keywords ***
Create Todo And Go To Home Page
    Create Todo  Test todo
    Go To Home Page
