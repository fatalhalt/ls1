# ls1

ls1 is unix ls inspired handy utility for computing total sizes of subdirectories and files of given path 1 level deep written in Python 3.
ls1 allows you to quickly identify large directories while being much simpler to use than 'du -h'. ls1 also allows sorting output.

### Installation

Included are ls1.py and ls1 python files, they're identical except that first one is meant for Windows as it uses CRLF line terminators

On GNU/Linux or MacOS you can copy 'ls1' file to ~/bin/ or /usr/local/bin/ directory
```sh
# cp ls1 /usr/local/bin/
# chmod +x /usr/local/bin
```

For Windows, I included a wrapper ls1.bat batchfile allowing to launch this utility directly by simply typing 'ls1' in command prompt
```sh
cd %USERPROFILE%
md bin
copy ls1.py and ls1.bat to bin
add %USERPROFILE%\bin to PATH
```
you always have option of putting files into System32

### Usage

```sh
$ ls1
usage: ls1 [-h] [-S] [-r] path

-S
	sort by file size, smallest first
-r, --reverse
	reverse order while sorting

```

### Example

```sh
C:\Users\kyle>ls1 -S -r D:\Games
d    75.9GB Destiny 2
d    68.2GB Battlefield 4
d    47.6GB Assassin's Creed Origins
d    33.7GB BnS
d    27.3GB The Witcher 3 Wild Hunt
d    16.3GB Overwatch
d    14.3GB Crysis 3
d    10.7GB EVE
d   542.6MB (TH15) Touhou Kanjuden ~ Legacy of Lunatic Kingdom
d   445.7MB (TH16) Touhou Tenkuushou ~ Hidden Star in Four Seasons
```
