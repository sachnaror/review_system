from io import BytesIO

import qrcode
from django.core.files import File
from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    google_business_id = models.CharField(max_length=50)  # Added Google Business ID for linking
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate QR code URL linked to the business ID
        qr_data = f"127.0.0.1:8000/reviews/{self.id}/rate"
        qr = qrcode.make(qr_data)
        qr_io = BytesIO()
        qr.save(qr_io, 'PNG')

        # Save the QR code image to the qr_code field without duplicating saves
        self.qr_code.save(f"{self.name}_qr.png", File(qr_io), save=False)
        super().save(*args, **kwargs)

class Review(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.business.name} - {self.rating} Stars"
