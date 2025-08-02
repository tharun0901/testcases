from fastapi.testclient import TestClient
from main import app
import pytest
import os
import uuid

tc=TestClient(app)
user_id=str(uuid.uuid4())[:12]
def test_upload_user_photo():
    with open("test_images/pic1.jpg","rb") as f:
        res=tc.post(f"/upload_user_foto/?user_id={user_id}",files={"file":("pic1.jpg",f,"image/jpeg")})
        assert res.status_code==200
        
def test_get_user_picture():
    res=tc.get(f"/user-pic/{user_id}")
    assert res.status_code==200
def test_create_user():
    tc.delete(f"/delete_user/{user_id}")
    res=tc.post(f"/create_user/?_id={user_id}",json={
    "nome": "zxtharu00ncg",
    "role": 1,
    "foto":"pic1.jpg" ,
    "telefone":4661225,
    "email":"thar1@gmail.com" ,
    "password":"password",
    "deleted":None 
    })
    print(res.json())
    print(res.status_code)
    assert res.status_code==201
    
def test_get_user():
    res=tc.get("/users/")
    assert res.status_code==200
@pytest.mark.parametrize("user_id,new_user_id",[(user_id,user_id)])
def test_get_user_by_id(user_id,new_user_id):
    #user_id="thar13"
    res=tc.get(f"/users/{user_id}")
    print( res.json())
    print(res.status_code)
    assert res.json()["id"]==new_user_id
def test_update_user():
    res=tc.post(f"/update_user/{user_id}",json={
        "nome":"z13tvhga_1",
        "role":1,
        "foto":"pic2.jpg",
        "telefone":173764,
        "email":"new@gmail.com",
        "password":"newpass",
        "deleted":None
    })
    print(res.json())
    assert res.status_code==200
def test_delete_user():
    res=tc.delete(f"/delete_user/{user_id}")
    assert res.status_code==204

