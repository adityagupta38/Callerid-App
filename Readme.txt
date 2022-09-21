Project Details

After login user can redirected to homepage where he can peform all the required tasks. 

1. There are two models User is for registered user info & GlobalUsers is for both registered and non registered.

2. i have crated a seprate view to populate GlobalUser model with data for testing purpose you can use it by going to localhost/globalusers like this http://127.0.0.1:8000/globalusers 

3. Both the Models have Spam field set to Default value No and registered user can add or update the spam value from UI and it will get reflected on both the  models.

How Api Can Be Used

1. only get and post requests are allowed for Api.

2. BASE_URL for api will be the localhost or ip address of the local machine for developments server.

3.ENDPOINT is 'guserapi/' for fetching the details from api you need to send valid credentials as request body.

4. for getting detail of phoneno just use phoneno  as key & the Mob no as Value of phoneno for fetching the detail of that particular phoneno using GET request.

5. For adding a no to Spam you need to first verify credentials of registered user as user(as key) and registered mobile no as value and password(as key) and registered user password as value and then rest of the data using specified key and Values.

6.  don't forget to append / at the end of api Url bcz append slash in django is still set as it will give an error.

7. views for api's are in seprate module named apiviews.



Note: please make sure to run python manage.py makemigrations and migrate commands respectively before try to run the server.

