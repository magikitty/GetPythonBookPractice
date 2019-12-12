# Basic Overview of Git
Some basic pointers to get you started with using Git like a pro!

## Handy Stuff

Tab = "auto-complete if typed something"
cd = "change directory"

## FIRST-TIME SETUP
### IN TERMINAL
1. Go to project directory
2. `git init` to create (INITialise) the repository in the directory
### IN BROWSER
3. Go to GitHub website
4. Click green "New" (repository) button on left-hand side
5. Fill desired fields ([ProjectName] mandatory), click "Create repository"
### IN IDE
6. Make changes (skip if making repo from existing project)
### IN TERMINAL
7. `git remote add origin https://github.com/magikitty/[ProjectName]`
8. `git add [FilesToAdd]` (Can add multiple files at once by seperating with spaces)
9. `git commit -m [CommitMessage]`
9. `git push -u origin master`

## NORMAL PROCESS
1. Make changes
2. `git add [FilesToAdd]` (Can add multiple files at once by seperating with spaces)
3. `git commit -m [CommitMessage]`
4. `git push`