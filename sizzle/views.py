from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def index(request):
    return render(request, 'land.html')

def auth(request):
    return render(request, 'auth.html')

def catalog(request):
    note = {'menu' : [
        {'name': 'Pizza', 'description': 'Some hot and tasty pizza slices.', 'price': '150', 'image': 'https://firebasestorage.googleapis.com/v0/b/sizzle-app-d4cf0.appspot.com/o/pizza.jpeg?alt=media&token=54cd36d1-6138-433f-a3b5-57e8d60950c9'},
        {'name': 'Pizza', 'description': 'Some hot and tasty pizza slices.', 'price': '150', 'image': 'https://firebasestorage.googleapis.com/v0/b/sizzle-app-d4cf0.appspot.com/o/pizza.jpeg?alt=media&token=54cd36d1-6138-433f-a3b5-57e8d60950c9'},
        {'name': 'Pizza', 'description': 'Some hot and tasty pizza slices.', 'price': '150', 'image': 'https://firebasestorage.googleapis.com/v0/b/sizzle-app-d4cf0.appspot.com/o/pizza.jpeg?alt=media&token=54cd36d1-6138-433f-a3b5-57e8d60950c9'},
        {'name': 'Pizza', 'description': 'Some hot and tasty pizza slices.', 'price': '150', 'image': 'https://firebasestorage.googleapis.com/v0/b/sizzle-app-d4cf0.appspot.com/o/pizza.jpeg?alt=media&token=54cd36d1-6138-433f-a3b5-57e8d60950c9'},
        {'name': 'Pizza', 'description': 'Some hot and tasty pizza slices.', 'price': '150', 'image': 'https://firebasestorage.googleapis.com/v0/b/sizzle-app-d4cf0.appspot.com/o/pizza.jpeg?alt=media&token=54cd36d1-6138-433f-a3b5-57e8d60950c9'},
        {'name': 'Pizza', 'description': 'Some hot and tasty pizza slices.', 'price': '150', 'image': 'https://firebasestorage.googleapis.com/v0/b/sizzle-app-d4cf0.appspot.com/o/pizza.jpeg?alt=media&token=54cd36d1-6138-433f-a3b5-57e8d60950c9'}
    ]}
    return render(request, 'catalog.html', note)

def cart(request):
    doc_ref = db.collection('users').document(request.GET.get('userkey'))
    doc = doc_ref.get()
    # if doc.exists:
    #     note = {doc.to_dict()}
    #     return render(request, 'cart.html', note)
    # else:
    #     return render(request, 'error.html')
    return render(request, 'cart.html')
    
def checkout(request): 
    return render(request, 'checkout.html')

def orders(request):
    return render(request, 'orders.html')

def added(request):
    return render(request, 'added.html')

def success(request):
    return render(request, 'success.html')

def error(request):
    return render(request, 'error.html')

def addUser(request):
    if request.method == 'GET':
        userkey = request.GET.get('userkey')
        name = request.GET.get('name')
        email = request.GET.get('email')
        doc_ref = db.collection('users').document(userkey)
        doc_ref.set({
            'name': name,
            'email': email,
            'userkey': userkey,
            'cart': [],
            'orders': []
        })

def addToCart(request):
    if request.method == 'GET':
        doc_ref = db.collection('users').document(request.GET.get('userkey'))
        doc_ref.update({
            'cart': [{'image': request.GET.get('image'), 'name': request.GET.get('name'), 'description': request.GET.get('description'), 'price': request.GET.get('price')}]
        })
        return render(request, 'added.html')

def addToOrders(request): 
    if request.method == 'GET':
        doc_ref = db.collection('users').document(request.GET.get('userkey'))
        doc_ref.update({
            'orders': [{'name': request.GET.get('name'), 'price': request.GET.get('price')}]
        })
        return render(request, 'success.html')

def orderNow(request):
    if request.method == 'GET':
        doc_ref = db.collection('orders').document(request.GET.get('key'))
        doc_ref.set({
            'name': request.GET.get('name'),
            'email': request.GET.get('email'),
            'address': request.GET.get('address'),
            'userkey': request.GET.get('userkey'),
            'price': request.GET.get('price')
        })
        return render(request, 'success.html')