# MusicPlayer

I'm using a linux mint operating system.

### Install the requirements from install.sh file

        $ sh install.sh

### To run the project

        $ python3 manage.py runserver

### Object-Relational Mapper(ORM)

- To build tables from models file in app(MusicPlayer)

        $ python3 manage.py makemigrations

        $ python3 manage.py migrate

### To create super user:

- A super user is already created with username : **vasavi** password : **root**

- For creating new super user

        $ python3 manage.py createsuperuser

### I'm raising the web request from postman

- Below the examples for create, delete, update, get (CRUD) operations for AudioSystem

## Create Operation

- route : **create/\<audio_type>**
- input as JSON data format
- required method : *POST*

here, datefield is automatically taken, if any field is not mention it shows 400 BadRequests

1. created record in Songs Audio type

    ![create](https://github.com/VasaviLagishetty/MusicPlayer/blob/main/sample_outputs/create.png?raw=true)

    ![c1](https://github.com/VasaviLagishetty/MusicPlayer/blob/main/sample_outputs/c1.png?raw=true)

2. Creating record in Podcasts Audio type but *host* field is not given

    ![c2](https://github.com/VasaviLagishetty/MusicPlayer/blob/main/sample_outputs/c2.png?raw=true)




## Get Operation

- route : **get/\<audio_type>** (all audio files) or **get/\<audio_type>/\<audio-id>** (specific)
- required method : *GET*

1. Get all the audio files with audio type
        
    ![g1](https://github.com/VasaviLagishetty/MusicPlayer/blob/main/sample_outputs/g1.png?raw=true)

2. Get specific audio file from audio type
            
    ![g2](https://github.com/VasaviLagishetty/MusicPlayer/blob/main/sample_outputs/g2.png?raw=true)

## Update Operation

- route : **update/\<audio_type>/\<audio-id>**
- input as JSON data format
- required method : *PUT* or *POST*

    ![u1](https://github.com/VasaviLagishetty/MusicPlayer/blob/main/sample_outputs/u1.png?raw=true)

    ![u2](https://github.com/VasaviLagishetty/MusicPlayer/blob/main/sample_outputs/u2.png?raw=true)

    ![u3](https://github.com/VasaviLagishetty/MusicPlayer/blob/main/sample_outputs/u3.png?raw=true)

## Delete Operation

- route : **delete/\<audio_type>/\<audio-id>**
- required method : *DELETE* or *POST*

    ![d1](https://github.com/VasaviLagishetty/MusicPlayer/blob/main/sample_outputs/d1.png?raw=true)
    
    ![d2](https://github.com/VasaviLagishetty/MusicPlayer/blob/main/sample_outputs/d2.png?raw=true)

    ![d3](https://github.com/VasaviLagishetty/MusicPlayer/blob/main/sample_outputs/d3.png?raw=true)

if any wrong method is specified for request it shows as BadRequest

![wrong](https://github.com/VasaviLagishetty/MusicPlayer/blob/main/sample_outputs/wrong.png?raw=true)
