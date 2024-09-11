update category

# Automated Testing

The aspects that aren't covered by automated tests are covered by [manual tests](./MANUALTESTS.md).

## Tested features

### Test models (test_models.py)

- Post model
1. featured flag is set to false by default
2. featured image is set to string ‘deafult’ by default
3. category is set to ‘others’ by default
4. status is set to 0 (draft) by default 
5. posts will be ordered from newest to oldest created date (created_on)
6. post will have a slug starting with the title
7. the string method will return the title
8. ‘num_of_likes’ will equal likes count
9. post with status 0 returns the status value of ‘Saved as draft’
11. post with status 1 returns the status value value of ‘Published’
12. pub_date will return string ‘Not published’ if not published. 
13. pub”_date returns date in the format %B %d, %Y" if published.
14. excerpt returns the first 200 characters of the post content
15. get_absolute_url method will return ‘/detail/‘ + slug + ‘/‘

Comment model
1. comment status is set to 0 by default
2. comments are ordered by oldest to newest created date
3. The string method of the comment will return “comment body by user”

<img src="./media/automated-tests/test_models.png" width="600" alt="results of testing test_models">

### Test forms (test_forms.py)

Post form
1. The title is required.
2. The content is required.
3. The featured image is not required.
4. The category is required.
5. The city is required.
7. The form fields are explicit.

Comment Form
1. The comment body is required.
2. The comment fields are required.

<img src="./media/automated-tests/test_forms.png" width="600" alt="results of testing test_forms">

### Test views (test_views.py)

- PostListView
1.  The home page will be rendered.
2. Three featured stories will be rendered.

- AddPost view 
1. If not signed in, users attempting to get to ‘Write Stories’ will be redirected to sign in page.
2. Logged in users can get to ‘Write Stories’. 
3. A post can be created.
4. The post will have status ‘Published’ if ‘Published’ button is clicked.
5. If ‘Save’ button is clicked, the post will have the status 0 (’draft’)
6. Saving a draft will render a message, ‘Your draft has been saved.'
7. Publishing a draft will render a message, “Your post has been published.”

- PostDetailView 
1. PostDetail view will render the detail page
2.  When the get method is called, ‘liked’ will be set to false if the user isn’t logged in or hasn’t liked the post
3.  When the get method is called, ’liked’ will be set to true if the user has liked the post
4. When the post method is called, ‘liked’ will be set to false if the user isn’t logged in or hasn’t liked the post
5.  When the post method is called, ’liked’ will be set to true if the user has liked the post
6.   When the get method is called, ‘bookmarked’ will be set to false if the user isn’t logged in or hasn’t bookmarked the post
7.  When the get method is called, ‘bookmarked’ will be set to true if the user has bookmarked the post
8. When the post method is called, ‘bookmarked’ will be set to false if the user isn’t logged in or hasn’t bookmarked the post
9.  When the post method is called, ‘bookmarked’ will be set to true if the user has bookmarked the post
10. comment can be created.
11.  When a comment is posted, a message “You posted a comment.” will be displayed.
12. The validation will throw an error message if only a space is entered for the comment.      ———————————fix this!
13. If the user is the author of the post, update and delete buttons are displayed.
14. If the user is not the owner of the post, update and delte buttons won’t be displayed.

- PostLike view
1.  Logged in user can ‘like’ a post
2. Sending a post request to post like view for the second time will ‘unlike’ the post. 

- Bookmark view
1. Logged in user can bookmark a post
2. Sending a post request to bookmark view for the second time will undo the bookmarking.

- UpdateComment view
1. The writer of the comment can get to ‘Update Comment’ page.
2. Trying to get to ‘Update Comment’ while not logged in will redirect to the log in page.
3. Trying to get to ‘Update Comment’ of another user’s comment will redirect to 403 page 
4. Logged in users can update their own comments.

- DeleteComment view
1. Deleting comments will set comments status to 2 (‘deleted’)

- UpdatePost view
1. The author of the post can get ‘Update Post’ page of their posts if logged in.
2. If not logged in, trying to get ‘Update Post’ page will redirect to the login page
3. Trying to get ‘Update Post’ page of another user’s post will redirect to 403 page. 
4. The title of the post can be updated.
5. The content of the post can be updated.
6. The city can be updated.
7. Canceling update will not update the post.
8. The feedback message will say the change has been saved if the post is updated.
9. The feedback message will say the post has been published if the post is published.
10. Publishing the post on ‘Update Post’ page will set the post status to 1 (‘Published’)

- DeletePost view
1. Posts can be deleted if the user is the writer of the posts.
2. Trying to delete others’ posts will redirect to 403 page
3. Trying to delete others’ posts will not delete the posts.
4. Trying to delete published posts will redirect to 403 page.

- RecentStories view
1. Recent stories page can be displayed.

- PopularStoriesView
1. Popular stories page can be displayed.

- MyPageView
1. Logged in users can get their own ‘My Page’
2.  Trying to get another user’s ‘My Page’ will redirect to 403 page.

<img src="../media/automated-tests/test_views.png" width="600" alt="results of testing test_models">