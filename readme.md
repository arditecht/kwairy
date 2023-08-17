# Kwairy :crystal_ball:

- Kwairy gets you perfect concoctions of data, summaries and insights that precisely answer your request.
- Get the list of SQL Queries that underlie those requests.
- No SQL knowledge needed, explore the depths of organizational data through an easy conversational interface.
- Get on-demand data-driven reports for an insider's view of complex business problems.
- Share historical conversations and present insights to coworkers with automatatically generated ppt.

### DEV SETUP INSTRUCTIONS :computer:
1. Make sure you have "docker-desktop" installed, and VSCode with "Dev-Containers" installed. 
	- This docker-desktop is for windows, but get appropriate Docker UI/Client/Daemon for your OS.
2. In VS Code, go to the lower-left corner button and go to "New Dev Container" in the prompted list.
3. Scroll a bit down and select a "Simple Debian?" image and create the container.
4. Once devcontainer workspace opens up in VSCode, Open its terminal ( ctrl + ` ) and run the following:
	- `sudo apt update`
	- `sudo apt -y upgrade`
	- `python3 --version` check the Python Version [17-08-2023: The default 3.9.x that you get with this should work fine for now.]
5. Download pip3: `sudo apt install -y python3-pip`.
6. Check if pip is working: `pip3 install numpy`.
7. There are few more subtle dependencies that run the dev setup better overall.
	- To install the extra deps., run `sudo apt install build-essential libssl-dev libffi-dev python3-dev`
8. Git comes with Debian, so just run `git clone <url of this repo>` in a folder you want as the project root.
9. Now go to that created project root folder, install the full set of python libraries needed for this application in the container:
	- run `pip3 install -r requirements.txt`
10. Before running this app on browser, create a blank `.env` file in this project/repository folder. In `.env` file, add the following
	- `OPENAI_API_KEY = <your-openai-key>`

For more details on VS Code dev-containers: https://code.visualstudio.com/docs/devcontainers/containers 