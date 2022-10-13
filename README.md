# PBD INTERNATIONAL CLASS MIDTERM PROJECT
## A Proceeding Conference App
### GROUP 3
1. Syafiqo Arashy Octaviano - 2106657821
2. Nafis Azizi Riza - 2106658843
3. Ammar Ash-Shiddiq - 2106656560
4. Azra Batrisyia Hisman - 2106656592
5. Matthew Rizky Hartadi - 2106720941
6. Theirry Nicole Panggabean - 2106721004

[Link to Deployed Website](ristek.link/MidtermProjectGroup3KI)

### DESCRIPTION OF OUR APP
The app that will be developed is a digital proceeding app for an academic conference. The app will display the information about the conference, such as the schedules, submitted papers, events, speakers, authors and room assignments. There is no need to define any authorization roles (e.g. admin, participant, etc.), meaning anyone can read the information without logging in. The app also has high interactivity, in which the modules are linked to one another. This means that users can easily access any other relevant modules from their current one (e.g. access speakers from events).

### LIST OF MODULES AND FEATURES

#### Landing Page
The website will have a landing page module. The landing page module will be the first thing the user will see when they visit the website. It should contain enough information and feature that’ll get them familiar with the website.

These features consists of:
- Navbar
    1. The functionality of the navbar is to make users navigate easier between pages/sections on the website 
    2. When the user clicks on a page name on the navbar, it’ll redirect them to each respective page
    3. The navbar should always be visible and usable wherever the user goes around the website
- A Hero Section
    1. The hero section will display an image/illustration to let the users know what Conference Event the website Is dedicated to
- Event Section
    1. A brief overview of the event
    2. A button will be used as a CTA(Call-To-Action) for the user to redirect them to the Events Page
- Speakers Section
    1. A button will be used as a CTA(Call-To-Action) for the user to redirect them to the Speakers Page
- Sessions Section
    1. A button will be used as a CTA(Call-To-Action) for the user to redirect them to the Sessions Page
- Footer and Sponsors
    1. Located at the bottom of the page, this footer contains information details regarding the Conference Event and its sponsors

#### Events Page
The events module keeps track of the rundown schedule. This means for each event, the start and end time is recorded as well as its program title, relevant speakers and location. The user is able to interact with certain events. For example, if the event is a parallel session, the user is able to access the parallel sessions page to find out more about said event. On the other hand, if it is a plenary session with a speaker, users are able to interact with the event and find further information on the speaker.

Overall, the data available is:

- Event Id
- Date (Displayed to user): The data is sorted by date. Users can interact by selecting which date they want to look at more closely, and only the sessions available on that day will be shown.
- Start Time
- End Time
- Time (Displayed to user): The start and end times are not shown individually to the user. Instead, it is shown in full.
- Program (Displayed to user): The title of the session
- Speaker (Displayed to user): May be null. Only applies to keynote lectures.
- Place (Displayed to user): Displays the location of the event.
- Is Parallel (Displayed to user): Parallel sessions are listed for users. Although the Boolean value of isParallel itself is not shown to users, they are able to identify which sessions are parallel and which are not, as interacting with the parallel sessions will also lead to the parallel sessions page.
- Is Child: This Boolean value is not explicitly shown to the users, and is mostly used for sorting. This value simply refers to the fact that the event is, in fact, running in parallel.

To implement these features, there would likely need to be a way to implement a sort of table to organize the events, and a filter (e.g. date, subject) to allow ease of access for the users.

URL routing would also need to be implemented towards Speakers and Events, given the user clicks on a certain event.

To conclude, the events module will have its own page where the rundowns are filtered as required by the users, but it will also have interactivity that will lead to sessions and speakers.
