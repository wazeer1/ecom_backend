from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import Group, User
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from main.encryptions import *
from rest_framework import status
from .serializers import *
from api.v1.main.functions import *
from accounts.models import *
from main.models import *
import json


@api_view(["POST"])
@permission_classes((AllowAny,))
def create_account(request):
    serialized = SignUpserializer(data = request.data)
    if serialized.is_valid():
        name = request.data["name"]
        username = request.data["username"]
        phone = request.data["phone"]
        password = request.data["password"]
        country = request.data["country"]
        email = request.data["email"]
        if not UserProfile.objects.filter(phone=phone,is_verified=True).exists():
            if not UserProfile.objects.filter(username=username).exists():
                if Country.objects.filter(web_code = country, is_active = True).exists():
                    country = Country.objects.get(web_code = country, is_active = True)
                    if not OtpRecord.objects.filter(phone=phone,email=email,is_applied=True).exists():
                        print(password,"password",encrypt(password))
                        user = User.objects.create_user(
                            username = username,
                            password = password
                        )
                        otp = randomnumber(4)
                        otp_record = OtpRecord.objects.create(
                            phone = phone,
                            country = country,
                            email = email,
                            otp = otp
                        )
                        profile = UserProfile.objects.create(
                            name = name,
                            phone = phone,
                            country = country,
                            email = email,
                            password = encrypt(password),
                            username=username,
                            user = user,
                            auto_id = get_auto_id(UserProfile)
                        )
                        response_data = {
                            "StatusCode":6000,
                            "data":{
                                "title":"succes",
                                "message":"succes"
                            }
                        }
                    else:
                        response_data={
                            "StatusCode":6001,
                            "data":{
                            "title":"failed",
                            "message":"number or email already used"
                            }
                        }
                else:
                    response_data={
                        "StatusCode":6001,
                        "data":{
                        "title":"failed",
                        "message":"not available in your country"
                        }
                    }
            else:
                response_data={
                    "StatusCode":6001,
                    "data":{
                        "title":"failed",
                        "message":"username already exists"
                    }
                }
        else:
            response_data = {
                "StatusCode":6001,
                "data":{
                "title":"failed",
                "message":"number already registered"
                }
            }
    else:
        response_data = {
            "StatusCode": 6001,
            "data" : {
                "title": "Validation Error",
                "message": generate_serializer_errors(serialized._errors)
            },
        }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes((AllowAny,))
def verify_otp(request):
    serialized = Verifyserializer(data=request.data)
    if serialized.is_valid():
        phone = request.data["phone"]
        country = request.data["country"]
        email = request.data["email"]
        otp = request.data["otp"]
        if OtpRecord.objects.filter(phone = phone, email = email,is_applied=False).exists():
            otp_record = OtpRecord.objects.get(phone = phone, email = email,is_applied=False)
            if UserProfile.objects.filter(phone = phone,is_verified=False).exists():
                profile = UserProfile.objects.get(phone = phone,is_verified=False)
                if otp_record.otp == int(otp):
                    otp_record.is_applied=True
                    profile.is_verified=True
                    otp_record.save()
                    profile.save()
                    decrypt_pass = decrypt(profile.password)
                    headers = {
                        "Content-Type" : "application/json"
                    }

                    data = {
                        "username" : profile.username,
                        "password" : decrypt_pass,
                    }

                    protocol = "http://"
                    if request.is_secure():
                        protocol = "https://"

                    host = request.get_host()

                    url = protocol + host + "/api/v1/accounts/token/"
                    print(url)
                    response = requests.post(url, headers=headers, data=json.dumps(data))

                    if response.status_code == 200:
                        login_data = response.json()
                        response_data = {
                            "StatusCode":6000,
                            "data":{
                                "title":"succes",
                                "message":"otp verified succesfully",
                                "access":login_data
                            }
                        }
                    else:
                        response_data={
                            "StatusCode":6001,
                            "data":{
                            "title":"failed",
                            "message":"something went wrong"
                            }
                        }
                else:
                    response_data={
                        "StatusCode":6001,
                        "data":{
                        "title":"failed",
                        "message":"incorrect otp"
                        }
                    }
            else:
                response_data = {
                    "StatusCode":6001,
                    "data":{
                        "title":"failed",
                        "message":"no datas found"
                    }
                }
        else:
            response_data={
                "StatusCode":6001,
                "data":{
                "title":"failed",
                "message":"no otp record with phone or emal"
                }
            }
    else:
        response_data = {
            "StatusCode": 6001,
            "data" : {
                "title": "Validation Error",
                "message": generate_serializer_errors(serialized._errors)
            },
        }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    serialized = Loginserializer(data = request.data)
    if serialized.is_valid():
        username = request.data["username"]
        password = request.data["password"]
        if UserProfile.objects.filter(username = username,is_verified = True).exists():
            profile = UserProfile.objects.get(username = username,is_verified = True)
            if password == decrypt(profile.password):
                headers = {
                        "Content-Type" : "application/json"
                    }

                data = {
                    "username" : profile.username,
                    "password" : password,
                }

                protocol = "http://"
                if request.is_secure():
                    protocol = "https://"

                host = request.get_host()

                url = protocol + host + "/api/v1/accounts/token/"
                print(url)
                response = requests.post(url, headers=headers, data=json.dumps(data))

                if response.status_code == 200:
                    login_data = response.json()
                    response_data = {
                        "StatusCode":6000,
                        "data":login_data
                    }
                else:
                    response_data = {
                        "StatusCode":6001,
                        "data":{
                        "title":"failed",
                        "message":"something went wrong"
                        }
                    }
            else:
                response_data={
                    "StatusCode":6001,
                    "data":{
                    "title":"failed",
                    "message":"incorrect password"
                    }
                }
        else:
            response_data={
                    "StatusCode":6001,
                    "data":{
                    "title":"failed",
                    "message":"no verified accounts found in this username"
                    }
                }
    else:
        response_data = {
            "StatusCode": 6001,
            "data" : {
                "title": "Validation Error",
                "message": generate_serializer_errors(serialized._errors)
            },
        }
    return Response(response_data, status=status.HTTP_200_OK)