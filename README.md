# HUDL Login Automation

In this automation project created using **Selenium Python + BDD(Behave)** we test the HUDL login page.

## Which software do you need to run this project?

* Windows 11
* Python 3.11.2 [Download here](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)
* Pip 23.0.1
* Behave 1.2.6

```bash
pip install behave
```

* Selenium library 4.8.2

```bash
pip install selenium
```

### To debug

We have used this IDE to develop this project:

* PyCharm Community 2022.3.3 [Download here](https://www.jetbrains.com/pycharm/download/#section=windows)

## Usage

1. Clone the project in your PC
2. Open Terminal
3. Point terminal into hudlProhect location
4. Run the command:

```bash
<hudlProject_location> behave --junit
```

5. When execution finish you will find the report on reports folder inside project directory

### Why --junit ?

We run it with the command --junit to generate a little report inside reports folder at hudlProject directory

## Scope of testing

* Logo in HUDL login page                                                       
* Email input is present                                                        
* Password input is present                                                     
* Log in button works                                                            
* Try other sections links                                                                                                                 
* Log in with existing user                                                      
* Log in with wrong data                                                 