# python_pw_generator
python password generator

## What does it do
It generate a random string or password
According to specified characters and length

## Usage
```
python main.py [-h] [--length [N]] [--char [C]]
options:
  -h, --help            show this help message and exit
  --length [N], -l [N]  set password length
  --char [C], -c [C]    set characters in password (l -> lowercase) (u ->
                        uppercase) (d -> digits) (s -> symbols)
```  

10 characters including lowercase and digits  
` python main.py -c ld -l 10 `

### can be imported
