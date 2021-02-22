# CreateGoogleSlidesPresentation
programmatically create a google slides presntation from jpg files or other images 

This python programs creates a google slide presentation using the API https://developers.google.com/slides/how-tos/presentations

The data is created as follows:

ls -l *jpg | awk '{print "./" $9}' | sort > files

Besides the API, the following guidelines have been used: 

https://stackoverflow.com/questions/60160794/getting-the-provided-image-is-in-an-unsupported-format-error-when-trying-to-in

https://stackoverflow.com/questions/56099575/how-to-fix-403-insufficient-authentication-scopes-when-uploading-file-python
