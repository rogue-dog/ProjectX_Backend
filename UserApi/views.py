from django.db import models
from django.db.models import query
from django.http import response
from django.shortcuts import render
import rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, serializers
from UserApi.models import Faculty, User, UserVerification, Wallet
from UserApi.send_otp import send_otp
from UserApi.dummy_data import dummy_data,dummy_reviews
 

from UserApi.encode import decode, encode
from UserApi.serializers import FacultySerializers

# Create your views here.


@api_view(['GET'])
def login(request):
    email = request.headers['email']
    password = request.headers['password']
    
    body = {"": ""}
    if(User.objects.filter(email=email,password=password).exists()):
        
        

        message = "Logged In Successfully..."
        success = True
        user = User.objects.get(email=email)
        body = {
                "email": getattr(user, "email"),
                "name": getattr(user, "name"),
                "user_id": str(getattr(user, "user_id")),
                "phone": getattr(user, "phone")
            }
    else:
        message = "Incorrect Credentials"
        success = False

    return(Response({"message": message, "success": success, "body": body}))


@api_view(['POST'])
def SignUp(request):
    name = request.data['name']
    email = request.data['email']
    password = request.data['password']
    new_user = User(email=email, password=password, name=name)
    new_user.save(force_update=True)
    id = str(getattr(new_user, "user_id"))
    return (Response({"success": True, "message": "Account Created!", "user_id": id}))


@api_view(['GET'])
def EmailVerification(req):
    email = req.headers['email']
    success, message = send_otp(email)
    return(Response({"success": success, "message": message}))


@api_view(['GET'])
def OTPCheck(req):
    email = req.headers['email']
    otp = req.headers['otp']
    if(UserVerification.objects.filter(email=email, otp=otp).exists()):
        UserVerification.objects.filter(email=email).delete()
        return(Response({"success": True, "message": "Email Verified"}))
    else:
        return(Response({"success": False, "message": "Incorrect OTP"}))



class FacultyView(generics.ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializers

    def get(self, request, *args, **kwargs):
        user_id=request.headers['user_id']
        if(User.objects.filter(user_id=user_id).exists()):
        
            return(Response(dummy_data))
        else :
            return(Response({"message" : "User Inauthorized"}))


    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


     
@api_view(['GET'])
def get_reviews(request) :
    return(Response(dummy_reviews))

@api_view(['GET'])
def get_wallet(request) :
    user_id= request.headers['user-id']
    if(User.objects.filter(user_id=user_id).exists()):
        wallet,_ = Wallet.objects.get_or_create(user_id=user_id)
        wallet_data = {
            'wallet' :{
                "user_id" : getattr(wallet,"user_id"),
                "wallet_id" : getattr(wallet,"wallet_id"),
                "amount" :getattr(wallet,"amount"),
                "transactions" : getattr(wallet,"transactions")
            }
        }

        return(Response(wallet_data))
    return(Response({"message" : "Invalid Data"}))



@api_view(['GET'])
def add_to_wallet(request) :
    user_id= request.headers['user-id']
    added_amount = request.headers['added-amount']
    if(Wallet.objects.filter(user_id=user_id).exists()):
        wallet=Wallet.objects.filter(user_id=user_id)[0]
        org_amount = wallet.amount
        Wallet.objects.filter(user_id=user_id).update(amount=org_amount+int(added_amount))
        wallet=Wallet.objects.filter(user_id=user_id)[0]
        wallet_data = {
            'wallet' :{
                "user_id" : getattr(wallet,"user_id"),
                "wallet_id" : getattr(wallet,"wallet_id"),
                "amount" :getattr(wallet,"amount"),
                "transactions" : getattr(wallet,"transactions")
            }
        }
        return(Response(wallet_data))
    return(Response({"message" : "No Such User Exist"}))