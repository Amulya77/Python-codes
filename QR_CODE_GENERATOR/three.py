import qrcode
import re  # Importing regular expression module

def generate_qr_code():
    url = input("Enter the website URL: ")
    fill_color = input("Enter the fill color (e.g., red, blue, etc.): ")
    back_color = input("Enter the background color (e.g., white, black, etc.): ")

    qr = qrcode.QRCode(version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_H,
                        box_size=10, border=4)
    
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Using regular expression to replace invalid characters in the URL for the filename
    file_name = re.sub(r'\W+', '', url) + "_QR.png"
    img.save(file_name)
    print(f"QR Code generated and saved as {file_name}")

# Generate QR code based on user input
generate_qr_code()
