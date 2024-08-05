import requests
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/hydjobsinfo/'
requests = requests.get(BASE_URL + END_POINT)
data = requests.json()
for job in data:
    print('Company name:',job['company'])
    print('Eligibility:', job['eligibility'])
    print('Title:', job['title'])
    print("Address:", job['address'])
    print('Mail ID:', job['email'])
    print('Phone Number:', job['phonenumber'])
    print()