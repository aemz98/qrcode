import qrcode

data = 'Prueba de QR'

img = qrcode.make(data)

img.save('C:/Users/aemz9/Pictures/imagenesqr/primero.png')