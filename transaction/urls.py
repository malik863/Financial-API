from django.urls import path
from .views import *


urlpatterns = [
    
    path('', list_transactions, name='transaction_list'),
    path('create/', create_transaction, name='create_transaction'),
    path('update/<int:pk>/', update_transaction, name='update_transaction'),
    path('delete/<int:pk>/', delete_transaction, name='delete_transaction'),
    path('api/transactions/', TransactionListAPIView.as_view(), name='api-transaction-list'),
    path('api/transactions/<int:pk>/', TransactionDetailAPIView.as_view(), name='api-transaction-detail'),

    path('api/users/', UserListAPIView.as_view(), name='user-list'),
    path('api/users/<int:user_id>/transactions/', UserTransactionListAPIView.as_view(), name='user-transactions'),
    path('api/reports/', ReportView.as_view(), name='report'),
]
