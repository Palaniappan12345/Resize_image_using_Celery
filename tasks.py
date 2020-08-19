from celery import Celery
from PIL import Image

app = Celery('tasks', broker='pyamqp://guest@localhost//',backend='amqp')

@app.task

def size(): 
	try: 
		#Relative Path 
		img = Image.open("celery.png") 
		
		#In-place modification 
		img.thumbnail((150, 150)) 
		
		img.save("thumb.png") 
	except IOError: 
		pass

if __name__ == "__size__": 
	size()



