# Email Summarizer

This project is a Python application that uses OpenAI's GPT-3 API to summarize emails and send them to a Matrix chat room. It uses the Google Mail API to retrieve emails from a Gmail account and the Matrix API to send messages to a Matrix chat room. The mails are summarized and rated using the GPT-3 API.

The project can be configured to look periodically for new mails and send the summaries depending on the importance and the configured labels. To do so, you can modify the `.env` file to include a loop that periodically retrieves new emails and sends their summaries to the Matrix chat room. You can also modify the `.env` file to adjust the rating algorithm used to rate the emails based on their importance.

## Requirements

To use this application, you will need the following:

- An OpenAI API key for accessing the GPT-3 API
- A Matrix user ID and access token for sending messages
- A Google Mail API credentials.json file like it is described in the [Google Mail API Quickstart guide](https://developers.google.com/gmail/api/quickstart/python?hl=de)
- Save the credentials.json file in src/credentials.json
- copy the example.env file to .env and fill in the variables

## Info

The bot currently seems to be working only in non encrypted matrix rooms.

At first start you need to invite the bot to a new room and the bot will save this room id in a .json. If you want to change the room you need to invite the bot to the new room and delete the .json file. This means the bot currently works only for one person. If you want to use it for multiple persons you need to change the code or work with multiple bots in multiple containers. In the future it would be nice to have a bot that can be invited to multiple rooms and can be used by multiple persons by giving the bot the required files over the chat room.

There are some weirdly formatted emails that won't work and the summary will be none.

## Quickstart

To start the program, follow these steps:

1. Clone the repository to your local machine.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Copy the `credentials.json` file to the src directory of the project.
4. Create a `.env` file in the root directory of the project with the variables found in example.env:
5. Run the program by running `python mailbot.py`.

Note: The first time you run the program, you will be asked to authorize the Google Mail API. Follow the instructions in the terminal to authorize the API.

## Usage

To use the bot, send a message to the Matrix chat room with the command `!mail`. The bot will retrieve the latest emails from your Gmail account and summarize them using the GPT-3 API. The summaries will be sent back to the chat room.

The `!mail` command can be followed by the following parameters:

- `count`: the number of emails to retrieve (default is 5)
- `positive`: a list of labels that the emails must have (default is `['INBOX', 'UNREAD']`)
- `negative`: a list of labels that the emails must not have (default is `['summarized']`)

For example, to retrieve the 10 most recent unread emails in your inbox, you can use the following command:

'' !mail count: 10 positive: ['INBOX', 'UNREAD'] ''

Note that the bot will only summarize emails that are labeled with the labels specified in the `.env` file. You can change these labels to suit your needs.

## Devcontainer

This project includes a devcontainer configuration for Visual Studio Code. To use the devcontainer, follow these steps:

1. Install [Docker](https://www.docker.com/) on your machine.
2. Install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension in Visual Studio Code.
3. Open the project in Visual Studio Code.
4. Click on the "Reopen in Container" button that appears in the bottom right corner of the window.
5. Wait for the devcontainer to build and start.
6. Open a terminal in Visual Studio Code and run `python main.py` to start the program.

That's it! You should now be able to use the program in the devcontainer.