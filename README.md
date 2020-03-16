# BigBlueButton-Attendance
Automatic attendance script for BigBlueButton

## Getting Started

These instructions will get you a copy of the project up and running. To see how to run the program read the Deployment section.
### Prerequisites

* Firefox and it's gecko (if someone needs chrome just tell me and I will update it to be able to use chrome too)
* Python3
* pipenv

### Installing

I am using pipenv for packaging so just use the pipenv file.

```
git clone https://github.com/q1e123/BigBlueButton-Attendance
cd BigBlueButton-Attendance
pipenv install
```
### Setup

Make a config file, following the template. **You need to modify just the right part of each line**

#### Template

spreadsheet = the type of spreadsheet (ex: xlsx) . If you don't need to use one put -

spreadsheet_name = name of the spreadsheet file

week = will be used to put the attendance (A + week)

login = the login link of the platform

user, pass = your credentials

link = the link of the page that has the button to join a session

output = name of the file that will contain current users

#### Example

```
spreadsheet xlsx
spreadsheet_name test.xlsx
sheetname Sheet1
week 8
login https://example.com/login/index.php
user example@example.com
pass password
link https://example.com/mod/bigbluebuttonbn/view.php?id=12345
output users
```


## Deployment

```
pipenv run python3 main.py
```


