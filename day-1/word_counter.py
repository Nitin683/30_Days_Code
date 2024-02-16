import argparse
import sys

def wordCounter(path):
    try:
        with open(path, "r") as file:
            text = file.read()
            
    except FileNotFoundError:
        print("Error: File not found")
    except IOError:
        print("Error: Could not read the file")
    word_list = text.split() 
    return len(word_list)  
parser = argparse.ArgumentParser(description='Count words in a text')
parser.add_argument('--path', type=str, required=True, help = "To check the the total numbers of words in a .txt file type --path and enter the path of file")
args = parser.parse_args()

file_content = wordCounter(args.path)
if file_content is not None:
    sys.stdout.write(str(file_content))