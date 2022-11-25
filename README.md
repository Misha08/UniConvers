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


### directly a function from a construction file:
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

### directly a function from a construction file:
