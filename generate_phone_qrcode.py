# Install qrcode
# pip3 install qrcode
# Importing library
import qrcode

data_phone = input("Type your phone: ") 
# Data to be encoded
data = data_phone
 
# Encoding data using make() function
img = qrcode.make(data)
 
# Saving as an image file
img.save('phone_qrcode.png')