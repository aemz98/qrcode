import qrcode

data = 'Prueba de QR'

# img = qrcode.make(data)

# img.save('C:/Users/aemz9/Pictures/imagenesqr/primero.png')

qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color = 'red', back_color = 'black')

img.save('C:/Users/aemz9/Pictures/imagenesqr/segundo.png')