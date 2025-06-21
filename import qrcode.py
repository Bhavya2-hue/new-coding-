import qrcode

# Get user input
data = input("Enter the text or URL to generate QR code: ")

# Create QR code object
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code
    box_size=10,  # size of each box in pixels
    border=5  # border size (min: 4)
)

qr.add_data(data)
qr.make(fit=True)

# Generate the image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("my_qrcode.png")

print("✅ QR Code generated and saved as my_qrcode.png")