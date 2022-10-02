import pyspeedtest 

data = pyspeedtest.SpeedTest()

down = data.download()
up = data.upload()

print("Download speed is: ", down)
print("Upload speed is: ", up)