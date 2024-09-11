# Manual Tests

The aspects that weren't covered by automated tests are conducted manually and are documented on this page.

### Testing User Stories
No. | Goals | How they are achieved | 
|:---| :--- | :--- |  
|1| What the site is for and how to use it are clear. | An introductory paragraph on the home page describes what the site is for and how to use it.  Also the links in the navigation bar indicate which page has which functionality so users can easily understand how to use the app. | 
|2|The app can be used on screen of different sizes|All pages of the app are responsively designed.| 
|3| Visitors can sign up. | Users can go to the sign up page via the link in the navbar, present on all pages.  Also, at the end of the introductory paragraph on the home page, another link to the sing up page is provided. | 
|4| Users can see the detail page of a post. | All post excerpts have a link ‘Read the full story,’ and by clicking the link, users can go to the detail page. The detail page displays the full content of the post and comments written on the post. |
|5| Featured posts are presented on the home page. | Three featured posts chosen by editors are displayed on the home page. |
|6| Users can see a list of recently published posts. |By clicking the link on the home page 'More Stories from this week' users can go to the page displaying a list of recently published posts. | 
|7| Users can see a list of popular posts. | By clicking the link on the home page 'Readers' favorite stories of all time' users can go to the page displaying a list of the posts that have been liked the most. |
|8| Users can write posts. | On ‘Write Stories’ page logged in users can write their own posts and submit them.  The posts will be published if admin of the site approves of them. |
|9| Users can edit posts. | By clicking 'update' on the post_detail page, users can edit their posts. |
|10| Users can delete posts. | By clicking 'delete' on the post_detail page, users can delete their posts.|
|11| Users can write comments. | Logged in users can leave comments on the post_detail page.|
|12| Users can edit comments | By clicking the edit icon, users can delete their comments. |
|13| Users can delete comments. | By clicking the trash bin icon, users can delete their comments. |
|14| Users can search posts. | On "Search Stories" page, users can search posts by multiple factors. |
|15| Users can like posts. |By clicking on the heart icon, logged in users can like posts.|
|16| Users have easy access to the posts written, commented or bookmaked by them. |'My page' displays these three groups of posts.|
|17| The most interesting posts are presented on "Home" |Three featured stories chosen by admin will be displayed on the home page. |
|18| Allow users to update or delete posts only before submission | ‘Update’ and ‘Delete’ buttons for posts appear only if posts are in ‘draft’ status.  In addition, the code is programmed to raise errors if attempts are made to update or delete submitted posts. (line 226 & 232 in views.py) |
|19| Allow only the authors to update/delete the posts & comments | LoginRequiredMixin and UserPassestestMixin allow only the users who are logged in as the authors of posts and comments to update or delete their writings. |
|20|Allow users to access only their own “My page” | LoginRequiredMixin and UserPassestestMixin will allow users to access only their own “My Page.” |
|21|Users get feedback messages|Feedback messages are displayed on the top of the page for 5 seconds after requests from the users have been processed. |
|22|Users will see delete confirmation dialogs. |Before deleting their posts or comments, users will see delete confirmation dialogs. |
|23| Users can bookmark posts. |By clicking the bookmark icon, logged-in users can bookmark posts.  The bookmarked posts will be displayed on 'My Page'. |

#### Testing Features
As preparatory steps,
1. create a user with username "testuser" and a password "gR48NmYr1" (leave the email blank)
2. Sign in as "testuser"
3. make 10 posts with the following field values:
title: blog 1, blog 2, blog 3, blog 4, blog 5, blog 6, blog 7, blog 8, blog 9, blog 10
content: (for all of them): test content
city: Dublin
country: Ireland
4. go to admin panel.
5. publish blog 1-10 one by one in the order.
6. set featured_flag True for blog 1-3.
7. go to "Detail Page" of blog 4-10 and click 'like' button

Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image|Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Logo link|Go to “Search Stories”|Click the logo|Redirected to the home page|Redirected to the home page|pass|[image](./media/manual-tests/navlinks/1.png)|2023/10/15|
|2|Link to ”Home”|Go to “Search Stories” page|Click the link “Home”|Redirected to ”Home"|Redirected to ”Home”|pass|[image](./media/manual-tests/navlinks/2.png)|2023/10/15|
|3|Link to ”Search Stories”|Go to “Home”|Click “Search Stories”|Redirected to ”Search Stories”|Redirected to ”Search Stories”|pass|[image](./media/manual-tests/navlinks/3.png)|2023/10/15|
|4|”Become a Member”|Go to “Home” page|Click “Become a Member”|Redirected to ”Become a Member” | Redirected to “Become a Member”|pass|[image](./media/manual-tests/navlinks/4.png)|2023/10/15|
|5|”Sign in”|Go to “Home” page|Click "Sign in”|Redirected to ”Sign in”|Redirected to “Sign in”|pass|[image](./media/manual-tests/navlinks/5.png)|2023/10/15|
|6|”Write Stories”|Log in and go to “Home”|Click “Write Stories”|Redirected to ”Write Stories”|Redirected to ” Write Stories”|pass|[image](./media/manual-tests/navlinks/6.png)|2023/10/15|
|7|”My Page”|Go to “Home” page|Click “My Page”|Redirected to ”My Page”|Redirected to “My Page”|pass|[image](./media/manual-tests/navlinks/7.png)|2023/10/15|
|8|”Sign out”|Go to “Home” page|Click “Sign out”|Redirected to ”Sign out”|Redirected to “Sign out”|pass|[image](./media/manual-tests/navlinks/8.png)|2023/10/15|

