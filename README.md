**[See my other projects](https://github.com/mtomzynski?tab=repositories)**

# Online Radio
Polish online radio - Radio Nowy Świat

## Table of contents
* [General Information](#general-information)
* [Goal of the Project](goal-of-the-project)
* [Technology](#technology)
* [Implementation](#implementation)

## General Information
Source of data: https://nowyswiat.online/

Radio Nowy Świat was launched in 2020. It is polish online radio station.
Radio doesn't provide API. However, data (currently played song) can be get on radio's subpage that I have found once inspecting the code of website.

## Goal of the Project
The project has an educational purpose.
There are two goals:
1. Read song titles from radio's website and save it to the file. (POC already working - code will be delivered soon)
2. Load saved song titles and add them to dedicated Spotify playlist. (to be done)

## Technology
In the project there were used:
* Python 3
* Amazon Web Services
* Spotify Web API (to be done)

## Implementation
Note: for now I have prepared the Python script running on AWS E2C micro machine. I run .py script in the backgroud. However, this is only just for POC.
In the final solution, I would like to run script on schedule (probably using CRON).

I'm working on PDF file where I'll present and describe details of the project.