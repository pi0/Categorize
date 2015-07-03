# Categorize
Categorize files by extension

I wrote this simple script to categorize recovered files by photo-rec utility :)

#Quick install
For a quick and dirty install:

```bash
sudo wget https://raw.githubusercontent.com/pi0/Categorize/master/caregorize.py -O /usr/local/bin/categorize && sudo chmod +x /usr/local/bin/categorize && hash -r && echo "DONE :)"
```  
# Usage
categorize [-h] [-v] src dst  

### positional arguments:  
  src              source directory of files  
  dst              destination directory to move files  
 
### optional arguments:  
  -h, --help       show this help message and exit  
  -v, --verbosity  increase output verbosity  