#### Burger Menu for screen sizes below 700px
*Conduct test no. 2 & 3 without any actions in between.*
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image|Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Hamburger menu| Set the window size to 690px | Check if the burger menu appears. | The burger menu appears. |The burger menu appears.| pass|[image](./media/manual-tests/burger/1.png)|2023/8/15|
|2|Hamburger menu| --| Click the hamburger menu | The menu box opens |The menu box opens| pass|[image](./media/manual-tests/burger/2.png)|2023/8/15|
|3|Hamburger menu| --| Click the link 'Search Stories' | The menu box closes. Redirected to "Search Stories." |The menu box closes. Redirected to "Search Stories." | pass|[image](./media/manual-tests/burger/3.png)|2023/8/15|
|4|Hamburger menu| --| Click the burger to open the menu. Click again on the burger.| The menu box closes. |The menu box closes. | pass|[image](./media/manual-tests/burger/4.png)|2023/8/15|
|5|Hamburger menu| --| Click the burger to open the menu. Click outside the menu.| The menu box closes. |The menu box closes. | pass|[image](./media/manual-tests/burger/5.png)|2023/8/15|

#### Links in the footer
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image|Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|link to facebook|--|Click the facebook icon|Redirected to the facebook site|Redirected to the facebook site| pass|[image](./media/manual-tests/footer/1.png)|2023/8/15|
|2|link to twitter|--|Click the twitter icon|Redirected to the twitter site|Redirected to the twitter site| pass|[image](./media/manual-tests/footer/2.png)|2023/8/15|
|3|link to instagram|--|Click the instagram icon|Redirected to the instagram site|Redirected to the instagram site| pass|[image](./media/manual-tests/footer/3.png)|2023/8/15|

#### The flash messages
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image|Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1| Message disappears after 5 seconds. | sign out | sign in as testuser | Redirected to the home page.  The message "Successfully signed in as testuser" will show up and disappear after 5 seconds. |Redirected to the home page.  The message "Successfully signed in as testuser" shows up and disappears after 5 seconds.| pass|[image](./media/manual-tests/flash_messages/1.png)|2023/8/15|

#### Home
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail |Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|link ”become a member” in the introduction |--|Click the link|Redirected to "Become a member."| Redirected to "Become a member."|pass|[image](./media/manual-tests/home/1.png)|2023/8/15|
|2|link ”Read the full story” at the bottom of "blog 3" |--|Click the link|Detail page of "blog 3" will be displayed.| Detail page of "blog 3" is displayed.|pass|[image](./media/manual-tests/home/2.png)|2023/8/15|
|3|link ”Read the full story” at the bottom of "blog 2" |--|Click the link|Detail page of "blog 2" will be displayed.| Detail page of "blog2" is displayed.|pass|[image](./media/manual-tests/home/3.png)|2023/8/15|
|4|link ”Read the full story” at the bottom of "blog1" |--|Click the link|Detail page of "blog 1" will be displayed.| Detail page of "blog 1" is displayed.|pass|[image](./media/manual-tests/home/4.png)|2023/8/15|
|5|link ”More stories from this week” |--|Click the link|Redirected to “More stories from this week”| Redirected to “More stories from this week”|pass|[image](./media/manual-tests/home/5.png)|2023/8/15|
|6|link ”Readers’ favorite stories of all time” |--|Click the link|Redirected to ”Readers’ favorite stories of all time” |Redirected to ”Readers’ favorite stories of all time”|pass|[image](./media/manual-tests/home/6.png)|2023/8/15|

#### Detail Page
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail |Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|link to "Become a Member"|Log out|Click the link on the right side of the comments section|Redirected to "Become a Member" page|Redirected to "Become a Member" page|pass|[image](./media/manual-tests/detail_page/1.png)|2023/8/15|
|2|link to "Sign in"|--|Click the link|Redirected to "Sign in" page|Redirected to "Sign in" page|pass|[image](./media/manual-tests/detail_page/2.png)|2023/8/15|
|3|validation message for comment form| Sign in as testuser and go to "Detail Page" page of "blog 1"| leave the comment field blank, and click 'Submit' | A message says "Please fill out this field"| A message says "Please fill out this field"| pass|[image](./media/manual-tests/detail_page/3.png)|2023/8/15|

