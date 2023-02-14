# PIZZAMAZE

<img src="/workspace/pizzamaze/static/PIZZAMAZE-mockup.png">

## About

PIZZAMAZE is a website for a restaurant with a booking system. The user can book one or more guests for a meal at a particular time and date. The data model "Booking" provides the features and business logic to manage, query and manipulate the customer bookings. It features the ability to avoid double bookings, multiple table occupancies and cancellations. It also offers authorisation, authentication and permission features to provide a new user the ability to create an account and login or logout. The site owner has the ability to also log in to a staff panel and take online bookings for their restaurant. I used Agile methodology to plan and design the website.

The live site can be found here: https://pizzamaze.herokuapp.com/

------

## Features

The website features front-end design for a data-driven web application that meets accessibility guidelines, follows the principles of UX design, meets its given purpose and provides a set of user interactions.

### Title
- The website title appears on every page and redirects the user back to the homepage at any time. It offers common CSS style such as changing color while hovering the cursor above the link. Hovering styles also applies to all the links on the website.<br>
<img src="/workspace/pizzamaze/static/README-active-link.png" style="height:100px"><br>
- A button on the top right corner provides easy booking access to the user.<br>

### Navbar
- The navbar appears on everypage and is reponsive to mobile views. The navbar collapses into a toggle button using Bootstrap code.<br>
    <img src="/workspace/pizzamaze/static/README-navbar.png" style="height:70px"><br>
    <img src="/workspace/pizzamaze/static/README-navbar-toggle.png" style="height:150px">
- On the right side, the navbar also gives access to the user signup page or account page and will show the login or logout links accordingly. It will also show the staff panel link only if the user is already logged in as admin.<br>
    <img src="/workspace/pizzamaze/static/README-navbar-login.png" style="height:70px">
    <img src="/workspace/pizzamaze/static/README-navbar-logout.png" style="height:70px">
    <img src="/workspace/pizzamaze/static/README-navbar-staff.png" style="height:70px">

### Footer
- The footer appears on everypage and is reponsive to mobile views. Instead of showing the contents side-by-side in mobile views, they appear on top of each other. It contains the restaurant's contact information and social media links.<br>
    <img src="/workspace/pizzamaze/static/README-footer.png" style="height:150px">

### Homepage
- The homepage is composed of fours sections. The first is a full-page picture, the second is a short about section describing the beginnings of the restaurant and its philosophy. The third and fourth sections provide easy access to the menu and the booking page.

### About
- The about section contains the restaurant opening times. It also contains the address to the resturant using a google maps iframe. The contents collapse one on top of each other in mobile-view.

### Menu
- The dishes contained in the menu page were created using https://www.name-generator.org.uk/food/. Each section is divided by category with pictures. The layout of the page changes to be responsive to mobile view.

### Booking
- If the user is not logged in or has not created an account yet, the following message will be prompted to the user:<br>
<img src="/workspace/pizzamaze/static/README-account-needed.png" style="height:150px"><br>
- If the user clicks on the button, the user will be redirected to the user registration page:<br>
<img src="/workspace/pizzamaze/static/README-account-needed.png" style="height:150px"><br>
- Each field is required and in the correct format:<br>
<img src="/workspace/pizzamaze/static/README-required.png" style="height:150px"><br>
<img src="/workspace/pizzamaze/static/README-email-format.png" style="height:70px"><br>
- Once completed, the form's submit button redirects the user to the booking page and a message pops-up to alert the user their registration was successful.
<img src="/workspace/pizzamaze/static/README-online.png" style="height:150px"><br>
- Here, the user can select the amount of guests (up to 8), the date up to 21 days ahead (except on Mondays as the restaurant is closed) and the time within the opening hours (9am-9pm) which can also be found on the "about page".
- If the user selects the same time or date as another user previously selected, a message pops-up to alert the user their booking time was selected before to avoid double bookings.
- If there are 11 bookings on a selected day, a message pops-up to alert the user their booking day is full to avoid going over restaurant capacity.
- Then, the user needs to fill out their information and click on submit. The user is then be redirected to the account page and a message pops-up to alert the user their booking was successful.<br>
<img src="/workspace/pizzamaze/static/README-booking-saved.png" style="height:150px"><br>

### Account
- The account page lets the user read, update and delete their booking. They can also view all their bookings if they make more than one.
<img src="/workspace/pizzamaze/static/README-update.png" style="height:150px"><br>
- If the user has no bookings, they will be prompted with the following message:
<img src="/workspace/pizzamaze/static/README-no-booking.png" style="height:150px"><br>

### Contact
- The contact page is a simple contact form. Once completed, the user is alterted that their form was submitted successfully. It will also automatically redirect the user back to the index page after 5 seconds.
------

## Testing
I have manually tested this project by doing the following:<br>
<br>
- Typed invalid inputs (i.e., numbers and typos) when specific strings are expected
- Tested in my local terminal and the Code Institute Heroku terminal
- No errors were found when passing through the official https://pep8ci.herokuapp.com/
- Error messages are present in case of errors:<br>
<img src="/workspace/pizzamaze/static/README-endif.png" style="height:150px"><br>

## Bugs remaining
- If the user makes more than one booking, the "welcome, user" message appears once per booking.

## Ressources

- Media ressources from: https://unsplash.com/
- AI menu generator from: https://www.name-generator.org.uk/food/
- Mockup generator from: https://techsini.com/multi-mockup/index.php
- Restaurant booking tutorial: https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78?gi=809a19b69138
- Django tutorial: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models
- User authentication tutorial: https://www.youtube.com/watch?v=CTrVDi3tt8o&embeds_widget_referrer=https%3A%2F%2Fblog.devgenius.io%2Fdjango-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78&embeds_euri=https%3A%2F%2Fcdn.embedly.com%2F&embeds_origin=https%3A%2F%2Fcdn.embedly.com&source_ve_path=MjM4NTE&feature=emb_title&ab_channel=Codemy.com
