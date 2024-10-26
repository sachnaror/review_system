from io import BytesIO

import qrcode
from django.conf import settings
from django.core.files import File
from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=200)
    google_business_id = models.CharField(max_length=100, unique=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Only generate a QR code if it doesn't already exist
        if not self.qr_code:
            # Create QR code
            qr = qrcode.make(self.google_business_id)  # You can customize this with a URL or other info
            buffer = BytesIO()
            qr.save(buffer, format='PNG')
            file_name = f'qr_code_{self.name}.png'
            # Save QR code image to the model
            self.qr_code.save(file_name, File(buffer), save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