#### Update/Delete Comments
As preparation,<br>
- Sign in as testuser and go to "Detail Page" of "blog 1."
- Enter "test comment" in the text box and click 'Submit.'
- Conduct test no. 1-2 consecutively.

Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Update comment button|--| Click the update icon next to the comment.|"Update Comment" page will be displayed.|"Update Comment" page is displayed.|pass|[image](./media/manual-tests/detail_page_comments/1.png)|2023/8/15|
|2|Delete comment button|--| Click the trash bin icon next to the comment.|Confirmation dialog "Are you sure you want to delete your comment?" will show up. |Confirmation dialog "Are you sure you want to delete your comment?" shows up. |pass|[image](./media/manual-tests/detail_page_comments/2.png)|2023/8/15|
|3|Confirmation dialog - cancel|--|Click 'Cancel'|The dialog diappears, and "Detail Page" is displayed.|The dialog diappears and "Detail Page" is displayed.|pass|[image](./media/manual-tests/detail_page_comments/3.png)|2023/8/15|
|4|Confirmation dialog - ok|Click the trash bin icon.|Click 'OK' in the dialog.|The dialog disappears. A label says 'Comment deleted' where the comment originally was.|The dialog disappears. A label says 'Comment deleted' where the comment originally was.|pass|[image](./media/manual-tests/detail_page_comments/4.png)|2023/8/15|

#### Confirmation Dialog before Deleting Posts
*Write a story and save. Conduct no. 1-3 without any actions in between.*
Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Confirmation dialog |--|Go to the "Detail Page" of the draft, and click "Delete"|Confirmation dialog appears and says "Are you sure you want to delete your post?  You won't be able to retrieve the draft.|Confirmation dialog appears and says "Are you sure you want to delete your post?  You won't be able to retrieve the draft.|pass|[image](./media/manual-tests/detail_page_delete_posts/1.png)|2023/8/15|
|2|Confirmation dialog - cancel|--|Click on 'Cancel'|The dialog diappears, and "Detail Page" remains unchanged.|The dialog diappears and the "Detail Page" remains unchanged.|pass|[image](./media/manual-tests/detail_page_delete_posts/2.png)|2023/8/15|
|3|Confirmation dialog - ok|--|Click on 'Ok'|Redirected to "home." A flash message, "Your draft has been deleted." appears.|Redirected to "home." A flash message, "Your draft has been deleted." appears.|pass|[image](./media/manual-tests/detail_page_delete_posts/3.png)|2023/8/15|

#### Recent Stories
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- | :--- |
|1|pagination|--|Go to "More Stories"| Blog 5-10 are displayed in descending order and blog 4 is displayed on the second page.|Blog 5-10 are displayed in descending order and blog 4 is displayed on the second page.|pass|[image1 ](./media/manual-tests/more_stories/1.png)[image2 ](./media/manual-tests/more_stories/1-2.png)[image3](./media/manual-tests/more_stories/1-3.png)|2023/8/16|
|2|link 'NEXT' if paginated|--|Click ‘NEXT’|The second page is displayed.|The second page is displayed.|pass|[image ](./media/manual-tests/more_stories/2.png)|2023/8/16|
|3|link 'PREV' on the second page|--|Click on PREV|The first page is displayed.|The first page is displayed.|pass|[image ](./media/manual-tests/more_stories/3.png)|2023/8/16|

#### Popular Stories
Test No.| Feature tested| Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|1|content of the page|--|Go to "Popular Stories"| Blog 5-10 are displayed in descending order and blog 4 is displayed on the second page.|Blog 5-10 are displayed in descending order and blog 4 is displayed on the second page.|pass|[image1 ](./media/manual-tests/more_stories/1.png)[image2 ](./media/manual-tests/more_stories/1-2.png)[image3](./media/manual-tests/more_stories/1-3.png)|2023/8/16|
|2|link 'NEXT' if paginated|--|Click on NEXT|The second page is displayed.|The second page is displayed.|pass|[image ](./media/manual-tests/more_stories/2.png)|2023/8/16|
|3|link 'PREV' on the second page|--|Click on PREV|The first page is displayed.|The first page is displayed.|pass|[image ](./media/manual-tests/more_stories/3.png)|2023/8/16|

