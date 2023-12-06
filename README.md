# Overhead Manager

Overhead Manager is a simple to use timesheet platform where you can post your work hours based upon your work sector. The example used is based on some previous real life work undertaken in an architects firm. The data used, uses actual overhead costing but the names and values have all changed due to confidentiality.

* To provide the user with an easy to navigate quiz game that is challenging whilst also not extensively time consuming.
* To present the user with a website that is visually appealing and fully responsive.
* To allow the user to test their general knowledge against a selection of randomly selected questions.
* To present the user with a quick thinking challenge whilst also not being too restricting.
* To tempt the user to come back and try again to get further and further along. 

# User Stories

## User Goals

### First Time User

* As a first time user I want to understand the main purpose of the quiz.
* As a first time user I want to be able to naavigate the quiz, understand the concept of the quiz, see how far I can get and restart the quiz should I fail.
* As a first time user I want to have fun and also expand my general knowledge.
  
### Returning User

* As a returning user I want to be able to play the same quiz and still enjoy it as much as the first time.
* As a returning user I want to be able to get further than the first time I attempted the quiz.

# Design

## Imagery and colour scheme

* The colour scheme of the site was given careful consideration. The colours used in the quiz is important to the overall experience of the user.
* The background of the site was chosen from a selection of images that relayed with how I wanted the quiz to look. Both images sourced from:
* https://www.freepik.com/free-vector/hand-drawn-question-mark-pattern_26373356.htm#query=question%20mark%20background&position=11&from_view=keyword&track=ais
* https://www.freepik.com/free-vector/hand-drawn-question-mark-pattern_26373361.htm#query=question%20mark%20background&position=15&from_view=keyword&track=ais
* Once the background image was chosen, it was important to make sure the quiz followed suit and so Blue and White became the two dominant colours.
* Making sure the image and the question and answers contrasted was important to make sure the accessibility for the user was always paramount, that is why there is large black backgrounds to take the focus off the background image.

## Fonts

Sans Serif is the default font used for this quiz. There wasn't much reason for changing the font as the question aim was to be readable in a quick manner. Google fonts were imported to explore but ultimately settled on the default font.
  
## Layout

The quiz site is a single page with 3 sections:

* Welcome Area
* Play game
* How to play

## Initial Wireframes

Wireframes were designed on https://wireframe.cc

<details>

<summary>Computer Wireframe</summary>

![Desktop Wireframe](assets/images/readme-images/computer-wireframe.png)
</details>

<details>

<summary>iPad Wireframe</summary>
    
![iPad Wireframe](assets/images/readme-images/ipad-wireframe.png)
</details>
        
<details>

<summary>Mobile Wireframe</summary>
    
![iPhone Wireframe](assets/images/readme-images/iphone-wireframe.png)
</details>

## Features

### Home page

The home page of this website is very simple, it has a H1 heading stating the name of the game and two simplistic buttons to choose from:
- Play
- How to Play
  
![Home page](assets/images/readme-images/home-page.png)

### How to play page

When the user clicks "How the Endless Quiz works", it tkaes them to a little intro secction that explains the main aim of the game, with a back button to return to the main page.

![How To page](assets/images/readme-images/how-to.png)

### Game area

Once the user clicks play the game will start and they will be presented with a question, in which they have 15 seconds to choose one of the 4 options presented to them.

![Game area](assets/images/readme-images/game-area.png)

### Game over

The game can end in one of two ways:
- When time expires, which brings a message saying "Time's up!, or;
- When they select a wrong answer in which a message pops up saying "Game over, wrong answer." with the option to play again.
  
![Game over](assets/images/readme-images/game-over-time.png)
![Game over](assets/images/readme-images/game-over-wrong.png)

### Layout change

* The layout of the website changed mostly as the positioning of the timer wasn't in the middle of the questions. This may have created a harder to read atmosphere and players would focus more on the timer than the actual question/answer due to their eyes being drawn to the timer.
* Rather than two seperate border boxes, one box was used to keep the styling in sync especially when longer questions came out.

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

### Programs used

- https://favicon.io/ - Used to create Favicon.
- https://wireframe.cc - Used to create Wireframe images.
- https://developer.chrome.com/docs/devtools/ - Used in the development process to tweak layouts and responsiveness on different devices.
- https://github.com/ - Used for hosting.
- https://fonts.google.com/ - Used for importation of different font styles.
- https://www.w3.org/ - For document validation.

### External resources used

- https://stackoverflow.com/ - Used to help get the general layout for a quiz timer and then tweaked to suit how my quiz worked and reacted to the user.
- https://foolishdeveloper.com/ - Used for the general layout of a quiz and starting position for code before simplifying everything after the question layout and making it more readable and adapted to call on elements used in my quiz.
- https://www.cosmopolitan.com/uk/worklife/a32433256/best-hard-general-knowledge-quiz-questions/ - Used for quiz questions.
- https://www.welovequizzes.com/multiple-choice-quiz-questions-and-answers/#google_vignette - Used for quiz questions.
- <https://www.readersdigest.ca/culture/trivia-questions/> - Used for quiz questions.

### Media

- Both images courtesy of https://www.freepik.com/home

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
