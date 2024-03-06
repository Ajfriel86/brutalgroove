# Music Blog Site: Brutal Groove

**Deployed website: [Link to website](https://brutalgroove-1df729525c70.herokuapp.com/)**


![Main image](documentation/brutal_groove.png)

## About
"Brutal Groove" is an independent music blog covering all aspects of underground music. It includes comment sections on each blog article, along with the ability to like or unlike a particular post. 
As well as there there are role-based profiles for staff members and basic users alike. Staff members will have access to the admin panel upon login whereas basic users will not have this functionality. Admin users will also have the option to adjust the carousel images via the back end and attach a caption with each image. There is also a contact form available for any advertisers who to to promote their products or brand through this site.  

---

## UX
The website was created to have an eye-catching appeal with an emphasis on the content and user experience. The user can navigate easily throughout the site as well as leave comments, delete their comments, and like / unlike posts. The site is easily scalable with the ease of adding content via the admin panel.  


### Target Audience
This website is intended for users who are interested in rock, metal, or anything underground in terms of music-related journalism.  


### User Stories


| Issue ID    | User Story |
|-------------|-------------|
| [#1](https://github.com/Ajfriel86/brutalgroove/issues/1) | **Site Pagination:** As a Site User I can view a paginated list of posts so that easily view posts and select as needed |
| [#2](https://github.com/Ajfriel86/brutalgroove/issues/2) |**View Post List:** As a Site User, I can view a list of posts so that I can select one to read|
| [#3](https://github.com/Ajfriel86/brutalgroove/issues/3) |**Open a post:** As a Site User, I can click on a post so that I can read the full text. |
| [#4](https://github.com/Ajfriel86/brutalgroove/issues/4) |**View likes:** As a Site User / Admin, I can view the number of likes on each post so that I can see which is the most viral. |
| [#5](https://github.com/Ajfriel86/brutalgroove/issues/5) |**View comments:** As a Site User / Admin I can view comments on an individual post so that I can read the conversation. |
| [#6](https://github.com/Ajfriel86/brutalgroove/issues/6) |**Account registration** As a Site User I can register an account so that I can comment and like|
| [#7](https://github.com/Ajfriel86/brutalgroove/issues/7) |**Comment on a post:** As a Site User I can leave comments on a post so that I can be involved in the conversation|
| [#8](https://github.com/Ajfriel86/brutalgroove/issues/8) |**Like / Unlike:** As a Site User I can like or unlike a post so that I can interact with the content |
| [#9](https://github.com/Ajfriel86/brutalgroove/issues/9) |**Manage posts:** As a Site Admin I can create, read, update and delete posts so that I can manage my blog content|
| [#10](https://github.com/Ajfriel86/brutalgroove/issues/10) |**Create drafts:** As a Site Admin I can create draft posts so that I can finish writing the content later |
| [#11](https://github.com/Ajfriel86/brutalgroove/issues/11) |**Approve comments:** As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments|
| [#12](https://github.com/Ajfriel86/brutalgroove/issues/12) |**Carousel Basic Upload Functionality:** As a site admin, I can upload multiple hero images to the carousel so that visitors are greeted with a dynamic and visually appealing homepage.|
| [#13](https://github.com/Ajfriel86/brutalgroove/issues/13) |**Carousel Caption Addition:** As a site admin, I can add captions to each hero image so that visitors can understand the context or message associated with each image.|
| [#14](https://github.com/Ajfriel86/brutalgroove/issues/14) |**Carousel Image Activation:** As a site admin, I can select which hero images are active so that only relevant and current images are displayed to visitors.|
| [#15](https://github.com/Ajfriel86/brutalgroove/issues/15) |**Carousel Editing Captions:** As a site admin, I can edit the captions of existing hero images so that I can correct errors or update the text to stay relevant.|
| [#16](https://github.com/Ajfriel86/brutalgroove/issues/16) |**Carousel Previewing Changes:** As a site admin, I can remove hero images from the carousel so that I can keep the carousel content fresh and relevant.|
|[#18](https://github.com/Ajfriel86/brutalgroove/issues/18) |**Contact Form - Submit Inquiry:** As a site visitor, I can submit inquiries through the contact form so that I can get answers to my questions or further information about the services/products offered.|
| [#19](https://github.com/Ajfriel86/brutalgroove/issues/19) |** Contact Form - Receive Confirmation:** As a site visitor, I can receive immediate confirmation after submitting the contact form so that I know my message has been successfully sent and will be looked at.|


### User Acceptance Criteria

#### General Site Functionality
 - Homepage Load Time: The homepage of the blog must load within 3 seconds over a standard broadband connection.
- Responsive Design: The site must be fully responsive, displaying correctly on desktop browsers, tablets, and smartphones, with no horizontal scrolling required.
Accessibility: The site must meet WCAG 2.1 AA standards to ensure it is accessible to users with disabilities.

#### User Interface and Experience
- Navigation: Users must be able to navigate to all sections of the blog from the homepage within two clicks.
- Content Readability: Blog posts must use a legible font size (minimum 16px for body text) and contrast ratios that comply with WCAG 2.1 AA standards for text and background colors to ensure readability.

- Image Loading and Quality: Images within blog posts must load within 2 seconds and must be optimized for the web without compromising on quality. Images should be displayed at a resolution that looks sharp on both high-density (Retina) and standard displays.

- Interactive Elements Feedback: Interactive elements (e.g., buttons, links, comment submission form) must provide immediate visual feedback when interacted with (e.g., hover or focus states) to indicate their functionality.

- Author Profiles: An overview of the authors on the site

- Mobile Menu Usability: On mobile devices, the site must offer an easily accessible and navigable menu to access different sections of the blog without pinching or zooming.

- Error Handling and Messages: The site must display user-friendly error messages for any issues encountered (e.g., failed comment submission, broken links), guiding users on possible next steps.

- Custom 404 Page: The blog must have a custom 404 error page that maintains the site's branding and offers links back to the homepage or popular sections, reducing user frustration on encountering dead links.

- Footer Accessibility: Ensure the footer of the site is accessible from any point within the site without excessive scrolling, containing links to important pages such as About, Contact, and Privacy Policy.

#### Content and Features
- Blog Post Creation: Authorized users must be able to create, edit, and publish blog posts, including text, images, and embedded media, through a CMS interface.
 - Comment System: Readers must be able to leave comments on blog posts. New comments should appear immediately after submission pending moderation.

#### Security and Data Protection
- User Accounts: Users must be able to create, edit, and delete their accounts. Passwords must be encrypted, and the site must offer a password reset feature via email.
- Data Privacy: The blog must comply with GDPR/CCPA, providing users with a clear privacy policy and options to manage their data.

#### Performance and Scalability
- Uptime: The blog must maintain 99.9% uptime, excluding scheduled maintenance windows.
- Scalability: The site must be able to handle spikes in traffic, supporting up to 10,000 concurrent users without significant performance degradation.

#### Testing and Release
- User Acceptance Testing (UAT): Before launch, a beta version of the site will be made available to a select group of users for feedback. At least 95% of identified issues must be resolved before the official release.
- Launch Readiness: The site must pass a final UAT with no critical issues remaining. Feedback on usability must be overwhelmingly positive from at least 80% of beta testers.

---

## Future Development

#### Down Votes
A future feature to add is a "down-voting" option as seen on sites such as Reddit. This would enhance the US for users.


#### Writes: Backend Model for easier updating of Writes
A future feature to add is a model that can handle the "Meet the Writers" section where pictures of the writers and overviews of them can easily be updated, changed, or reviewed. 

#### Email Verification
A future feature to add is a more robust email verification mechanism. Where the user will have to verify their emails by clicking a link that is sent to their email address

#### Forgotten Password Authentication
A future feature to add is the enablement of "Forgotten Passwords." Here a user, or admin staff, could avail of changing their password if they have forgotten it.

#### Enabling "Remember Me"
A future feature to add is the "Remember me" option while signing into the site. This would help enhance the UX for users.

---


## Technologies used

### Languages:
+ [Python](https://www.python.org/downloads/release/python-385/): The primary language used to develop the server side of the website.
+ [JS](https://www.javascript.com/): The primary language used to develop interactive components of the website.
+ [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): The markup language used to create the website.
+ [CSS](https://developer.mozilla.org/en-US/docs/Web/css): The styling language used to style the website.

### Frameworks and libraries:
+ [Django](https://www.djangoproject.com/): Python framework used to create all the logic.
+ [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/): The style framework used to create the layout of the site.

### Databases:

+ [SQLite](https://www.sqlite.org/): was used as a development database.
+ [PostgreSQL](https://www.postgresql.org/): the database used to store all the data.

### Other tools:
+ [Git](https://git-scm.com/): This is the version control system used to manage the code.
+ [Pip3](https://pypi.org/project/pip/): This is the package manager used to install the dependencies.
+ [Gunicorn](https://gunicorn.org/): This is the web server used to run the website.
+ [Psycopg2](https://www.psycopg.org/): This is the database driver used to connect to the database.
+ [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): This is the authentication library used to create user accounts.
+ [Django-crispy-forms](https://django-cryptography.readthedocs.io/en/latest/): was used to control the rendering behavior of Django forms.
+ [GitHub](https://github.com/): This is used to host the website's source code.
+ [VSCode](https://code.visualstudio.com/): This is the IDE used to develop the website.
+ [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): This was used to debug the website.
+ [Font Awesome](https://fontawesome.com/): This was used to create the icons used in the website.
+ [Google Fonts](https://fontawesome.com/): This was used to create the icons used in the website.
---

## Features
### Home Page
![Home Page](documentation/home.png)

#### Blog Posts On Home Page
![Blog Posts](documentation/blog.png)

#### Approval Message
![Approval](documentation/approval.png)

#### Comments on Blog Posts (CRUD)
![Comments](documentation/commented.png)

### Contact Page
![Contact Page](documentation/contact.png)

### Register/Signup Page
![Register](documentation/reg.png)

### Logout Page
![Logout Page](documentation/signout.png)

### Custom 404 Page
![Custom 404](documentation/404.png)

### Custom 500 Page
I have created a custom 500 page but I have not triggered this to capture a screenshot. Below is the code for this to be handled.
![Custom 500](documentation/500.png)

---
## Design
The core design for the website was taken from a [Bootstrap template](https://getbootstrap.com/docs/5.0/examples/carousel/)

- Here I added my own touches to colours & typography

### Typography
The [Google Fonts](https://fontawesome.com/) font Inconsolata was used to display text throughout the site. 
![Inconsolata](documentation/type.png)

### Wireframes
#### Home Page
![Wire Frames](documentation//wireframes_1.png)
#### Blog Page
![Wire Frames](documentation/wireframes_2.png)
#### Contact Page
![Wire Frames](documentation/wireframes_3.png)
#### Sign Out Page
![Wire Frames](documentation/wireframes_4.png)
#### Sign Up Page
![Wire Frames](documentation/wireframes_5.png)


---

## Agile Methodology

### GitHub Project Management
GitHub Project Management was used to manage this project. This was used to create issues with GitHub which related to user stories. These User Stories when then imported into Actions and set as a roadmap. This helped me stay on top of the project and ensure I had a Minimal Viable Product (MVP) at the end of the project

![Issues](documentation/issues.png)

![Road Map](documentation/roadmap.png)


---

## Information Architecture

### Database


### Data Modeling
![Data Model](documentation/data_model.png)

![Data Model](documentation/data_model_two.png)

### Data Schema
![Data](documentation/data.png)


---
## Testing

### Python
#### admin.py Pass
![admin.py](documentation/admin_linter.png)

#### apps.py Pass
![apps.py](documentation/apps_linter.png)

#### env.py Pass
![env.py](documentation/env_linter.png)

#### forms.py Pass
![forms.py](documentation/forms_linter.png)

#### manage.py Pass
![manage.py](documentation/manage_linter.png)

#### models.py Pass
![model.py](documentation/models_linter.png)

#### Project urls.py Pass
![project urls.py](documentation/project_urls_linter.png)

#### settings.py Pass
![settings.py](documentation/settings_linter.png)

#### views.py Pass
![views.py](documentation/views_linter.png)

#### tests.py Pass
![tests.py](documentation/tests_linter.png)

##### Running tests.py Fail
![Fail](documentation/python_test_fail.png)

##### Removing the issue
![Remove](documentation/python_test_remove.png)

##### Running tests.py  Pass
![Pass](documentation/python_test_pass.png)


### JavaScript

My JavaScript files are from [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/). This is not custom JavaScript. As a result, some errors were present in validating these files. But we were instructed to document and leave them as is.  

### HTML
#### Home Page Pass
![Home Page](documentation/w3_validator_home.png)
#### Contact Page Pass
![Contact Page](documentation/w3_validator_contact.png)
#### Sign Up Page Pass
![Signup Page](documentation/w3_validator_signup.png)
#### Log Out Page Pass
![Log Out Page](documentation/w3_validator_logout.png)
### CSS Pass
![style.css](documentation/css_test.png)
---



## Deployment

Please see the [DEPLOYMENT.md](https://github.com/Ajfriel86/brutalgroove/blob/main/DEPLOYMENT.md)

---

## Credits

- [GitHub](https://github.com/) for project management.
- [Django](https://www.djangoproject.com/) for the framework.
- [Font awesome](https://fontawesome.com/): for the free access to icons.
- [Heroku](https://dashboard.heroku.com/): for hosting.
- [ElephantSQL](https://www.elephantsql.com/): for providing the database.
- [amiresponsive](https://ui.dev/amiresponsive): for the mockup image.
- [fontawesome](https://fontawesome.com/): for providing the icons.
- [googlefonts](https://fonts.google.com/): for providing the fonts.
- [iTech e-Learn](https://www.youtube.com/watch?v=EPzUN97KvNU&list=PLuJZH5pDX4GKrPyVImrii6mZ3kdwAOLvv): for their in-depth Django tutorials.
- [Pixabay](https://pixabay.com/): for providing the hero images on the carousel.

### Content and Images
- [Pitchfork](https://pitchfork.com/reviews/albums/23019-emperor-of-sand/): for their album review of Mastodon Emperor of Sand
- [Sputnik Music](https://www.sputnikmusic.com/review/81075/Igorrr-Spirituality-and-Distortion/): for their review of Igorrr - Spirituality and Distortion
- [BlabberMouth.Net](https://blabbermouth.net/news/mastodons-bill-kelliher-how-i-got-sober): for their interview with Bill Kelliher.
- [Audioxide](https://audioxide.com/reviews/boards-of-canada-music-has-the-right-to-children/): for their review of Boards of Canada's Music has a right to the Children.
- [Metal Hammer](https://www.loudersound.com/reviews/elder-lore): for their review of Elder Lore.
- [Pitchfork](https://pitchfork.com/reviews/albums/mastodon-hushed-and-grim/): for their review of Mastodon's Hushed and Grim.


## Acknowledgments
[Iuliia Konovalova](https://github.com/IuliiaKonovalova): I would like to thank my mentor for constant support throughout this project.
