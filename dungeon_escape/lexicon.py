class Lexicon(object):
    
    directions = ['north', 'south', 'west', 'east', 'north-east', 'south-east', 
                  'south-west', 'north-west', 'up', 'down', 'left', 'right']
    
    verbs = ['attack', 'go', 'move', 'kill', 'eat', 'close', 'flee', 
               'shoot', 'throw', 'take', 'open', 'run']
    
    stopWords = ['the', 'in', 'of', 'on', 'from', 'at', 'it', 'a', 'with', 
                 'to', 'or', 'and']
    
    nouns = ['door', 'chest', 'sword', 'knife', 'goblin', 'treasure', 
             'picture', 'window']
    
    def get_input(self):
    	userInput = raw_input('> ')
    	return userInput.lower()
    
    def scan(self, userInput):
    	sentence = userInput.split()
    	found = False
    	output = []
    	for word in sentence:
    		if not found:
    			for direction in self.directions:
    				if word == direction:
    					output.append(('direction', word)) 
    					found = True
    		if not found:
    			for verb in self.verbs:
    				if word == verb:
    					output.append(('verb', word))
    					found = True
    		if not found:
    			for stop in self.stopWords:
    				if word == stop:
    					output.append(('stop', word))
    					found = True
    		if not found:
    			for noun in self.nouns:
    				if word == noun:
    					output.append(('noun', word))
    					found = True
    		if not found:
    			try:
    				output.append(('number', int(word)))
    				found = True
    			except ValueError:
    				output.append(('error', word))		
    		
    		found = False #reset found for next word
    		
    	return output