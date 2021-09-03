import requests as req
import json as j
from tkinter import Tk  



def getFormatString(str):
	return "| "+str+" "*(99-len(str))+"|"

def getDictionary(word):
		try:
			print("******** word: "+word+"********")
			res = req.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+word)
			meanings_list = res.json()[0]['meanings']
			for i in range(len(meanings_list)):
				print("+"+"-"*100+"+")
				print(getFormatString("Definition: "+ str(i+1)))
				try:
					def_obj = meanings_list[i]['definitions'][0]
					print(getFormatString("definition: ****  "+def_obj['definition']+"  ****"))
					print(getFormatString("Parts of speech: "+meanings_list[i]['partOfSpeech']+""))
					print(getFormatString("example: "+def_obj['example']))
				except:
					print("|   Something went wrong!")
			print("+"+"-"*100+"+\n")	
			print(res)
		except : 
			print("No response")


prev = ''

while(True):
	word1 = ''
	r = Tk()
	try:
		word1 = r.clipboard_get()
		if(word1 != '' and word1 != prev):
			getDictionary(word1)
		prev = word1
	except:
		print("ERROR!") 
	r.destroy()
		
