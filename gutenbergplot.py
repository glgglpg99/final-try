
import matplotlib.pyplot as plt
import requests
import nltk
from bs4 import BeautifulSoup

def gutenberg_plot(url):
	import requests
	response = requests.get(url)
	soup = BeautifulSoup(requests.text, 'html.parser')
	words = soup.get_text()
	lowered = []
	for word in words:
		lowered.append(word.lower())




  
    
    
    
    
    	
    
    
    

