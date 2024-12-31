import qrcode
import os

# Create a folder to save images if it doesn't exist
if not os.path.exists("images"):
    os.makedirs("images")

# Data to encode
data = "https://www.example.com"  # Change this to any URL or text you want

# Create a QR code
qr = qrcode.QRCode(
    version=1,  # Size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Pixel size for each box in the QR code
    border=4,  # Number of boxes for the border
)

qr.add_data(data)
qr.make(fit=True)  # Ensure the QR code fits the data

# Create an image from the QR code
# Create an image from the QR code with custom colors
img = qr.make_image(fill="blue", back_color="yellow")


# Save the image in the "images" folder
img.save("images/qrcode.png")
