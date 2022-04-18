#trie node 
#use hashmap has children {"a": TrieNode(), "b": TrieNode()}
#isWord will represent if this trie node indicates if its a valid word 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    #root will include max of 26 alphabet letters
    def __init__(self):
        self.root = TrieNode()

    #when inserting, add each char to its list of children or keep traversing if it already exists 
    def insert(self, word: str) -> None:
        current = self.root
        
        #add to hashmap of children if character doesnt exist in children of current
        #else keep going down the path of that character
        for char in word:
            if char not in current.children:
                #if char doesnt exist, add to children of current
                current.children[char] = TrieNode()
        
            current = current.children[char]
        
        #mark last letter as a valid word
        current.isWord = True
        print("Inserted word: " + word)
    
    #when searching, you need to check if every character exists 
    #and when you get to last char, you need to make sure that char is marked as valid word (at the point of insert)
    def search(self, word: str) -> bool:
        current = self.root
        
        #check if every char exists
        for char in word:
            if char not in current.children:
                print("Did not find word: " + word)
                return False
            current = current.children[char]
        
        print("Found word: " + word)
        #check if last char is marked as a word
        return current.isWord

    #very similar to search except you don't care if last letter is word or not
    #as long as you're able to go to end, you can say prefix exists - doesnt matter if prefix is word or not
    def startsWith(self, prefix: str) -> bool:
        current = self.root
        
        #check if every char exists
        for char in prefix:
            if char not in current.children:
                print("Did not find prefix: " + prefix)
                return False
            current = current.children[char]
        
        print("Found prefix: " + prefix)
        #if you've got this far, means every char exists and hence prefix exists
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()

word = "apple"
obj.insert(word)

word = "fa"
param_2 = obj.search(word)

prefix = "app"
param_3 = obj.startsWith(prefix)