#### Write Stories
*Log in as testuser*
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Leave all fields empty| -- | click 'save' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass |[image](./media/manual-tests/write_stories/1.png)|2023/8/16|
|2|Leave all fields empty| -- | click ‘publish’ | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass |[image](./media/manual-tests/write_stories/2.png)|2023/8/16|
|3|Leave title empty | Enter 'content' for content, 'test city' for city, select 'Afghanistan' for country | click 'save' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass |[image](./media/manual-tests/write_stories/3.png)|2023/8/16|
|4|Leave title empty | Enter 'content' for content, 'test city' for city, select 'Afghanistan' for country | click ‘publish’ | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass|[image](./media/manual-tests/write_stories/4.png)|2023/8/16|
|5|Leave content empty | Enter 'test title 1' for title, 'test city' for city, select 'Afghanistan' for country | click 'save' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the content | pass|[image](./media/manual-tests/write_stories/5.png)|2023/8/16|
|6|Leave content empty | Enter 'test title 1' for title, 'test city' for city, select 'Afghanistan' for country | click ‘publish’ | A message says "Please fill out this field" for the content | A message says "Please fill out this field" for the content | pass|[image](./media/manual-tests/write_stories/6.png)|2023/8/16|
|7|Leave city empty | Enter 'test title 1' for title, 'content' for content, select 'Afghanistan' for country | click 'save' | A message says "Please fill out this field" for the city | A message says "Please fill out this field" for the city | pass|[image](./media/manual-tests/write_stories/7.png)|2023/8/16|
|8|Leave city empty | Enter "test title 1" for title, 'content' for content, select 'Afghanistan' for country | click ‘publish’ | A message says "Please fill out this field" for the city | A message says "Please fill out this field" for the city | pass|[image](./media/manual-tests/write_stories/8.png)|2023/8/16|
|9|Select nothing for country | Enter "test title 1" for title, 'content' for content, 'test city' for city | click 'save' | A message says "Please select an item in the list" for the country" | A message says "Please fill out this list" for the country" | pass|[image](./media/manual-tests/write_stories/9.png)|2023/8/16|
|10|Select nothing for country | Enter 'test title 1' for title, 'content' for content, 'test city' for city | click ‘publish’ | A message says "Please select an item in the list" for the country | A message says "Please fill out this list" for the country | pass|[image](./media/manual-tests/write_stories/10.png)|2023/8/16|
|11|enter spaces | enter spaces in 'title,' 'content' and 'city'| click 'save' | A message says "Please fill out this field" for the title | A message says "Please select an item in the list" for the country | fail |[image](./media/manual-tests/write_stories/11.png)|2023/8/16|
|12|enter spaces | enter spaces in 'title,' 'content' and 'city'| click ‘publish | A message says "Please fill out this field" for the title | A message says "Please select an item in the list" for the country | fail |[image](./media/manual-tests/write_stories/12.png)|2023/8/16|
|13|enter spaces | enter spaces in 'title,' 'content,' 'city' and select 'Afghanistan' for country| click 'save' | A message says "Please fill out this field" for the title | A message says "This field is required." appears for title, content and city | fail |[image](./media/manual-tests/write_stories/13.png)|2023/8/16|
|14|enter spaces | enter spaces in 'title,' 'content,' 'city' and select 'Afghanistan' for country (Go on to test no. without any actions.)| click ‘publish’ | A message says "Please fill out this field" for the title | A message says "This field is required." appears for title, content and city | fail |[image](./media/manual-tests/write_stories/14.png)|2023/8/16|

- Tests no. 11-14 failed.  Even though these results turned out to be different from the expectation, a validation message tells users to fill out the field, so the features do not need to be corrected.

#### Search Stories
As preparatory steps, go to admin and change the poems as follows:
Delete all other posts.

