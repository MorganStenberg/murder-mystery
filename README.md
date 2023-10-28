# Murder Mystery
Murder mystery is a text based adventure game, meant to take the user on a fun and somewhat surrealistic journey through the world that is Whodunit manor. 

You play the game as a detective arriving to solve a mysterious murder and your success depends on the choices you make. At the end of the game you are presented with facts around your chosen path in the game, to see if you are the first to take it or if others have tried it before! 


## Table of contents
- [User stories](#user-stories)
- [Strategy](#strategy)
- [Flowchart](#flowchart)
- [Features](#features)
- [Technologies](#technologies)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)

## Demo
Link to live site: https://murder-mystery-text-game-fb1e2ed36c7e.herokuapp.com/
- Insert screenshot here:

## User stories
This application is created for anybody that enjoys a good mystery and some wierd twists along the way.

- For fans of text-based adventure games, where each decision can take you down a different path.
- For fans of "Whodunit"/detective movies and games, where the plot thickens the deeper you get.

## Strategy
The strategy for developing this game was to make a fun, engaging and simple game. Where the correct choice is not always obvious for the user. With a focus on the narrative story itself, and that different parts is revealed with the different paths taken in the game. So that the user can play the game multiple times and have different experiences. 

It is also designed to be user friendly, with a simple choice-based system that takes the user through the game. 

## Flowchart
I used a flowchart to map out the different branches of the story. With some minor changes during the build process. It was very helpful in keeping track of the different endings for the different story branches. 

![Image of flowchart for the game](documentation/PP3_flowchart.png)

## Features

### Future features

## Technologies

### Coding languages
- **Python**, used for the application
- **HTML** and **CSS** for styling

### Libraries and packages
- **OS** and **Platform** for the clear_screen function
- **Time**, to delay printing of text to terminal
- **Gspread**, to use with connecting google sheet

### Other tools
- **LucidCharts,** to create the flowchart.
- **GitHub,** to host the application source code.
- **Gitpod,** to create/edit the source code.
- **Heroku,** to host the application.

## Testing

### Validating
The only errors that show up are related to the ASCII art that is used, as well as errors for visual indentation of long lines. 

### Manual testing
The game has been tested throughout the build process by running it directly in the console, this in combination with adding in print statements to see how the code progresses has helped alot in debugging amd solving problems with the code. 



## Bugs

### Problems encountered during build process

- Refactoring the main logic for the game and problems related to the refactoring. 


## Deployment

The project was deployed to [Heroku](https://www.heroku.com) using the below procedure:-    
  
- **Log in to Heroku** or create an account if required.
-
**click** the button labeled **New** from the dashboard in the top right corner, just below the header.
- From the drop-down menu **select "Create new app"**.
- **Enter a unique app name**. I used the name for the game and added "text-game" to it. 
- Once the web portal shows the green tick to confirm the name is original **select the relevant region.** In my case, I chose Europe as I am in Sweden.
- When happy with your choice of name and that the correct region is selected, **click** on the **"Create app" button**.
- This will bring you to the project "Deploy" tab. From here, navigate to the **settings tab** and scroll down to the **"Config Vars" section**. 
- **Click** the button labelled **"Reveal Config Vars"** and create config vars for CREDS and PORT.
- Scroll down to the **buildpacks section of the settings page** and click the button labeled **" add buildpack," select "Python," and click "Save Changes"**.
- **Repeat but** this time **add "node.js" instead of python**. 
   -  ***IMPORTANT*** The buildpacks must be in the correct order.
- Scroll back to the top of the settings page, and **navigate to the "Deploy" tab.**
- From the deploy tab **select Github as the deployment method**.
- **Confirm** you want to **connect to GitHub**.
- **Search** for the **repository name** and **click** the **connect** button next to the intended repository.
- From the bottom of the deploy page **select your preferred deployment type** by follow one of the below steps:  
   - Clicking either "Enable Automatic Deploys" for automatic deployment when you push updates to Github.  
   - Select the correct branch for deployment from the drop-down menu and click the "Deploy Branch" button for manual deployment. 

## Credits

- To my mentor Sandeep Aggarwal who was very helpful overall with this project and especially regarding the refactoring of the main logic for the game. 

**Story**
- The contents for the story itself was created with the help of [ChatGPT](https://chat.openai.com/), by giving it prompts regarding the outline for the story and then what the different branches should lead to. 
**Images**
- The background image for the deployed site was generated by [gencraft](https://gencraft.com/)
