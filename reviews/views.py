# reviews/utils.py
import os
from io import BytesIO

import qrcode
from django.conf import settings
from django.core.files import File


def generate_qr_code(business):
    # Define the URL to be encoded into the QR code, linking to the review page
    qr_data = f"http://127.0.0.1:8000/reviews/{business.id}/rate"

    # Create the QR code
    qr = qrcode.make(qr_data)

    # Save the QR code to a BytesIO stream, then save to the business instance
    qr_io = BytesIO()
    qr.save(qr_io, 'PNG')

    # Define the filename and save without triggering a second save in the model
    business.qr_code.save(f"{business.name}_qr.png", File(qr_io), save=False)
    business.save()  # Save the model to update with the new QR code image path
