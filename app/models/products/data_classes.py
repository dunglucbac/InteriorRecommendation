"""
Data class for products.
"""
from dataclasses import dataclass
# from typing import List

@dataclass
class Product:
    """
    Data class for products.
    """
    name: str
    url: str
    img: str
    price: str
    cat: str

    @staticmethod
    def deserialize(row):

        """
        Deserialize a row in the DataFrame
        """
        if not row.empty:
            return Product(
                name=row['name'],
                url=row['url'],
                img=row['img'],
                price=row['price'],
                cat=row['cat']
            )