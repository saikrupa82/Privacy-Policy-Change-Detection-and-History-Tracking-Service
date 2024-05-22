from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from authen.forms import SignUpForm
from datetime import datetime
from bs4 import BeautifulSoup
import json
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import *

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('homepage')  # Redirect to 'homepage_view' after successful signup
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})

# Adjust your logout_view to ensure a smooth flow
def logout_view(request):
    logout(request)
    return redirect('home')  

def home(request):
    if request.user.is_authenticated:
        return  render(request, 'auth/homepage.html')
    else:
        return  render(request, 'auth/home.html')


@login_required
def tracker(request):
    # Dictionary to map URLs to their respective classes
    dic = {"https://policies.google.com/privacy": "xXnO1d"}

    if request.method == 'POST':
        privacy_policy_url = request.POST.get('url-address')
        title = request.POST.get('title', 'Default Title')  # Provide a default title if none is given

        # Check if the provided URL is in the dictionary
        if privacy_policy_url not in dic:
            return HttpResponse("The URL is not recognized for tracking.", status=400)

        # Perform your saving logic here
        try:
            # Web scraping logic goes here
            class_name = dic[privacy_policy_url]
            response = requests.get(privacy_policy_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                elements = soup.find_all(class_=class_name)
                
                content_dict = {}
                if not elements:
                    return HttpResponse(f"No content found for class name '{class_name}' in the provided URL.", status=400)
                    
                for element in elements:
                    h1_text = element.find('h1').get_text(strip=True) if element.find('h1') else None
                    non_h1_texts = [tag.get_text(strip=True) for tag in element.find_all(True) if tag.name != 'h1']
                    if h1_text:  # Only add if h1 is present
                        content_dict[h1_text] = non_h1_texts
                
                # Save the PolicyTracker instance
                policy_tracker_instance = PolicyTracker(
                    user=request.user,
                    policy_name=title,
                    url=privacy_policy_url,
                    content_dict=content_dict
                )
                policy_tracker_instance.save()

                # Redirect to a success page
                return redirect('success_view_name')  # Redirect to a URL configured in urls.py
            else:
                return HttpResponse(f"Failed to retrieve the webpage with URL {privacy_policy_url}.", status=500)
        except Exception as e:
            # If an error occurs, return an error message
            return HttpResponse(f"An error occurred: {str(e)}", status=500)
    
    # If not a POST request, just render the page normally
    return render(request, 'auth/tracker.html')



@login_required
def homepage_view(request):
    try: 
        user_policies = PolicyTracker.objects.filter(user=request.user).order_by('-last_checked')
        tracked_pages_count = user_policies.count()
        
        context = {
            'user_policies': user_policies,
            'tracked_pages_count': tracked_pages_count
        }
        return render(request, 'auth/homepage.html', context)
    except:
        return render(request, 'auth/home.html')



@login_required
def trackingstatus_view(request, string):
    date_ranges = ["All time", "30 days", "15 days", "24 Hrs", "12 Hrs", "1 Hr"]

    # Replace 'string_field_name' with the actual field name that corresponds to 'string' in your model
    policy = get_object_or_404(PolicyTracker,user=request.user, policy_name=string)
    # Now you have the policy object filtered by both id and string
    context = {'policy': policy,
               'date_ranges': date_ranges}
    return render(request, 'auth/trackingstatus.html', context)