title| author | content | city | country | category | published date|
|:---| :--- | :--- |:---| :--- | :--- |:--- |
|blog 1| testuser | protecting animals odd numbers | Dublin | Ireland | protecting animals |2023/8/1|
|blog 2| testuser | protecting aquatic system content  | Dublin | Ireland | protecting aquatic system |2023/8/1|
|blog 3| testuser |protecting soil & trees odd numbers  | Dublin | Ireland | protecting soil & trees content |2023/8/6|
|blog 4| testuser |saving resources content| Freiburg | Germany | saving resources |2023/8/6|
|blog 5| admin |saving resources odd numbers | Freiburg | Germany |saving resources |2023/8/18|
|blog 6| admin |saving resources content | Freiburg | Germany | saving resources |2023/8/18|

Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- | :--- |
|1|search by title|—|enter ‘6’ for title and click ‘search’|’blog 6’ will be displayed.|’blog 6’ is displayed.|Pass|[image](./media/manual-tests/search_stories/2.png)|2023/8/19|
|3|search by author|—|enter ‘admin’ for author and click ‘search’|’blog 6’ will be displayed.|’blog 6’ is displayed.|Pass|[image](./media/manual-tests/search_stories/3.png)|2023/8/19|
|4|search by keyword|—|enter ‘odd numbers’ for keyword and click ‘search’|blog 1, 3, 5 will be displayed.|blog 1, 3, 5 are displayed.|Pass|[image](./media/manual-tests/search_stories/4.png)|2023/8/19|
|5|search by likes count|—|enter ‘1’ for ‘liked more than’ field and click ‘search’|blog 4, 5, 6 will be displayed.|blog 4, 5, 6 are displayed.|Pass|[image](./media/manual-tests/search_stories/5.png)|2023/8/19|
|6|search by published date (start date)|—|enter ‘2023/08/01’ for  the published date (start date) and click ‘search’|All 6 blogs will appear.|All 6 blogs appear.|Pass|[image](./media/manual-tests/search_stories/6.png)|2023/8/19|
|7|search by published date (start date)|—|enter ‘2023/08/02’ for  the published date (start date) and click ‘search’|blog 3-6 will appear.|blog 3-6 appear.|Pass|[image](./media/manual-tests/search_stories/7.png)|2023/8/19|
|8|search by published date (end date)|—|enter ‘2023/08/18’ for  the published date (end date) and click ‘search’|All 6 blogs will appear.|All 6 blogs are displayed.|Pass|[image](./media/manual-tests/search_stories/8.png)|2023/8/19|
|9|search by published date (end date)|—|enter ‘2023/08/17’ for  the published date (end date) and click ‘search’|blog 1-4 will be displayed.|blog 1-4 are displayed.|Pass|[image](./media/manual-tests/search_stories/9.png)|2023/8/19|
|10|search by city|—|enter ‘Dublin’ for  the city and click ‘search’|blog 1-3 will be displayed.|blog 1-3 are displayed.|Pass|[image](./media/manual-tests/search_stories/10.png)|2023/8/19|
|11|search by country|—|enter ‘Germany’ for  the country and click ‘search’|blog 4-6 will be displayed.|blog 4-6 are displayed.|Pass|[image](./media/manual-tests/search_stories/11.png)|2023/8/19|
|12|search by category|—|enter ‘protecting animals’ for  the category and click ‘search’|blog 1 will be displayed.|blog 1 is displayed.|Pass|[image](./media/manual-tests/search_stories/12.png)|2023/8/19|
|**| Test search by multiple factors | ||  |  ||  |  |
|13|search by author & keyword|—|enter ‘admin’ for  the author, enter ‘odd numbers’ for the keyword and click ‘search’|blog 5 will be displayed.|blog 5 is displayed.|Pass|[image](./media/manual-tests/search_stories/13.png)|2023/8/19|
|14|search by likes count & published start date|—|enter ‘1’ for  ‘liked more than’ field, enter ‘2023/08/10’ for the published start date and click ‘search’|blog 5 & 6 will be displayed.|blog 5 & 6 are displayed.|Pass|[image](./media/manual-tests/search_stories/14.png)|2023/8/19|
|15|search by author & keyword & category|—|enter ‘testuser’ for  the author, ‘odd numbers’ for keyword, enter ‘saving resources’ for the category and click ‘search’|A note ’no results’ will be displayed.|Note ‘no results’ is displayed.|Pass|[image](./media/manual-tests/search_stories/15.png)|2023/8/19|
|16|enter spaces and search|—|enter spaces for title, author, keyword and city and click ‘search’|All blogs are displayed.|All blogs are displayed.|Pass|[image](./media/manual-tests/search_stories/16.png)|2023/8/19|
|17|'liked more than' field accepts only a number|—|enter 'a' for 'liked more than' field.|'a' can't be entered. |'a' can't be entered.|Pass|[image](./media/manual-tests/search_stories/17.png)|2023/8/19|

#### Image Transformation
("Write Stories" and "Update Stories")

Test No.| Feature | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|image transformation (code in line 40-45 in blog.models.py)|Go to ‘Write Stories.’ Enter ‘test image transformation’ for title, ‘content’ for content, ‘test’ for city, ‘Afghanistan’ for country, upload ‘test_transformation.jpg,’ and click ‘Save’|Inspect the photo| The photo will be cropped to 510 x 340 px. The photo shows the face and the torso of the person (testing the function “gravity: ‘auto’”)  The file size is significantly reduced.|The photo was cropped to 510 x 340px. The photo shows the face and the torso of the person. The file size was reduced from 1.5MB to 33.0kB.|pass|[image1 ](./media/manual-tests/img_transform/1.png)[image2 ](./media/manual-tests/img_transform/1-2.png)|2023/05/02|

