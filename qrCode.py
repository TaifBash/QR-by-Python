# importing the qrcode library
import qrcode
# generating a QR code using the make() function
qr_img = qrcode.make("https://twitter.com/@6ai00")
# saving the image file
qr_img.save("MYtwiter.png")