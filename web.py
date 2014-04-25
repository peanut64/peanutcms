# This file is a part of PEANUTCMS
#
# (C) Copyright peanut64 <64peanuts@gmail.com>
#
# Licensed under the GNU GPL (any version you choose)
#
#######################################################

# This is the main program

#######################################################

class PRoute:
    ''' This class is the representative class for creating and managing routes.
        Routes in this content are with respect to bottlepy.
        The class creates, deletes and manages routes for the website. '''

class PConfigManager:
    ''' The PConfigManager class is a helper class that manages the configurations
        for the website. It maintains both the website configuration as found in
        the database as well as the configuration of the peanutCMS itself. '''

class PPageManager:
    ''' The Page manager manages the fetching and displaying of pages under a
        particular route. This class coordinates heavily with the PRoute class and
        consults with it every time it performs a page displaying operation. '''


class PAuthentication:
    ''' The PAuthentication class manages the authentication of users when they
        access the website. This class fetches the data from the database and checks
        for validity of credentials supplied by the user. There are 4 site authentication
        levels: 1) Anonymous, 2) User, 3) Content Manager, 4) Administrator.
        The levels are pretty self explanatory: Anonymous represents any visitor to
        the site that has not logged in. Users are those who have logged in, but have
        only limited ability to interact with the website, although they have more
        rights than Anonymous visitors. The Content managers can create content on the
        site and upload files. The Administrator has all the rights and can do anything
        he/she wants. '''


class PTheming:
    ''' This class manages the themes used on the website in coordination with the Bottle
        template system. This just makes it simple to handle embedding of the content to
        the page with the template. '''


class PFileManager:
    ''' The PFileManager class represents the system that manages the upload, storage and
        retrieval of files and content by the content managers and users(limited). '''


class PContentManager:
    ''' This class serves the required content with regards to the templates/themes of the
        site. '''


class PUserInput:
    ''' Content cleaner for the websites. Performs formatting of user input to clean it.
        Removes potentially dangerous code embedded in comment, etc. '''
