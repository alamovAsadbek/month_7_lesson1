from django.db import models


class CategoryModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class CompanyModel(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "company"
        verbose_name_plural = "companies"


class ColorModel(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "color"
        verbose_name_plural = "colors"


class TagModel(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"


class ProductModel(models.Model):
    photo_1 = models.ImageField(upload_to="products", null=True, blank=True)
    photo_2 = models.ImageField(upload_to="products", null=True, blank=True)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    in_stock = models.BooleanField(default=True)

    categories = models.ManyToManyField(CategoryModel, related_name="products")
    tags = models.ManyToManyField(TagModel, related_name="products")
    colors = models.ManyToManyField(ColorModel, related_name="products")
    companies = models.ManyToManyField(CompanyModel, related_name="products")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"


class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="products")

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "product image"
        verbose_name_plural = "product images"

