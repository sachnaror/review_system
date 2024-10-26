# reviews/utils.py
import qrcode
from django.conf import settings
import os

def generate_qr_code(business):
    # Generate Google Review URL using Google Business ID
    google_review_url = f"https://search.google.com/local/writereview?placeid={business.google_business_id}"

    # Generate QR code image
    qr = qrcode.make(google_review_url)
    qr_path = os.path.join(settings.MEDIA_ROOT, 'qr_codes', f'{business.id}.png')
    qr.save(qr_path)

    # Save QR code path to business instance
    business.qr_code = f'qr_codes/{business.id}.png'
    business.save()
