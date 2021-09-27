from urllib.request import urlopen, HTTPError, URLError
from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
    """HTML parser for removing the tags from the web page for analysing"""
    a = []
    def handle_data(self, data):
        self.a.append(data)

def read_url(url):
    """Read url page and try to decode it to utf-8"""
    print("Retrieve URL")
    try:
        with urlopen(url) as response:
            print("Opening file")
            try:
                data = response.read().decode("utf-8")
                return data
            except:
                print("File is not using utf-8 encoding")
                return 999
    except URLError:
        print("Error opening url")
    except HTTPError:
        print("Page not found")
    except ValueError:
        print("Invalid URL")

def save_page(page):
    """Save page"""
    path = file_path()
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(page)
            print("page saved")
    except PermissionError:
        print("Permission denied. Saving the file failed.")
    except OSError as err:
        print("OS error:", err)
        print("Saving failed.")

def save_file(file):
    """Save file as binary mode"""
    with urlopen(file) as response:
        data = response.read()
        path = file_path()
        try:
            with open(path, "wb") as f:
                f.write(data)
                print("file saved")
        except PermissionError:
            print("Permission denied. Saving the file failed.")
        except OSError as err:
            print("OS error:", err)
            print("Saving failed.")


def search_dangerous_words(url):
    """Analyse the web page's content for dangerous words"""
    danger = ["bomb", "kill", "murder", "terror", "terrorist", "terrorists", "terrorism"]
    dangerous_words = 0
    parser = MyHTMLParser()
    parser.feed(url)
    parsed_url = ' '.join(parser.a)
    for word in danger:
        s = re.compile(f"[\W]{word}[\W]",re.IGNORECASE)
        count = len(re.findall(s,parsed_url))
        print(f"{word} found {count} times")
        dangerous_words = dangerous_words + count

    print(f"Dangerous words found {dangerous_words} times")

def file_path():
    """Ask user path for file saving"""
    s = input("Give me a valid path to save the contents: ")
    return s

#Main program starts
while True:
    url = input("Give me a valid URL to download (enter exits): ")
    if not url:
        break
    else:
        filee = read_url(url)
        if not filee:
            print(f"Error opening url: {url}")
            break
        if filee == 999:
            save_file(url)
            break
        else:
            search_dangerous_words(filee)
            save_page(filee)
            break