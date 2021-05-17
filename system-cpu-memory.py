import psutil
print(psutil.cpu_percent())
print(psutil.virtual_memory())
print('memory % used:', psutil.virtual_memory()[2])