#### Update Stories
As preparation,<br>
1. Sign in as testuser, go to "Write Stories," enter "test title 2" for title, "content" for the content, "test city" for city, select 'Afghanistan' for country.
2. click "Save"
3. go to "My page" and click on the link "Read the full story" of the blog "test title 2"
4. click "Update" 

Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|1|Make all fields empty| delete prepopulated title, content, city and unselect the country | click 'save' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass |[image](./media/manual-tests/update_stories/1.png)|2023/08/16|
|2|Make all fields empty| delete prepopulated title, content, city and unselect the country | click 'save' | A message says "Please fill out this field" for the title | A message says "Please fill out this field" for the title | pass |[image](./media/manual-tests/update_stories/2.png)|2023/08/16|
|3|Make title field empty | delete the title but keep the other fields populated | click 'save' | A message says "Please fill out this field" for the title | The title filed is activated, but no message is displayed.| fail|[image](./media/manual-tests/update_stories/3.png)|2023/08/16|
|4|Make title field empty | delete the title but keep the other fields populated| click 'submit' | A message says "Please fill out this field" for the title | The title filed is activated, but no message is displayed. | fail|[image](./media/manual-tests/update_stories/4.png)|2023/08/16|
|5|Make content field empty | delete the content but keep the other fields populated | click 'save' | A message says "Please fill out this field" for the content | A message says "Please fill out this field" for the content | pass|[image](./media/manual-tests/update_stories/5.png)|2023/08/16|
|6|Make content field empty | delete the content but keep the other fields populated | click 'submit' | A message says "Please fill out this field" for the content | A message says "Please fill out this field" for the content | pass|[image](./media/manual-tests/update_stories/6.png)|2023/08/16|
|7|Make city field empty | delete the city but keep the other fields populated | click 'save' | A message says "Please fill out this field" for city | A message says "Please fill out this field" for city | pass|[image](./media/manual-tests/update_stories/7.png)|2023/08/16|
|8|Make city field empty | delete the city but keep the other fields populated | click 'submit' | A message says "Please fill out this field" for city | A message says "Please fill out this field" for city| pass|[image](./media/manual-tests/update_stories/8.png)|2023/08/16|
|9|Unselect country | unselect the country  | click 'save' | A message tells the country must be selected. | "Please select an item in the list" for the country | pass|[image](./media/manual-tests/update_stories/9.png)|2023/08/16|
|10|Unselect country | unselect the country | click 'submit' | A message telss the country must be selected.| "Please select an item in the list" for the country | pass|[image](./media/manual-tests/update_stories/10.png)|2023/08/16|
|11|enter spaces | enter spaces in the title, content and city fields.  | click 'save' | A message tells the fields must be filled. | Message "This field is required" is displayed for the title, content and city| pass|[image1 ](./media/manual-tests/update_stories/11.png)[image2](./media/manual-tests/update_stories/11-2.png)|2023/08/16|
|12|enter spaces | enter spaces in the title, content and city fields.  | click 'submit' | A message tells the fields must be filled. | Message "This field is required" is displayed for the title, content and city| pass|[image1 ](./media/manual-tests/update_stories/12.png)[image2](./media/manual-tests/update_stories/12-2.png)|2023/08/16|
|13|cancel functionality | change the title and content to 'test title 2 updated' & 'content updated'. Change the country to Aland Islands| click 'cancel' | Redirected to "detail page." And the fields remain unchanged. | Redirected to "detail page." And the fields remain unchanged. | pass|[image1 ](./media/manual-tests/update_stories/13.png)[image2](./media/manual-tests/update_stories/13-2.png)|2023/08/16|

