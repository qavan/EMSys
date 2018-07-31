import re
r="{'phrase': {'text': 'юрату', 'language': 'cv'}, 'meanings': [{'language': 'ru', 'text': '&#39;&#39;поэтич. тж.&#39;&#39; passion'}], 'meaningId': -4628189122811928367, 'authors': [1]}"
print(re.sub(r'\, \'meanings\'\: \[\{\'[a-z]*\'\: \'[a-z]*\'\, \'[a-z]*\'\: \'.*\'\}\]','',r))
