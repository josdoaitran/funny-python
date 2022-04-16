# Install qrcode
# pip install qrcode
# pip install image
# Importing library
import qrcode

data_phone = input("Type your phone: ") 
# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)
 
# Adding data to the instance 'qr'
qr.add_data(data_phone)
 
qr.make(fit = True)
img = qr.make_image(fill_color = 'black',
                    back_color = 'white')
 
img.save('MyQRCode.png')