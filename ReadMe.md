# Account Manage v3.5
 This program is based on python3.6.3 and django-2.0.3
 <br>
##### Languague : <a href='ReadMe.md'>English</a> <a href='ReadMe_zh.md'>简体中文</a>

## Important History
### 2019-02-06 : v3.5 admin is not completion.
### 2018-10-26 : v3.4 has Auth at first.

## Usage:
### 0. Set "MyCode"
#### Opened the v3/encypt.py in text-editor-software, change 'anyword' to anyword and delete the "+";
#### e.g.:<br>MyCode='8uj98hy_*asd'
#### <font color="#f00">Please don't change the word as same as the EXAMPLE!!!</font>

### 1. Copy the "Database.example.db" on the root , paste it on the root and change name to "Database.db"

### 2. Keyin shell "manage.py runserver"
#### e.g.: Windows : run "Start.bat",if you installed two versions of python , please change the bat file by yourself :)
#### Linux : keyin "python3 manage.py runserver"

### 3. Openning Address( 127.0.0.1:8000 ) ,it's ok on anyone browser
#### e.g.: Windows : keyin cmd "start 127.0.0.1:8000"
#### Linux keyin "w3m 127.0.0.1:8000"

### 4. Start your work
#### Address : Which web-site you need to registered.
#### Account :If you want to design your account ,keyin please and checkin Next "Used Account Key" , else you needn't keyin anythings in it and don't checkin "Used Account Key"
#### Generate : It's program start work button.
#### bottom one-check : checkin you needed to program to  save the password.
#### Text: you want to sign text with this account.
#### Save Result : Save Address and Account where under "the Generated Result" line and password which you check.

### 5. Search Item which you saved on the Database
#### checkin Address , Account, password and Text which you have remembered ,keyin one and checkin the one-check.
#### Search : Start Search

### 6.Update your Text
#### Date:which you search get
#### Text:you want to update text

<br>

## Note
### 1. Database is on the root-path.(SQLite3)
### 2. run on local area network please run "python3 manage.py runserver 0.0.0.0:8000"

## Warming
# <font color="#f00">It must never be used on production machines and linked on public network!!!<br><br>It must never be used on production machines and linked on public network!!!<br><br>It must never be used on production machines and linked on public network!!!<br><br></font>
## API
### all are based on "127.0.0.1:8000"

### 1. index
#### English home page

### 2. index/zh
#### Chinese home page

### 3. Del
#### Del API
#### e.g.:127.0.0.1:8000/Del/Date
#### Date which you search in the table<br>

### 4. search
#### English search page

### 5. search/zh
#### Chinese search page

### 6. getAccount
#### Get an account
#### e.g.: 127.0.0.1:8000/getAccount
#### return a text

### 7.getPassword_1
#### Get a password
#### e.g.: 127.0.0.1:8000/getPassword_1/
#### return a number

### 8.getPassword_2
#### Get a password
#### e.g.: 127.0.0.1:8000/getPassword_2/
#### return a text

### 9.getPassword_3
#### Get a password
#### e.g.: 127.0.0.1:8000/getPassword_3/
#### return a text

### 10.getPassword_max
#### Get a password
#### e.g.: 127.0.0.1:8000/getPassword_max/
#### return a text

### 11. Save_Result
#### Save data onto the Database
#### e.g.: 127.0.0.1:8000/Save_Result/
#### Method : Post <br> Address : text(no necessary) <br> Account: text(necessary) <br> Password : text(necessary) <br> Text : text(no necessary)

### 12. searched
#### Get the result of Search
#### e.g.: 127.0.0.1:8000/searched/Int/Str
#### Int : 0:Address ; 1:Account ; 2:Password <br> Str : text
#### return a table

### 13. Backup
#### Get the Database backup download.
#### e.g.:127.0.0.1:8000/backup
#### return a db file.

### 14.Update
#### English Update Page
#### e.g.:127.0.0.1:8000/Update

### 15.Update/zh
#### Chinese Update page
#### e.g.:127.0.0.1:8000/Update/zh

### 16.Update_Text
#### Update your text
#### e.g.: 127.0.0.1:8000/Update_Text/str1/str2
#### str1:Date string ; str2:Text string

### 17.login
#### login page
#### e.g.:127.0.0.1:8000/login

### 18.Admin
#### Control pages
#### e.g.:127.0.0.1:8000/Admin