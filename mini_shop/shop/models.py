from django.db import models
from django.utils.text import slugify # Matnni slug ko'rinishiga keltiruvchi funksiya
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name) or "category"
            slug = base_slug
            counter = 2
            while self.__class__.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "Category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Sotuvchi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Mahsulot kategoriyasi")
    title = models.CharField(max_length=100, verbose_name="Mahsulot nomi")
    description = models.TextField()
    price= models.DecimalField(decimal_places=2, max_digits=10)
    photo = models.ImageField(upload_to="products/", blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "Product"
        verbose_name = "Product"
        verbose_name_plural = "Products"