*test no. 3 & 4 failed, and these issues will be discussed later in [Test summary](#test-summary) section.*

#### My Page
To prepare<br>
1. sign up with username testuser3
2. go to "Write Stories" page, and make 4 new posts with the titles: blog 11, blog 12, blog 13, blog 14.
3. go to admin panel and publish the 4 posts one by one in the ascending order.
4. go to detail page of the 4 posts and bookmark them.
5. enter "test comment" as comment in all 4 posts and click "submit"

**"Written by me" section**<br>
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|The layout|--| Go to "My Page" | blog 14, blog 13, blog 12 appear in the order, and "Show more" button is shown. | blog 14, blog 13, blog 12 appear in the order, and "Show more" button is shown.|pass|[image](./media/manual-tests/my_page/1.png)|2023/08/17|
|2|The layout|--| Click "Show more" | blog 11 is displayed below blog 14-12. | blog 11 is displayed below blog 14-12.|pass|[image](./media/manual-tests/my_page/2.png)|2023/08/17|

**"Commented by me" section**<br>
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|3|The layout|--| Go to "My Page" | blog 14, blog 13, blog 12 appear in the order, and "Show more" button is shown. | blog 14, blog 13, blog 12 appear in the order, and "Show more" button is shown.|pass|[image](./media/manual-tests/my_page/3.png)|2023/08/17|
|4|The layout|--| Click "Show more" | blog 11 is displayed below blog 14-12. | blog 11 is displayed below blog 14-12.|pass|[image](./media/manual-tests/my_page/4.png)|2023/08/17|

**"Bookmarked by me" section**<br>
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|5|The layout|--| Go to "My Page" | blog 14, blog 13, blog 12 appear in the order, and "Show more" button is shown. | blog 14, blog 13, blog 12 appear in the order, and "Show more" button is shown.|pass|[image](./media/manual-tests/my_page/5.png)|2023/08/17|
|6|The layout in "Bookmarked by me"|--| Click "Show more" |blog 11 is displayed below blog 14-12. | blog 11 is displayed below blog 14-12.|pass|[image](./media/manual-tests/my_page/6.png)|2023/08/17|

**Show more/less buttons in "Written by me" section**<br>
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|7|"Show more" button| -- |Click "Show more"| blog 11 will be displayed, and the label of the clicked button will change to "Show less" | blog 11 is displayed, the clicked button says "Show less"|pass|[image](./media/manual-tests/my_page/7.png)|2023/08/17|
|8|"Show less" button (upper) | -- |Click "Show less" | "blog 11" will disappear. The clicked button will say "Show more" |"blog 11" disappears.  The clicked button says "Show more" | pass|[image](./media/manual-tests/my_page/8.png)|2023/08/17|
|9|"Show less" button (lower) | Click on "Show more" |Click on "Show less" | "blog 11" will disappear. The button below 3 posts (blog 12-14) will say "Show more" |"blog 11" disappears.  The button below 3 posts (blog 12-14) says "Show more" |pass|[image](./media/manual-tests/my_page/9.png)|2023/08/17|

**Show more/less buttons in "Commented by me" section**<br>
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|10|"Show more" button| -- |Click on "Show more"| blog 11 will be displayed, and the label of the clicked button will change to "Show less" | blog 11 is displayed, the clicked button says "Show less"|pass|[image](./media/manual-tests/my_page/10.png)|2023/08/17|
|11|"Show less" button (upper) | -- |Click "Show less" | "blog 11" will disappear. The clicked button will say "Show more" |"blog 11" disappears.  The clicked button says "Show more" | pass|[image](./media/manual-tests/my_page/11.png)|2023/08/17|
|12|"Show less" button (lower) | Click on "Show more" |Click "Show less" | "blog 11" will disappear. The button below 3 posts (blog 12-14) will say "Show more" |"blog 11" disappears.  The button below 3 posts (blog 12-14) says "Show more" |pass|[image](./media/manual-tests/my_page/12.png)|2023/08/17|

**Show more/less buttons in "Bookmarked by me" section**<br>
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|13|"Show more" button| -- |Click on "Show more"| blog 11 will be displayed, and the label of the clicked button will change to "Show less" | blog 11 is displayed, the clicked button says "Show less"|pass|[image](./media/manual-tests/my_page/13.png)|2023/08/17|
|14|"Show less" button (upper) | -- |Click on "Show less" | "blog 11" will disappear. The clicked button will say "Show more" |"blog 11" disappears.  The clicked button says "Show more" | pass|[image](./media/manual-tests/my_page/14.png)|2023/08/17|
|15|"Show less" button (lower) | Click on "Show more" |Click on "Show less" | "blog 11" will disappear. The button below 3 posts (blog 12-14) will say "Show more" |"blog 11" disappears.  The button below 3 posts (blog 12-14) says "Show more" |pass|[image](./media/manual-tests/my_page/15.png)|2023/08/17|

**Test if clicking "Show more" and "Show less" buttons in different sections will function normally**<br>
Preparation:
1. click "Show more" in "Written by me"
2. click "Show more" in "Commented by me"

Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |
|16|Show more/less buttons in different sections | -- |Click "Show less" in "Commented by me"| "blog 11" in "Commented by me" will disappear. The button in "Commented by me" will say "Show more" | "blog 11" in "Commented by me" disappears. The button in "Commented by me" section says "Show more" | pass|[image](./media/manual-tests/my_page/16.png)|2023/08/17|

#### Become a Member
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|link “sign in” | Go to “Become a Member” page | Click the link where it says "Already have an account.... 'sign in'" | Redirected to the sign in page| Redirected to the sign in page |pass|[image](./media/manual-tests/become_a_member/1.png)|2023/8/19|
|2|leave all fields empty| --|click “Sign up” button|A validation error message says “Please fill out this field for the username field| A validation error message says “Please fill out this field” for the username field |pass|[image](./media/manual-tests/become_a_member/2.png)|2023/8/19|
|3|Leave the second password empty|Enter “testuser1” for the username; “abc@test.com” for the email; “swUf8LcR” for the first password field |click “Sign up” button|A validation error message says “Please fill out this field” for the second password field| A validation error message says “Please fill out this field” for the second password field |pass|[image](./media/manual-tests/become_a_member/3.png)|2023/8/19|
|4|Leave the first password empty|Enter “testuser1” for the username; “abc@test.com” for the email; “swUf8LcR” for the second password field |click “Sign up” button|A validation error message says “Please fill out this field” for the first password field.| A validation error message says “Please fill out this field” for the first password field. |pass|[image](./media/manual-tests/become_a_member/4.png)|2023/8/19|
|5|Leave email empty|Enter “testuser1” for the username; “swUf8LcR” for the first password field; “swUf8LcR” for the second password field |click “Sign up” button|Redirected to “Home” page and the message says “Successfully signed in as testuser1” | Redirected to “Home” page and the message says “Successfully signed in as testuser1” |pass|[image](./media/manual-tests/become_a_member/5.png)|2023/8/19|
|6|Leave username empty|Enter “def@test.com” for the email; “swUf8LcR” for the two password fields; |click on “Sign up” button|A validation error message says “Please fill out this field” for the username field| A validation error message says “Please fill out this field” for the username field |pass|2[image](./media/manual-tests/become_a_member/5.png)|2023/8/19|
|7|Use already registered username| Enter “testuser1” for the username; “swUf8LcR” for the first password field; “swUf8LcR” for the second password field |click “Sign up” button|A validation message says “A user with that username already exists”| A validation message says “A user with that username already exists”| pass|[image](./media/manual-tests/become_a_member/7.png)|2023/8/19|
|8|Use already registered email| Enter “testuser2” for the username; "test@ecopost.com” for the email; “swUf8LcR” for the two password fields |click “Sign up” button|A validation message says “A user is already registered with this email address.”| A validation message says “A user is already registered with this email address.”| pass|[image](./media/manual-tests/become_a_member/8.png)|2023/8/19|
|9|Use common password| Enter “testuser2” for the username; “def@test.com” for the email; “password” for the two password fields |click “Sign up” button |A validation message says “This password is too common.”| A validation message says “This password is too common.”| pass|[image](./media/manual-tests/become_a_member/9.png)|2023/8/19|
|10|enter two different passwords| Enter “testuser2” for the username; “def@test.com” for the email; “rDw74kRmW” for the first password field; “Adr49PwTeB” for the second password field |click “Sign up” button|A validation message says “You must type the same password each time.”| A validation message says A validation message says “You must type the same password each time.”| pass|[image](./media/manual-tests/become_a_member/10.png)|2023/8/19|
|11|Enter all appropriate data| Enter “testuser2”; “def@test.com” for email; “swUf8LcR” for both password fields| click on“Sign up” button|Redirected to “Home” page, and a message says “Successfully signed in as testuser2” | Redirected to “Home” page, and a message says “Successfully signed in as testuser2”| pass|[image](./media/manual-tests/become_a_member/11.png)|2023/8/19|

#### Sign in
Test No.| Feature tested | Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Enter all appropriate data| Enter “testuser”; “gR48NmYr1” for both password fields| click “Sign in”|Redirected to “Home” page, and a message says “Successfully signed in as testuser” | Redirected to “Home” page, and a message says “Successfully signed in as testuser”| pass|[image](./media/manual-tests/signin/1.png)|2023/8/19|
|2|Leave username empty| Enter “gR48NmYr1” for password| click “Sign in”|A message says "Please fill out this field" for username | A message says "Please fill out this field" for username| pass|[image](./media/manual-tests/signin/2.png)|2023/8/19|
|3|Leave password empty| Enter “testuser” for username| click “Sign in”|A message says "Please fill out this field" for password| A message says "Please fill out this field" for password| pass|[image](./media/manual-tests/signin/3.png)|2023/8/19|
|4|Enter wrong password| Enter “testuser” for username; "wrongpw" for password | click “Sign in”|A message says "username and/or password you specified are not correct" | A message says "username and/or password you specified are not correct" | pass|[image](./media/manual-tests/signin/4.png)|2023/8/19|
|5|Enter wrong username| Enter “nouser” for username; "gR48NmYr1" for password | click “Sign in”|A message says "username and/or password you specified are not correct" | A message says "username and/or password you specified are not correct" | pass|[image](./media/manual-tests/signin/5.png)|2023/8/19|
|6|Remember me function| Enter “testuser” for username; "gR48NmYr1" for password; put a check for "Remember me" and sign in. Sign out and go back to the sign in page| Enter "testuser" for username | The password will be automatically filled out. | The password is not automatically filled out. | fail|[image](./media/manual-tests/signin/6.png)|2023/8/19|

*test no. 6 failed.  This issue will be discussed in [Test summary](#test-summary) section.*

#### Sign out
Test No.| Feature tested| Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail | Image |Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|“Sign out” button|Sign in as "testuser." Click "Sign out" in the navigation bar. |Click "Sign out"|Redirected to "Home" page, and the flash message says, "You have signed out." | Redirected to "Home" page, and the flash message says, "You have signed out." |pass|[image](./media/manual-tests/signout/1.png)|2023/8/19|

### Test summary

The following failed tests need to be discussed.

**Manual tests ‘Update Stories’ section test no. 3 & 4**

When the title field is made empty and ‘Update’ is clicked, a validation message should state the title should be filled out, but no message shows up.  I need to overwrite the customized validation, but I didn’t find the way to do that as of August 19th, 2023.  The form doesn’t get submitted without a title, so this will not cause a serious issue.  I will keep working on the issue.

**Manual tests 'Sign in' section test no. 6**

The check box ‘Remember me’ doesn’t function as expected.  If the checkbox is clicked, the password should be automatically filled out the next time the user enters the username, but when the function was tested, the password remained unfilled.  This doesn't cause a serious problem in the app, but I will try to fix the issue in the future.