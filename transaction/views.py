
from django.shortcuts import render, get_object_or_404, redirect
from .models import Transaction
from .forms import TransactionForm

from rest_framework import generics, permissions
from .serializers import TransactionSerializer

from .serializers import UserSerializer
from django.contrib.auth.models import User

from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView




# Create your views here.




def list_transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction/list_transactions.html', {'transactions': transactions})

def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')  # redirect to transaction list or detail page
    else:
        form = TransactionForm()
    return render(request, 'transaction/create_transaction.html', {'form': form, 'form_title': 'Create Transaction'})

def update_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transaction/create_transaction.html', {'form': form, 'form_title': 'Update Transaction'})


def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'transaction/confirm_delete.html', {'transaction': transaction})



class TransactionListAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer



class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserTransactionListAPIView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Transaction.objects.filter(user_id=user_id)
    


class ReportView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        year = request.query_params.get('year')
        month = request.query_params.get('month')

        
        transactions = Transaction.objects.filter(
            user_id=user_id,
            transaction_date__year=year,
            transaction_date__month=month
        )


        total_spent = transactions.aggregate(Sum('amount'))['amount__sum'] or 0
        total_transactions = transactions.count()

        
        report = {
            "user_id": user_id,
            "year": year,
            "month": month,
            "total_transactions": total_transactions,
            "total_spent": total_spent,
            "transactions": []
        }

        
        for transaction in transactions:
            report["transactions"].append({
                "date": transaction.transaction_date,
                "description": transaction.description,
                "amount": transaction.amount
            })

        return Response(report)

        