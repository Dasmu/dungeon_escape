directions = ['north', 'south', 'west', 'east', 'north-east', 'south-east', 
              'south-west', 'north-west', 'up', 'down', 'left', 'right']

actions = ['attack', 'go', 'move', 'kill', 'eat', 'close', 'flee', 'shoot', 
           'throw', 'take', 'open', 'run']

stopWords = ['the', 'in', 'of', 'on', 'from', 'at', 'it', 'a', 'with', 'to', 
             'or', 'and']

objects = ['door', 'chest', 'sword', 'knife', 'goblin', 'treasure', 'picture',
           'window']

def get_input():
	userInput = raw_input('> ')
	return userInput.lower()

def scan(userInput):
	sentence = userInput.split()
	found = False
	output = []
	for word in sentence:
		if not found:
			for direction in directions:
				if word == direction:
					output.append(('direction', word)) 
					found = True
		if not found:
			for action in actions:
				if word == action:
					output.append(('action', word))
					found = True
		if not found:
			for stop in stopWords:
				if word == stop:
					output.append(('stop', word))
					found = True
		if not found:
			for obj in objects:
				if word == obj:
					output.append(('object', word))
					found = True
		if not found:
			try:
				output.append(('number', int(word)))
				found = True
			except:
				output.append(('error', word))			
		
		found = False #reset found for next word
		
	return output