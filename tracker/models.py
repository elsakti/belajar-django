from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100);

    def __str__(self):
        return self.name;

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('IN', 'Income'),
        ('OUT', 'Expense'),
    )

    title = models.CharField(max_length=100);
    amount = models.DecimalField(max_digits=10, decimal_places=2);
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES);
    category = models.ForeignKey(Category, on_delete=models.CASCADE);
    date = models.DateField();

    def __str__(self):
        return f"{self.title} - {self.amount}"