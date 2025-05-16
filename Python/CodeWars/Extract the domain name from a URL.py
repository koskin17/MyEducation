# Write a function that when given a URL as a string parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

## ✅ Професійне рішення
# * 🔧 скористатися `re` (регулярні вирази) — просто, гнучко

import re

def domain_name(url):
    return re.search(r'(?:https?://)?(?:www\.)?([^\.]+)', url).group(1)

### 🧪 Пояснення:

# | Частина шаблону  | Що робить                               |
# | ---------------- | --------------------------------------- |
# | `(?:https?://)?` | Необов’язковий `http://` або `https://` |
# | `(?:www\.)?`     | Необов’язковий `www.`                   |
# | `([^\.]+)`       | Група — захоплює **ім’я домену**        |

# 👉 `.group(1)` — повертає саме домен

domain_name("http://google.com") #"google")
domain_name("http://google.co.jp") #"google")
domain_name("https://123.net") #"123")
domain_name("https://hyphen-site.org") #"hyphen-site")
domain_name("http://codewars.com") #"codewars")
domain_name("www.xakep.ru") #"xakep")
domain_name("https://youtube.com") #"youtube")
domain_name("http://www.codewars.com/kata/") #"codewars")
domain_name("icann.org") #"icann")