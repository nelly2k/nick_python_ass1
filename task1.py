import urllib.request
import hashlib
from urllib.error import URLError, HTTPError

host = "http://localhost:327691"
studentId = "156"


def input_words():
    words=[]
    while True:
        input_word = input("Please enter a word, If you done, print DONE: ")
        if input_word== "DONE":
            break
        else:
            words.append(input_word)
    return words

def fetch_yes(words):
    yes_words=[]
    for word in words:
        try:
            url = host + "/query?SID="+ studentId + "&Search="+word
            result = urllib.request.urlopen(url).read().decode()
            if result=="YES":
                yes_words.append(word)
        except HTTPError as err:
            print("Server responded with error. Error code: "+ str(err.code) + " word: " + word)
        except URLError:
            print("URL is unavailable. " + host + " word: " + word)
        except:
            print("Unexpected error. word: " + word)
    return yes_words

def print_checksum(yes_words):
    for yes_word in yes_words:
        encoded_word=str(yes_word).encode("utf-8")
        hash_md5 = hashlib.md5()
        hash_md5.update(encoded_word)
        print("Word: " + yes_word)
        print("Checksum: " + hash_md5.hexdigest())

words=input_words()
yes_words=fetch_yes(words)
print_checksum(yes_words)