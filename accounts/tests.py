import json
from unittest.case import _AssertRaisesContext
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import User ,UserManager
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from .serializers import LoginSerializer,RegisterSerializer ,LogoutSerializer
import requests
# import pyjwt

def getToken():
  url="http://localhost:8000/api/token/"
  response=requests.post(url,json={"email":"adham@gmail.com","password":"adham123"})
  tokens=response.json()
  return tokens.get("access")
factory = APIRequestFactory()

class TestSerilizer1(TestCase):
     def setUp(self):
        self.bike_attributes = {
        'email':"adham@gmail.com", 'username':"adham", 'password':"adham123",
        "is_company":True,"phone_number":"123456789",
        "profile_img":"adsda",
        "card_id_img":"adsd",
        "commercial_record_img":"dasasd","country":"sadsd",
        }

        self.serializer_data = {
         'email':"adham@gmail.com", 'username':"adham", 'password':"adham123",
        "is_company":True,"phone_number":"123456789",
        "profile_img":"adsda",
        "card_id_img":"adsd",
        "commercial_record_img":"dasasd","country":"sadsd",
        }

        self.bike = User.objects.create(**self.bike_attributes)
        self.serializer = RegisterSerializer(instance=self.bike)

     def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set( ["id",'email', 'username',"is_company","phone_number","profile_img","card_id_img",
        "commercial_record_img","country",]))

        RegisterSerializer.validate(self,self.serializer_data)
        RegisterSerializer.create(self,{'username':"sda",'email':"dasd"})
        LoginSerializer.get_tokens(self,self.bike_attributes)
     def test_contains_expected_fields2(self):
          data = self.serializer.data
          self.assertEqual(set(data.keys()), set( ["id",'email', 'username',"is_company","phone_number","profile_img","card_id_img",
        "commercial_record_img","country",]))

         
  
          self.assertRaises(LoginSerializer.validate(self,self.serializer_data))
          LogoutSerializer.validate(self,self.serializer_data)
          LogoutSerializer.save(self,self.serializer_data)
class BlogTest(TestCase):
  
    def setUp(self):
      self.user = User.objects.create_user(
    country = "jordan",
    username = "ash",
    email = "adham@gmail.com",
    first_name ="ash",
    last_name = "adham",
    is_verified = True,
    is_active = True,
    is_staff = True,

    date_joined = "12/12/1212",
    
    last_login = "12/12/1212",
    auth_provider = "facebook",
        )
    def setUp(self):
      self.user = User.objects.create_user(
    country = "jordan",
    username = "ash",
    email = "adham@gmail.com",
    first_name ="ash",
    last_name = "adham",
    is_verified = True,
    is_active = True,
    is_staff = True,

    date_joined = "12/12/1212",
    
    last_login = "12/12/1212",
    auth_provider = "facebook",
        )
      
    
    def test_string_representation(self):
        user = User(username='ash')
        self.assertEqual(str(user), user.username)


# #####################
    def test_all_fields(self):
        
        self.assertEqual(str(self.user), 'ash')
        self.assertEqual(f'{self.user.country}', 'jordan')
        self.assertEqual(self.user.last_name, 'adham')

#    ###########################

    def test_accounts_app(self):
        user={
    "email": "adham@gmail.com",
    "password":"adham123",
    "username": "14dsd34",
    "is_company": "True",
    "phone_number": "False",
    "country": "False"
  
        }
        access=getToken()
        resp=requests.get("http://localhost:8000/register/",headers={"Authorization":"Bearer " +access})
        resp6=requests.post("http://localhost:8000/register/",json={"email":"adham@gmail.com","password":"adham123"},headers={"Authorization":"Bearer " +access})
        resp2=requests.get("http://localhost:8000/register/1",headers={"Authorization":"Bearer " +access})        # response = self.client.get(reverse('register'))
        resp3=requests.post("http://localhost:8000/login/",json=user ,headers={"Authorization":"Bearer " +access})  
       
       
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp2.status_code, 200)
        self.assertEqual(resp3.status_code,200)
        self.assertEqual(resp6.status_code,400)

        resp_body=json.loads(resp.content)
        self.assertEqual(resp_body[0]["username"],"adham")
        
        resp6=requests.post("http://localhost:8000/register/" , json={})
        print(resp6.content)
        resp6_body=json.loads(resp6.content)
        self.assertEqual(resp6_body["email"][0], "This field is required.")
        self.assertEqual(resp6_body["username"][0], "This field is required.")
        self.assertEqual(resp6_body["password"][0], "This field is required.")
import json
from django.contrib.auth import get_user_model
from django.test import TestCase
from connect.models import Post ,Offer ,Comment
from django.urls import reverse
import requests
def getToken():
  url="http://localhost:8000/api/token/"
  response=requests.post(url,json={"email":"adham@gmail.com","password":"adham123"})
  tokens=response.json()
  return tokens.get("access")

class BlogTest(TestCase):
    def test_post_comment_offer(self):
        # self.client.login(json={"email":"adham@gmail.com", "password":"adham123"})
        # response = self.client.get(reverse('post'))
        access=getToken()
        response=requests.get("http://localhost:8000/api/v1/connect/post" ,headers={"Authorization":"Bearer " +access})
        self.assertEqual(response.status_code, 200)
        response12=requests.get("http://localhost:8000/api/v1/connect/post" ,)
        self.assertEqual(response12.status_code, 401)
        post_details=requests.get("http://localhost:8000/api/v1/connect/post/15/post_detail" , headers={"Authorization":"Bearer " +access})
        self.assertEqual(post_details.status_code, 200)
        response2=requests.put("http://localhost:8000/api/v1/connect/post/15/post_detail",json=post_details.json() ,headers={"Authorization":"Bearer " +access})

        self.assertEqual(response2.status_code,200)
        response3=requests.get("http://localhost:8000/api/v1/connect/offer/",json=post_details.json() ,headers={"Authorization":"Bearer " +access})
        self.assertEqual(response3.status_code,200)
        response4=requests.put("http://localhost:8000/api/v1/connect/offer/",json=post_details.json() ,headers={"Authorization":"Bearer " +access})
        self.assertEqual(response4.status_code,405)
        response5=requests.delete("http://localhost:8000/api/v1/connect/offer/",json=post_details.json() ,headers={"Authorization":"Bearer " +access})
        self.assertEqual(response5.status_code,405)
        response6=requests.get("http://localhost:8000/api/v1/connect/comment",json=post_details.json() ,headers={"Authorization":"Bearer " +access})
        self.assertEqual(response6.status_code,200)
        comment_details=requests.get("http://localhost:8000/api/v1/connect/comment/2/comment_detail",json=post_details.json() ,headers={"Authorization":"Bearer " +access})
        self.assertEqual(comment_details.status_code,200)
        activityes=requests.get("http://localhost:8000/api/v1/connect/activity",json=post_details.json() ,headers={"Authorization":"Bearer " +access})
        self.assertEqual(activityes.status_code,200)
        activityes__details=requests.get("http://127.0.0.1:8000/api/v1/connect/activity/1416/activity_detail/",json=post_details.json() ,headers={"Authorization":"Bearer " +access})
        self.assertEqual(activityes__details.status_code,200)
        body=json.loads(activityes__details.content)
        self.assertEqual(body["type_of_activity"],"Comment")
