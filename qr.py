import qrcode
from PIL import Image

# Function to generate QR code with custom security level and colors
def generate_custom_qr(data, error_correction_level='L', box_size=10, border=4, fill_color="black", back_color="white", filename="custom_qr_code.png"):
   
    
    # Map the error correction level to the constants from qrcode library
    error_correction_map = {
        'L': qrcode.constants.ERROR_CORRECT_L,
        'M': qrcode.constants.ERROR_CORRECT_M,
        'Q': qrcode.constants.ERROR_CORRECT_Q,
        'H': qrcode.constants.ERROR_CORRECT_H
    }

    # Create a QR code instance with user-defined parameters
    qr = qrcode.QRCode(
        version=1,
        error_correction=error_correction_map[error_correction_level],
        box_size=box_size,
        border=border
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code with custom colors
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Save the image
    img.save(filename)

    print(f"QR code generated and saved as {filename}")


# Example usage
if __name__ == "__main__":
    # User inputs
    data_to_encode = input("Enter the data to encode (e.g., URL or text): ")

    print("Choose Error Correction Level (L, M, Q, H):")
    print("L - 7%  of code can be restored")
    print("M - 15% of code can be restored")
    print("Q - 25% of code can be restored")
    print("H - 30% of code can be restored")
    error_correction_level = input("Enter error correction level (L, M, Q, H): ").upper()

    box_size = int(input("Enter the box size (default 10): ") or 10)
    border_size = int(input("Enter the border size (default 4): ") or 4)

    fill_color = input("Enter the fill color (default black): ") or "black"
    back_color = input("Enter the background color (default white): ") or "white"

    filename = input("Enter the filename to save the QR code (default custom_qr_code.png): ") or "custom_qr_code.png"

    # Generate the custom QR code
    generate_custom_qr(
        data=data_to_encode,
        error_correction_level=error_correction_level,
        box_size=box_size,
        border=border_size,
        fill_color=fill_color,
        back_color=back_color,
        filename=filename
    )
