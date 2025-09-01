*** Settings ***
Library    can_utils.py

*** Test Cases ***
Send And Receive CAN Message
    ${result}=    Send Can Message    0x123    0A0B0C0D
    Log To Console    ${result}
    ${rx}=    Receive Can Message    timeout=1
    Log To Console    ${rx}
