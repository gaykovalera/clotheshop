from django.core.exceptions import ValidationError
from django.db.models.fields.files import ImageFieldFile

MIN_BRAND_WIDTH = 400
MIN_BRAND_HEIGHT = 400


def validate_brand(image: ImageFieldFile) -> None:
    if image.width < MIN_BRAND_WIDTH or image.height < MIN_BRAND_HEIGHT:
        raise ValidationError(
            f'Разрешение изображения должно быть не'
            f' менее {MIN_BRAND_WIDTH}x{MIN_BRAND_HEIGHT}'
        )


MIN_PRODUCT_WIDTH = 400
MIN_PRODUCT_HEIGHT = 400


def validate_product(image: ImageFieldFile) -> None:
    if image.width < MIN_PRODUCT_WIDTH or image.height < MIN_PRODUCT_HEIGHT:
        raise ValidationError(
            f'Разрешение изображения должно быть не'
            f' менее {MIN_PRODUCT_WIDTH}x{MIN_PRODUCT_HEIGHT}'
        )
