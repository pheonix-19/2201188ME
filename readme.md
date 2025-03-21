

###  Fetch Users
Send a *GET* request to:

http://127.0.0.1:5000/users

With the Authorization header:

Authorization: Bearer YOUR_ACCESS_TOKEN


###  Fetch Posts by a User
Send a *GET* request:

http://127.0.0.1:5000/users/{user_id}/posts


### Fetch Comments for a Post
Send a *GET* request:

http://127.0.0.1:5000/posts/{post_id}/comments
