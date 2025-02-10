# **L A B &emsp; R E M O T E &emsp; A C C E S S**

> Author :: **`D A R S H A N  S (GitHub/azuregray)`**

> My Identity >>  [**`Github`**](https://github.com/azuregray/)


### *`LAB HELPER` - A remote access hub that can be used to easily access your desired data files.*
#### *Welcome to Engineering!*

> **`SPECIAL NOTE FROM AUTHOR`** :: I am turning this repo into a Public Archive as I deem that no further changes are required for the repository. Please continue reading to know how this repo might be of great help for you.  


> Oh wait!! There are no files in the repo other than a README! Yes, ofcourse.  
> Feel free to fork this repo to your own GitHub account and then populate it with files in the root folder itself so that you won't need to type longer commands 😉  

---
## **U S A G E**

## **W I N D O W S**

### Single File needs a *Single Command*:
```
(iwr -uri *UrlDirectToFile* ).content | clip
```
---
### Multiple Files simplified by a _Function_:
> _NOTE: You can write the whole function in a single line too.._

- **Function Definition as a BLOCK:**
```
function gcl{
param(
[parameter(mandatory=$true, position=0)]
[string] $uri)
(iwr -uri $uri).content | clip
}
```
- **Function definition _InLine_:**
```
function gcl{ param([parameter(mandatory=$true, position=0)] [string] $uri) (iwr -uri $uri).content | clip }
```

- **Usage of Inline Function:**
```
gcl UrlDirectToFile
```

- **Undefine the function:**
```
remove-item function:\gcl
```
---
### Repeated Fetching easier with _ForEach_ loop:

##### FOREACH LOOP SYNTAX

> rangeSTART.....rangeEND | foreach { command_with_($)sign_at_loopingPosition }

##### Examples: 
- For fetching _program1.html_ >> _program12.html_:
```
1..12 | foreach {iwr -uri https​://raw.githubusercontent.com/azuregray/LabHelper/main/program$($_).html -outfile program$($_).html}
```
- For fetching _q51.txt_ >> _q55.txt_:
```
1..5 | foreach {iwr -uri https​://raw.githubusercontent.com/azuregray/LabHelper/main/q5$($_).txt -outfile q5$($_).txt}
```

## **L I N U  X**

### Simplest on Linux:
- For fetching a single file:
  ```
  curl -s *UrlDirectToFile* | xclip -selection clipboard
  ```

- For fetching multiple files, use a loop:
  Let's say _program1.html_ >> _program5.html_:
  ```
  numbers=(1 2 3 4 5); for i in "${numbers[@]}"; do curl -s https​://raw.githubusercontent.com/azuregray/LabHelper/main/program${i}.html; done | xclip -selection clipboard
  ```
  or perhaps, _q51.txt_ >> _q56.txt_:
  ```
  numbers=(1 2 3 4 5); for i in "${numbers[@]}"; do curl -s https​://raw.githubusercontent.com/azuregray/LabHelper/main/q5${i}.txt; done | xclip -selection clipboard
  ```

---
### _**UriDirectToFile**_ for your repo after forking might look something like:

> https​://raw.githubusercontent.com/<span><</span>GithubUsername<span>></span>/LabHelper/main/<span><</span>FileName<span>></span>

---
 ### _**UriDirectToFile**_ for me for this repo is as follows:

> https​://raw.githubusercontent.com/azuregray/LabHelper/main/<span><</span>FileName<span>></span>

---
