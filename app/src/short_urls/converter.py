import numbers

class Converter:

    def __init__(self):
        self.map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def id_to_shortURL(self, id):

        if isinstance(id, str) :
            raise Exception('id must be an integer')

        shortURL = ""
            
        # for each digit find the base 62
        while(id > 0):
            shortURL += self.map[id % 62]
            id //= 62

        # reversing the shortURL
        return shortURL[len(shortURL): : -1]
 
    def shortURL_to_id(self, shortURL):

        if isinstance(shortURL, numbers.Number):
            raise Exception('id must be a string')

        my_id = 0
        for i in range(len(shortURL)):
            val_i = ord(shortURL[i])
            idx = len(shortURL) - i - 1
            if(val_i >= ord('a') and val_i <= ord('z')):
                my_id += 62**idx * (val_i - ord('a'))
            elif(val_i >= ord('A') and val_i <= ord('Z')):
                my_id += 62**idx * (val_i - ord('A') + 26)
            else:
                my_id += 62**idx * (val_i - ord('0') + 52)