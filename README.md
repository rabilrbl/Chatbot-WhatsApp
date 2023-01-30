# Chatbot-WhatsApp

Chatbot-WhatsApp is a Chatbot built using the Flask framework and Works with Whatsapp Business API. It takes messages from users and replies like a bot generated from ChatGPT. It also has the ability to generate images for messages prefixed with /image.

## Features
- Reply to messages like ChatGPT (using OpenAI API)
- Generate images for messages prefixed with /image
- Easy integration with Whatsapp Business API

### Prerequisites

- Python 3.10.x
- Flask
- WhatsApp Business API

# Deploying a Flask Application to the Cloud 

Deploying a Flask application to the cloud can be a straightforward and simple process. The following steps describe how to deploy your application.

## Prerequisites 
Before getting started, make sure you have the following:
- An account with a cloud hosting provider
- A virtual environment configured to run the Flask application

## Setting Up Environment Variables
Environment variables required for the application can be found in the `.example.env` file. Make sure to define these values before deploying the application. Once you have configured all of the environment variables, save them to a `.env` file. This file should then be added to the root of the application.

### Environment Variables Description

* *OPENAI_API_KEY* - This is the API key for accessing the OpenAI API. This is used to generate messages from the chatbot.

* *WHATSAPP_PHONE_NUMBER_ID* - This is the unique phone number ID provided by WhatsApp Business API in Facebook Developer Portal after registering the phone number.

* *WHATSAPP_API_KEY* - This is the API key for accessing the WhatsApp account. Also known as ACCESS_TOKEN in the Facebook Developer Portal.
  
* *AUTHORIZED_PHONE_NUMBER* - The phone number of the user who is authorized to send messages to the WhatsApp account. This is the phone number that will be used to send messages to the chatbot.
  
* *WHATSAPP_VERIFY_TOKEN* - This is a secret token used to authenticate the access to the chatbot.

## Note
> Your WhatsApp Business API account must be registered for webhooks. The webhook URL should be set to the URL of the deployed application with verify token same as the one defined in the environment variable `WHATSAPP_VERIFY_TOKEN`. The webhook event `messages` must be subscribed.

## Deploying
Once you have confirmed that the application runs in the local environment and that all environment variables are properly set, you are ready to deploy the application in the cloud. Using a hosting service such as Heroku, follow the provider’s documentation to deploy the application.

## Summary
Deploying a Flask application to the cloud is a relatively simple task. Start by setting up the environment variables as specified in the .example.env file, then deploy using a cloud hosting provider's documentation. Enjoy using chatbot-whatsapp!


# WhatsApp Usage

## Sending Messages
To send messages to the chatbot, send a message to the WhatsApp number associated with the chatbot. The message should be sent from the phone number specified in the environment variable `AUTHORIZED_PHONE_NUMBER`. The message should be sent in the following format:

`<message>`

## Generating Images
To generate images for messages, send a message to the WhatsApp number associated with the chatbot. The message should be sent from the phone number specified in the environment variable `AUTHORIZED_PHONE_NUMBER`. The message should be sent in the following format:

`/image <message>`

