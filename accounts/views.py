from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# Only allow logged in users to access the system
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm

from app2_user_home.models import UserDetail
from app2_user_home.models import Vendor
from app2_user_home.models import Customer


"""
The 'index' logic applies only when the browser initially loads the page. 
The user may be logged into admin, but not exist on the issue tracking system. 
So the user will be logged out, if already logged in, and forced to log in 
properly via the app, so that it can check whether the user exists on the 
Issue Tracking System.
"""

def index(request):
    if request.user.is_authenticated:
        
        """ Log the user out """
    
        auth.logout(request)
        
    return redirect(reverse('home'))
    
    
    
# @login_required will first check if the user is logged in. If not they will
# be re-directed to the login page

@login_required
def logout(request):
    
    """ Log the user out """
    auth.logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect(reverse('home'))
    
    
def login(request):
    
    """ If the user is already logged in, send them back to home page """
        
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    
    """ If user has sent login details, validate them """
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            
            
            if user:
                auth.login(user=user, request=request)
                
                # Check that the user has been set up for the Issue Tracking 
                # System. If not, log out System
    
                UserDetails = ""
                try:
                    UserDetails = UserDetail.objects.get(user_name=user.username)
                    messages.success(request, "You have successfully logged in!")
                    return redirect(reverse('userhome'))
                except:
                    login_form.add_error(None, "User not set up on the Issue Tracking System")
                    
                    """ Log the user out """
                    auth.logout(request)
                
            else:
                login_form.add_error(None, "Your user name or password is incorrect")
    
    else:
        
        """ Return a login page """
    
        # Set user login form = instance of UserLoginForm (see forms.py), 
        # notice the "()"" here, and display for user to log in
    
        login_form = UserLoginForm()
    
    return render(request, 'login.html', {"login_form": login_form})
    

# User registration view

def registration(request):
    
    """ If the user is already logged in, send them back to home page """
        
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    
    """ If user has sent login details, validate them """
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered!")
                return redirect(reverse('home'))
            else:
                messages.error(request, "Unable to register your account at this time")
                
    else:
        registration_form = UserRegistrationForm()
    
    """ Render the registration page """
    return render(request, 'registration.html', {
        'registration_form': registration_form})


def user_profile(request):
    
    """ User's Profile page """
    
    user = User.objects.get(email=request.user.email)
   
    """
    Retrieve the user details relating to the Issue Tracking System.
    """
    
    UserDetails = UserDetail.objects.get(user_name=request.user.username)
    
    # Get the Vendor or Customer Details depending on which the user is 
    # associated with
    
    CustomerDetails = ""
    VendorDetails = ""
    
    if UserDetails.user_type == 'C':
        
        try:
            CustomerDetails = Customer.objects.get(cust_code=UserDetails.vend_cust_code)
        except:
            messages.success(request, "Customer details not found!")
    
    else:
        try:
            VendorDetails = Vendor.objects.get(vend_code=UserDetails.vend_cust_code)
        except:
            messages.success(request, "Vendor details not found!")
    
    
    return render(request, 'profile.html', {'profile': user, 'userdetails': UserDetails, 'customerdetails': CustomerDetails, 'vendordetails': VendorDetails})

    

    
        
        
    
    
    

