#a sample view using viewsets
# the 'controllers' are the classes that would handle the business logic. See users.py file
from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from app.custompermissions import CustomPermission
from app.controllers.users import UsersController

class UserViewset(viewsets.ViewSet):
    """Users viewset"""
    lookup_field = 'username'
    permission_classes = [IsAuthenticated(), ]
    # parser_classes = [MultiPartParser] This would be set where a different parser class is needed
    
    def list(self, request):
        """return all users"""    
        list_users = UsersController()
        return list_users.list_users(request)

    def create(self, request):
        """create a user"""
        create_user = UsersController()
        return create_user.create_user(request)

    def destroy(self, request, username=None):
        """delete user"""
        delete_user = UsersController()
        return delete_user.delete_user(username)

    def update(self, request, username=None):
        """update user"""
        update_user = UsersController()
        return update_user.update_user(request, username)

    def retrieve(self, request, username=None):
        """retrieve a user"""
        retrieve_user = UsersController()
        return retrieve_user.retrieve_user(username)

    @action(methods=['POST'], detail=False, permission_classes=[CustomPermission(), ])
    def login(self, request):
        """login a user"""
        login_user = LoginController()
        return login_user.login(request)

    #example of overiding default get_permission function permission
    def get_permissions(self):
        if self.action in ('create', 'list'):
            return [CustomPermission(), ]
        return super(UserViewset, self).get_permissions()

#this code snippet below is an example of how the above would look with class based views
from rest_framework.views import APIView

class AllUsers(APIView):
    def get(self, request):
        """return all users"""    
        list_users = UsersController()
        return list_users.list_users(request)

    def post(self, request):
        """create a user"""
        create_user = UsersController()
        return create_user.create_user(request)        

class SpecificUser(APIView):
    def get(self, request, username=None):
        """retrieve a user"""
        retrieve_user = UsersController()
        return retrieve_user.retrieve_user(username)
        
    def put(self, request, username=None):
        """update user"""
        update_user = UsersController()
        return update_user.update_user(request, username)
        
    def delete(self, request, username=None):
        """delete user"""
        delete_user = UsersController()
        return delete_user.delete_user(username)

class Login(APIView):
    def post(self, request):
        """login a user"""
        login_user = LoginController()
        return login_user.login(request)

