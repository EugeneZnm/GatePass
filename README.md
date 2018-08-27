# PASSWORD LOCKER

## Built by [EUGENE NZIOKI](https://github.com/EugeneZnm)

## Description

A Password Locker with user login and password details, enabling a
user to store existing login credentials, generate new credentials 
for new accounts, copy credentials to clipboard and dictate length 
of password to generate

## User Stories

These are the features that the application implements for use by a user

A user should be able to:

   * Creating an account with  my details -login and password
   * Create credentials for carious accounts
   * Auto-generate password for new account
   * Store created credentials
   * Search for created credentials and delete credentials

## Specifications


|  Behaviour |  Input   |   Output    |  
| :--------------------- | :-------------------------: | -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Show navigation codes | **In terminal:$./runpass.py** | Welcome Enter you Details.Type in Shortcode to choose preferred action:start - to enter user details,  save - to create credentials, show - to display credentials, search -  to find by service, remove - to delete credentials, copy - to copy service password|
|Enter user details | **Enter : start** | Enter User Info, First Name:, Last Name:, Password |
|Creating Credential| **Enter : save**| Enter Name: , Service Used: , Your Password is:, Welcome {first name} {last name}, your details have been saved |
|Show credentials | **Enter : show**| Your stores credentials are: Username, Servicename, Password|                                             
|Search for credentials| **Enter : search** | Enter service to find credentials:|
|Delete credentials | **Enter : remove** | delete credential |
|copy credential | **Enter: copy** |                                                                                                                                                                                                                                                                 
    
## SetUp / Installation Requirements

### Prerequisites

   * python3.6
   * pip
   * pyperclip

## Cloning
   * In terminal:
   
   
        ``$ git clone https://github.com/EugeneZnm/GatePass``
        
        ``$ cd GettPass``                      

## Running the Application

   * To run the application in terminal:
   
        ``$ python3.6 passwordtest.py``                             

## Technologies Used

   * python3.6
   
## License Information
    
    
MIT License

Copyright(c) 2018

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
                  