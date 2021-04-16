# CreateGoogleSlidesPresentation
programmatically create a google slides presentation from jpg files or other images 

This python programs creates a google slide presentation using the API https://developers.google.com/slides/how-tos/presentations

The program must be run in the same directory where the data files are stored. Next, the file 'files' is created as follows:

ls -l *jpg | awk '{print "./" $9}' | sort > files

For the implementation, besides the API, the following guidelines have been used: 

https://stackoverflow.com/questions/60160794/getting-the-provided-image-is-in-an-unsupported-format-error-when-trying-to-in

https://stackoverflow.com/questions/56099575/how-to-fix-403-insufficient-authentication-scopes-when-uploading-file-python

When this program is run for a new application/slides-deck you MUST create new json credentials. See here https://console.cloud.google.com/apis/credentials?folder=&organizationId=&project=quickstart-1613196175693 On April 16 2021 I ran a couple of failed attempts, presumably the project name must be quickstart.

The file containing the credentials must be named credentials.json and must reside in the same working directory.

The program returns a string similar to 1nBWjxrAonni6V-7yZA6X2MuX-JzexhcsCPHP9G9xFbk which needs to be inserted into the presentation url such as https://docs.google.com/presentation/d/1nBWjxrAonni6V-7yZA6X2MuX-JzexhcsCPHP9G9xFbk/edit#slide=id.p1
