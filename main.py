import qrcode
from qrcode.constants import ERROR_CORRECT_L

def generate_qr_code(data: str, filename: str = "qr_code.png"):
    """
    Generates a professional-looking QR code from the given data and saves it to a file.

    Args:
        data (str): The string data to encode (e.g., a URL).
        filename (str): The name of the output image file (default: "qr_code.png").
    """
    # 1. Configuration of the QR code object
    # version=None: Auto-selects the smallest version number based on data.
    # error_correction=L: Low error correction (about 7% of data can be restored).
    # box_size=10: Sets the size of each box/pixel in the QR code.
    # border=4: Sets the minimum size of the white border around the code.
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # 2. Add data to the QR object
    qr.add_data(data)
    # The 'fit=True' argument ensures the code structure is optimized for the data.
    qr.make(fit=True)

    # 3. Create the image object
    # Defines the colors for the modules (fill) and the background.
    img = qr.make_image(fill_color="black", back_color="white")

    # 4. Save the image to the specified file
    img.save(filename)
    print(f"QR code successfully generated and saved as '{filename}'")

# --- Execution Block ---

# Data to be encoded (Your GitHub profile)
encoded_data = "https://github.com/hrosicka"

# Generate and save the QR code using the function
generate_qr_code(data=encoded_data, filename="my_github_qr.png")