__author__ = 'TPei'
import getpass
import os



def get_file_path():
    """
    find default dayone entries folder, which is in the users' iCloud drive
    /Users/<username>/Library/Mobile Documents/<some semi-cryptic dayoneapp folder>/Documents/Journal_dayone/entries/
    :return:
    """
    username = getpass.getuser()

    file_path = "/Users/" + username + "/Library/Mobile Documents/"
    folders = os.listdir(file_path)

    for folder in folders:
        if "dayoneapp" in folder:
            file_path += folder + "/Documents/Journal_dayone/entries/"

    #if
    if os.path.isdir(file_path) and os.listdir(file_path):
        return file_path

    # no dayoneapp folder with the necessary sub-folders was found,
    # so we'll use a folder chooser dialog
    from Tkinter import Tk
    import tkFileDialog
    Tk().withdraw() # stops random empty tk root window from appearing

    # open folder chooser dialog
    filename = tkFileDialog.askdirectory()
    return filename


if __name__ == '__main__':
    print get_file_path()