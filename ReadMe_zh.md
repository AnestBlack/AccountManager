# Account Manage v3.3
 此程序基于 python3.6.3 和 django-2.0.3
 <br>
##### 语言 : <a href='ReadMe.md'>English</a> <a href='ReadMe_zh.md'>简体中文</a>

## 重要历史记录
### 2018-07-25 : v3.2 不再支持v3.2前面的版本数据库
### 请使用Tool/Database_Update_to_3.2.py 来更新你的数据库，复制你的数据库到Tool然后运行Database_Update_to_3.2.py，备份好你原来的数据库并移动New_Database.db到根目录替换原来的！



## 用法:
### 0. 设置 "MyCode"
#### 用文本编辑软件打开(非windows自带的笔记本) encypt.py(v3/encypt.py), 把 'anyword' 改成任意正常范围内的数字和字母，并去掉右边的"+"
#### 例:<br>MyCode='8uj98hy_*asd'
#### <font color="#f00">请不要把MyCode设置成和例子中相同！！！</font>

### 1.在根目录复制一份"Database.example.db"然后粘贴在根目录并重命名为"Database.db"

### 2. 输入 "manage.py runserver"
#### 例: Windows : 运行"Start.bat"，如果装有两个版本的python请自行修改bat文件 :)
#### Linux : 输入 "python3 manage.py runserver"

### 3. 用任意浏览器打开网址( 127.0.0.1:8000 )
#### 例: Windows : 在cmd中输出 "start 127.0.0.1:8000"
#### Linux 输入 "w3m 127.0.0.1:8000"

### 4. 开始你的工作
#### 地址 : 你需要注册的网址.
#### 帐号 :如果你想要自定义帐号,输入框内并在"自定义帐号"后打勾, 否则你不需要输入任何东西并且不用在"自定义帐号"后打勾
#### 生成 : 程序开始的按钮.
#### 下面的单选框 : 在你需要保存的密码右边打勾
#### 保存结果 : 保存地址和在"生成结果"下面的帐号以及打勾的密码

### 5. 搜索你保存在数据库中的数据
#### 填入你能记住的地址，帐号或密码中一项,并在右边打勾
#### 搜索 : 开始搜索
<br>

## 注

### 1. 数据库在根目录.(SQLite3)

### 2. 在局域网上运行请在根目录下cmd中输入"python3 manage.py runserver 0.0.0.0:8000"

<br>
## 警告

# <font color="#f00">1. 禁止用于生产环境与开放于公网!!!<br><br>禁止用于生产环境与开放于公网!!!<br><br>禁止用于生产环境与开放于公网!!!<br><br></font>

## API

### 全部基于 "127.0.0.1:8000"

### 1. index
#### 英文主页

### 2. index/zh
#### 中文主页

### 3. Del
#### 删除接口
#### 例:127.0.0.1:8000/Del/Date
#### Date 输入搜索结果中的日期

### 4. search
#### 英文搜索界面

### 5. search/zh
#### 中文搜索界面

### 6. getAccount
#### 获得帐号
#### 例: 127.0.0.1:8000/getAccount/Str
#### Str : 无空格字符串
#### 返回一个字符串

### 7.getPassword_1
#### 获得密码
#### 例: 127.0.0.1:8000/getPassword_1/Str1/Str2
#### Str1 : 无空格字符串 <br> Str2 : 无空格字符串
#### 返回一串数字

### 8.getPassword_2
#### 获得密码
#### 例: 127.0.0.1:8000/getPassword_2/Str1/Str2
#### Str1 : 无空格字符串 <br> Str2 : 无空格字符串
#### 返回一个字符串

### 9.getPassword_3
#### 获得密码
#### 例: 127.0.0.1:8000/getPassword_3/Str1/Str2
#### Str1 : 无空格字符串 <br> Str2 : 无空格字符串
#### 返回一个字符串

### 10.getPassword_max
#### 获得密码
#### 例: 127.0.0.1:8000/getPassword_max/Str1/Str2
#### Str1 : 无空格字符串 <br> Str2 : 无空格字符串
#### 返回一个字符串

### 11. Save_Result
#### 保存数据进数据库
#### 例: 127.0.0.1:8000/Save_Result/Str1/Str2/Str3
#### Str1 : 地址字符串 <br> Str2 : 帐号字符串 <br> Str3: 密码字符串

### 12. searched
#### 获得搜索结果
#### 例: 127.0.0.1:8000/searched/Int/Str
#### Int : 0:地址 ; 1:帐号 ; 2:密码 <br> Str : 所需要搜索的字符串
#### 返回一个table标签

### 13. Backup
#### 下载数据库备份
#### 例:127.0.0.1:8000/backup
#### 返回一个db文件
