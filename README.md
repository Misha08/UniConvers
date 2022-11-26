# The UniConvers V 0.75

😺 The program "UniConverse", which allows you to transfer currency at the current rate, is ready for use ❕ 
<br />
<br />

### **You can transfer 5 currencies in the world at a favorable rate, such as:**
<br />

<ul>
    <li>✅ US Dollars (USD) </li>
    <li>✅ Euros (EUR) </li>
    <li>✅ Serbian Dinars (RSD) </li>
    <li>✅ Pounds (GBP) </li>
    <li>✅ Norwegian Kroner (NOK) </li>
</ul>
<br />
<br />

### **Also, the program can greet you in five languages! :), such as:**
<br />

<ul>
    <li>✅<img src="https://th.bing.com/th/id/OIP.lcElUjxX_dDwCNCb3KkG9QHaEo?pid=ImgDet&rs=1" style="width: 20px">English </li>
    <li>✅<img src="https://th.bing.com/th/id/R.20cca07dfda89b5054b68e5b54e2ddc0?rik=tLso0pVAlNKO9w&riu=http%3a%2f%2fwww.hqwallpapers.ru%2fwallpapers%2fflags%2fflag-serbii-774x435.jpg&ehk=AyW4Xr2XqoteTTUHmmKUhE3h%2fWJg9dgv6q4%2ftg522y8%3d&risl=&pid=ImgRaw&r=0"style="width: 20px"> Serbian </li>
    <li>✅<img src="https://th.bing.com/th/id/R.c69fe03f837a2557067c770656beda72?rik=xNJzv5LcCeFLAw&pid=ImgRaw&r=0" style="width: 20px"> German </li>
    <li>✅<img src="https://th.bing.com/th/id/OIP.OV6AUPcF7B_dxdEcgMZCdQHaE8?w=303&h=202&c=7&r=0&o=5&dpr=1.3&pid=1.71" style="width: 20px"> French </li>
    <li>✅<img src="https://th.bing.com/th/id/R.9d7997e4e13b1c737217f8d1a3f1c6f5?rik=2tCsgtAE5w6xoA&riu=http%3a%2f%2fechesters.co.uk%2fimages%2fposts%2fflag-of-spain.png&ehk=t0cUSAxXePoXOokg%2bPWqCFoxqJQ%2bXhrIA3V%2b9QQEeoM%3d&risl=&pid=ImgRaw&r=0" style="width: 20px"> Spanish </li>
</ul>
<br />
<br />

**💥 The program is made on the version of Python 3.11 💥**
<br />
<br />

❔ Every day, millions of people travel around Europe, and each of them faces a constant problem when exchanging currency, I hope my program will help solve this problem a little :) ❗
<br />
<br />

### 👋 At the beginning, you are only shown welcome words once, because how can you not greet users on five languages!!!:
<br />

```python 
def print_hello_text_eng():
    print("///__________________________________________________///")
    print("///               Hello my dear user :)              ///")
    print("///   You are welcomed by the 'UniConverse' program  ///")
    print("///Here you can transfer currency at the current rate///")


def print_hello_text_fr():
    print("///_____________________________________________________///")
    print("///           Bonjour mon cher utilisateur :)           ///")
    ...
...
```
<br />
<br />

### 
**👉 But first you need to choose a language, language selection is carried out using a special function inside the _"Switches.py"_ file:**
<br />

### 🔧 directly a function from a construction file:
```python 
# Function of the choice the languages
def get_choice_language_1():
    print("???--------------------???")
    print("Please, choose your lang:)")
    print("1 - English")
    print("2 - Deutsch")
    print("3 - Српски")
    print("4 - Français")
    print("5 - Espagnol")
    print("???--------------------???")
```

### 🔧 A function that allows you to make a selection by a given parameter:
```python 
# Help functions
# Provides a choice a Method for Calculating Certain Values
def get_choice():
    choice = int(input("Enter your choice: "))
    return choice
```
### 🔧🔑 language selection function, by comparing values
```python
# Directly switch functions
# Function of the choice the language
def set_language_switch(choice):
    match choice:
        case 1:
            return print_hello_text_eng()
        case 2:
            return print_hello_text_de()
        case 3:
            return print_hello_text_srb()
        case 4:
            return print_hello_text_fr()
        case 5:
            return print_hello_text_sp()
```

### 📢🚩Recall is prevented by changing the entry in the text file:
```python 
# Open the text files with switch parameters
def open_text_document(doc_name: str):
    with open(doc_name, "r+", encoding="UTF-8") as rw_file:
        doc = rw_file.read()

    return doc


# Get information about the switch status of functions
def get_info_from_document(doc: str):
    info = doc.split(":")
    return info


# Write information only in the document about the switch status of functions
def write_text_to_document(doc_name: str):
    with open(doc_name, "r+", encoding="UTF-8") as rw_file:
        doc = rw_file.read()
        rw_file.write(doc.split(":")[0] + "False")
```
### 🔧🚩Main function to transfer a certain amount of currency to another:
```python 
# Main logical function in the Program
def change_the_currency(currency_1: str, currency_2: str, amount: int):
    return str(converter.convert(currency_1, currency_2, amount))
```

### 🔧📜Functions - switches between possible currencies for transfer:
```python
# Function of getting the currency, which you want to change from
def get_currency_switch_1(choice):
    match choice:
        case 1:
            return "EUR"
        case 2:
            return "USD"
        case 3:
            return "RSD"
        case 4:
            return "GBP"
        case 5:
            return "NOK"


# Function of getting the currency, which you want to change to
def get_currency_switch_2(choice):
    match choice:
        case 1:
            return "EUR"
        case 2:
            return "USD"
        case 3:
            return "RSD"
        case 4:
            return "GBP"
        case 5:
            return "NOK"
```

### 🔰 _And the final function that displays the result of the transfer from one currency to another_

```python
# Main constructional function in the Program
def get_currencies():
    print("///-///")
    print("1 - EUR")
    print("2 - USD")
    print("3 - RSD")
    print("4 - GBP")
    print("5 - NOK")
    print("///-///")
    print("First - from")
    print("Second - to")
    curr_1 = get_currency_switch_1(get_choice())
    curr_2 = get_currency_switch_2(get_choice())
    amm = int(input(f"How many {curr_1} do you want to exchange to {curr_2}: "))
    final_words = f"The amount of {curr_1} you entered equals the number of {curr_2} equals: "
    return final_words + change_the_currency(curr_1, curr_2, amm)
```

<h2 style="text-align: center"> Summarice </h2>
<p style="text-align: center; font-size: 15px"> it took about 3 days to develop this program, and for the first time I changed the logical class to implement the main logic of the program, work was also done on designing function and parameter transfers through other files! </p>


