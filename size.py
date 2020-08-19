from celery import Celery
from PIL import Image

app = Celery('tasks', broker='pyamqp://guest@localhost//',backend='amqp')

@app.task
def resize(foo):
    
    foo = Image.open("/home/palaniappan/Documents/celery/celery.png")
    foo.size
    (200,374)
 # I downsize the image with an ANTIALIAS filter (gives the highest quality)
    foo = foo.resize((160,300),Image.ANTIALIAS)
    foo.save("/home/palaniappan/Documents/celery/outputn2.png",quality=95)
 # The saved downsized image size is 24.8kb
    foo.save("/home/palaniappan/Documents/celery/outputn3.png",optimize=True,quality=95)
    
 # The saved downsized image size is 22.9kb
 # My image is a 200x374 jpeg that is 102kb large
    return foo()

