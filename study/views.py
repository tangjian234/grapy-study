
import dateutil.parser
from study.graph_helper import get_user, get_calendar_events,get_profile_items,get_calendar_events_detail,get_onedrive_files_detail
from django.urls import reverse
#from study.auth_helper import get_sign_in_url, get_token_from_code
from study.auth_helper import get_sign_in_url, get_token_from_code, store_token, store_user, remove_user_and_token, get_token

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


def initialize_context(request):
    context = {}
    # Check for any errors in the session
    error = request.session.pop('flash_error', None)

    if error != None:
        context['errors'] = []
        context['errors'].append(error)

    # Check for user in the session
    context['user'] = request.session.get('user', {'is_authenticated': False})
    return context

# old home 
def home1(request):
  # Temporary!
  return HttpResponse("Welcome to the study.")


def home(request):
  context = initialize_context(request)
  #return render(request, 'study/templates/study/home.html', context)
  return render(request, 'study/home.html', context)


def sign_in(request):
      # Get the sign-in URL
  sign_in_url, state = get_sign_in_url()
  # Save the expected state so we can validate in the callback
  request.session['auth_state'] = state
  # Redirect to the Azure sign-in page
  return HttpResponseRedirect(sign_in_url)

# old call back before change in 
#https://docs.microsoft.com/en-in/graph/studys/python?study-step=3
def callback_old(request):
  # Get the state saved in session
  expected_state = request.session.pop('auth_state', '')
  # Make the token request
  token = get_token_from_code(request.get_full_path(), expected_state)
  # Temporary! Save the response in an error so it's displayed
  request.session['flash_error'] = { 'message': 'Token retrieved', 'debug': format(token) }
  return HttpResponseRedirect(reverse('home'))


def callback_old(request):
      # Get the state saved in session
  expected_state = request.session.pop('auth_state', '')
  # Make the token request
  token = get_token_from_code(request.get_full_path(), expected_state)

def callback(request):
      # Get the state saved in session
  expected_state = request.session.pop('auth_state', '')
  # Make the token request
  token = get_token_from_code(request.get_full_path(), expected_state)

  # Get the user's profile
  user = get_user(token)

  # Save token and user
  store_token(request, token)
  store_user(request, user)

  return HttpResponseRedirect(reverse('home'))

"""
  # Get the user's profile
  user = get_user(token)
  # Temporary! Save the response in an error so it's displayed
  request.session['flash_error'] = { 'message': 'Token retrieved',
    'debug': 'User: {0}\nToken: {1}'.format(user, token) }
  return HttpResponseRedirect(reverse('home'))  
"""


def sign_out(request):
      # Clear out the user and token
  remove_user_and_token(request)

  return HttpResponseRedirect(reverse('home'))

def calendar_old(request):
      context = initialize_context(request)

      token = get_token(request)

      events = get_calendar_events(token)

      context['errors'] = [
        { 'message': 'Events', 'debug': format(events)}
      ]

      return render(request, 'study/home.html', context)  

def calendar(request):
  context = initialize_context(request)

  token = get_token(request)

  events = get_calendar_events_detail(token)

  if events:
    # Convert the ISO 8601 date times to a datetime object
    # This allows the Django template to format the value nicely
    for event in events['value']:
      event['start']['dateTime'] = dateutil.parser.parse(event['start']['dateTime'])
      event['end']['dateTime'] = dateutil.parser.parse(event['end']['dateTime'])
      attendees_name=""
      # Get each attendee's name, 
      for attendee  in event['attendees']:
       attendees_name=attendees_name+attendee['emailAddress']['name']+","
      event['at']=attendees_name

    context['events'] = events['value']
    print("yes",events)
    
  return render(request, 'study/calendar.html', context)

def onedrive(request):
  context = initialize_context(request)

  token = get_token(request)

  files = get_onedrive_files_detail(token)
  if files:
    context['files'] = files['value']
    print("yes",files)

  return render(request, 'study/onedrive.html', context)

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm
from .forms import ContactForm
from django.core.mail import send_mail
def get_name(request):    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'study/name.html', {'form': form})

def get_mail(request):    
    # if this is a POST request we need to process the form data
    print("P21",request.method )
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        print("ds")
        # check whether it's valid:
        if form.is_valid():
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                sender = form.cleaned_data['sender']
                cc_myself = form.cleaned_data['cc_myself']

                recipients = ['info@example.com']
                if cc_myself:
                    recipients.append(sender)

                #res=send_mail(subject, message, sender, recipients,auth_user="tangjian234@gmail.com",auth_password="tangwin/")
          
                return HttpResponseRedirect('/thanks/')
        else:
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        print("sdd")
        form = ContactForm()

    return render(request, 'study/get_mail.html', {'form': form})

def profile(request):
      context = initialize_context(request)
      token = get_token(request)
      item = get_profile_items(token)
      if item:
            context['item'] = item
      return render(request, 'study/profile.html', context)


