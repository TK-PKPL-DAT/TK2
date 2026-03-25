from django.db import models

class SiteAppearance(models.Model):
    # Menyimpan kode warna HEX (misal: #ffffff)
    background_color = models.CharField(max_length=20, default="#F8FAFC") 

    def __str__(self):
        return "Pengaturan Tampilan Website"