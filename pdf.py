# Import the pikepdf library
import pikepdf

# Open an existing PDF file named "test.pdf"
old_pdf = pikepdf.Pdf.open("test.pdf")

# Create a pikepdf.Permissions object with the 'extract' permission set to False
no_ext = pikepdf.Permissions(extract=False)

# Save the modified PDF to a new file named "test1.pdf"
# Apply encryption with the specified user and owner passwords, and restrict extraction permissions
old_pdf.save("test1.pdf", encryption=pikepdf.Encryption(user="123456abc", owner="shahrul", allow=no_ext))
