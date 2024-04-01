from django.db import models
import pandas as pd

# Create your models here.
class Record(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=200)

    @classmethod
    def load_from_csv(cls, csv_path):
        df = pd.read_csv(csv_path)
        records_list = df.to_dict('records')
        records_generator = (
            cls(
                id=row['id'], 
                name=row['name'], 
                price=row['price'],
                quantity=row['quantity'],
                category=row['category'],
            )
            for row in records_list
        )
        cls.objects.bulk_create(records_generator)
        