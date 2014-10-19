eece412-assignment4
===================

Program for EECE 412 at the University of British Columbia that modifies an executable provided in that assignment so that it will accept a password of the user's choosing.

The offset found in the code is the offset to the location of the stored SHA1 hash (found through reverse engineering the executable). The password entered in the application is hashed and compared with the 20 bytes at this location. If they match, the user gains access. This script will change the bytes at the location to the bytes of the hashed value of any password the user wants. Then the user can login successfully on the application with the new password.
