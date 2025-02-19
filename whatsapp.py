import requests
import json

def SendMessageWhastapp(textUser, number):
    try:
        token = "EAATpsZC4pzuEBOwcaqoxWkk9yJD5I6K7jWC448zhGZBfvQQ17x5eqJDSLZBurOgEd9t3huswQG3lTd0nDfbHvCDcNVuxDQ9oYFMCyxjHHfzKuT0RaDSPMD0cICoaTVvVs3KfZAkbhmthUYC5iM4NliRawkxC0OompMvHD0TZCrSFqt0ZCeSUJqi3vRJkZCnqYZBsGUCkZB0ZCjNILppk4H76UtHSq0i7MzN5k2z0iUor9L0gZDZD"  
        api_url = "https://graph.facebook.com/v21.0/544334725432761/messages"
        data = {
                "messaging_product": "whatsapp",    
                "to": number,
                "text": {
                    "body": textUser
                },
                "type": "text"
                }
        headers= {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers)


        if response.status_code == 200:
            return True
        
        return False
    except Exception as exception:
        print(exception)
        return False    

