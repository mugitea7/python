import qrcode

qr = qrcode.QRCode()
qr.add_data('Happy Birthday!')
qr.make()

img = qr.make_image()

img.save('qrcode_test.png')
