# Overhead Manager

Overhead Manager is a simple to use timesheet platform where you can post your work hours based upon your work sector. The example used is based on some previous real life work undertaken in an architects firm. The data used, uses actual overhead costing but the names and values have all changed due to confidentiality. The idea originally arose from a period of work experience undertaken where I worked out the cost analysis and management reports for the company to help them work out their profitability ratios per sector.

<details>

<summary>Overhead Manager</summary>

![Desktop View](images/desktop_wireframe.png)
</details>


# User Stories

## User Goals

* To provide the user with an easy to navigate timesheet portal to track hours worked in a specific sector.
* To present the user with a layout that is easy to understand and read.
* To allow the user to view graphs of previous financial years results and current expectations.

### As a user I want to:

* I want to understand the main purpose of the website.
* I want to be able to naavigate the website, understand the concept of the website and use the website confidently.
* I want to be able to discuss the website with other potential users.

# Design

## Imagery and colour scheme

* The colour scheme of the site was given careful consideration. The colours used in the website is important to the overall experience of the user.
* The colour scheme was chosen based on what colours are easy on the eye and also bearing in the mind the colour scheme of accounting software.
* Once the colours were chosen, it was a test to see if they blended together, the gentle red is easy on the eye and the green is just enough to capture the attention of where the user needs to go.
  
## Layout

The website is split into 3 sections:

* Home
* Timesheets
* Reports

## Timesheets and reports features

### Timesheet Page
![Timesheet Page](images/timesheet.png)
* When the user clicks the timesheet page, this is what they are greeted with.
    * They then choose the sector they wish to post into,
    * Their name,
    * How many hours they worked
*  After this they are then greeted with a view of the current state of hours worked in the month  
![Timesheet Table](images/timesheet_section.png)
* After this, the use can choose to input another timesheet where they will be redirected back to the front page to be able to post another timesheet.

### Reports Section
![Reports Page](images/reports_page.png)
* This is the section where the user can view data from previous financial years to compare how long they spent working on projects in other sectors.
* This is for the management to look at as the data in here would grasp on teh financials and show you in a clear concise way where time is being spent as well as where the money is being earned.

### Layout change

* The layout of the website changed mostly due to the idea being changed. Originally this was going to be a cost managment system for manufacturing products, however, this idea would have been over time consuming and impractical. The idea became to just focus on the analytical areas on the information I already had stored from my time working in the company.
* The idea still pulls through from the google sheet, using two different ones for the different sections. Timesheets uses the current month sheet, where reports uses the old financial year sheet.
![November](images/november.png)
![FY22/23](Milestone-project-3/images/fy.png)

# Testing

### Validator testing
  - ## HTML
    - No errors were returned after passing code through official W3C Markup Validator.
      - ![HTML Validator](assets/images/readme-images/html-validator.png)
  - ## CSS
    - No errors were found when passing CSS code through official W3C CSS Validator.
    - ![CSS Validator](assets/images/readme-images/css-validator.png)
  - ## JavaScript
    - No errors were returned when passing through the JSHint Validator (https://jshint.com/)
      - ![JS Validator](assets/images/readme-images/js-validator.png)

### Button testing

- All buttons were tested manually to make sure the navigation for the user was correct.

### Game testing

- The game was tested by numerous family and friends to ensure everything was working and as they would have different levels of knowledge, it helped to go further into the quiz to see if it responded the same. Things that were tested included:
  - Question shows correctly when the quiz starts,
  - The How To section shows the instuctions clearly,
  - When the timer runs out the game ends and the user can no longer click,
  - When the user chooses the wrong answer the game ends and they can no longer click,
  - When the user gets a question right, the question changes and the timer restarts,
  - The timer stops when the game ends,
  - The game over pop up shows correctly and,
  - The win game pop up shows correctly.

### Browser testing

- The game was tested on Google Chrome, Microsoft Edge and Safari with no issues reported.

### Device testing

- The game was played on a number of devices, including phones, desktop, laptop and tablet. This was to ensure the game was responsive and the layout looked clear on all devices.

### Bugs fixed in development process

### Question not showing on playing of game

- When the user clicked on the play button, the game wouldn't appear. This was due to the eventListener not having the correct id called to it.
- To fix this, I removed any excess code that didn't relate to the question and the play button and slowly put it in one line at a time to see what I was calling on each line of code.

### Ability to still click answers after game over

- When the timer ran out or you chose a wrong option, you could still click the answers behind the modal until you chose the right answer to move the quiz on.
- This was fixed by adding in let blocked = false; and calling it in my function checkAnswer, so when the answer was false, they could no longer click anything behind the modal.
  
### Timer not reseting on question change

- Upon choosing the correct answer the timer didn't stop its current count, it just carried on. The same was said for the end of game when there was only a few test questions.
- This was fixed by adding in clearInterval(timer); to the winGame and gameOver function.

### Known bugs

- There are no known bugs. After Debugging the quiz works exactly as it should.

# Technologies used

### Languages used

- JavaScript
- HTML
- CSS
- Python

### Programs used

- https://stackoverflow4.com - Used to get advice and tips on how to print from and to google sheets.
- https://github.com/ - Used for hosting.
- https://plotly.com - Used for creation of reports.

### External resources used

- https://stackoverflow.com/ - Used to help get the formula and syntax for printing to and from google sheets.
- https://materializecss.com/ - used to set up pages and format the style

### Media

# Deployment

The site was deployed using GitHub pages. The steps to deploy using GitHub pages are:

1. Go to the repository on GitHub.com
2. Select 'Settings' near the top of the page.
3. Select 'Pages' from the menu bar on the left of the page.
4. Under 'Source' select the 'Branch' dropdown menu and select the main branch.
5. Once selected, click the 'Save'.
6. Deployment should be confirmed by a message on a green background saying "Your site is published at" followed by the web address.

# Ideas for Improvement

### User experience

* Allow first time users to select a subsection of the quiz for something they enjoy more than a general quiz.
* Allow first time users to choose a mode of difficulty for the question bank.
* Allow the ability for first time/returning users to choose how long they want on the timer.
* Starting the quiz from a completely random point, and subsequent questions will be random, so the user won't do the quiz in the same order.
* Tracking the time it takes people to do the quiz. (Completions only)
* Having a set time to complete the whole quiz in.
* Having a local/non-local leaderboard to compare scores and see who did the quiz in the fastest time.

### Development

* Linking an API with a larger question bank for the JavaScript to call on.
* Adding sounds to the timer when it counts down.
* Adding delay to the click function and changing the colour of the answer when correct (like in who wants to be a millionaire).
* Breaks to tell you when the questions increment in difficulty.
