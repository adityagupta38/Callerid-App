After login user can redirected to homepage where he can peform all the required tasks. 

1. There are two models User is for registered user info & GlobalUsers is for both registered and non registered.

2. i have crated a seprate view to populate GlobalUser model with data for testing purpose you can use it by going to localhost/globalusers like this http://127.0.0.1:8000/globalusers 

3. Both the Models have Spam field set to Default value No and registered user can add or update the spam value from UI and it will get reflected on both the  models.

4. only get and post requests are allowed for Api.

5. BASE_URL for api will be the localhost or ip address of the local machine for developments server.

6.ENDPOINT is 'guserapi/' for fetching the details from api you need to send valid credentials as request body.

7. phoneno is the key for api and Mobile No will be the value.

8.  don't forget to append / at the end of api Url bcz append slash in django is still set as it will give an error.

9. views for api's are in seprate module named apiviews.

10. please make sure to run python manage.py makemigrations and migrate commands respectively before try to run the server.

