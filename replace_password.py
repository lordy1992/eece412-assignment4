import sys
import hashlib

# Offset to the first byte of the stored SHA1 hash; it is
# 12813 in hex, so 75795 in decimal.
OFFSET_HASH_DATA = 75795

# Number of bytes that must be replaced in the file.
NUM_BYTES_HASH = 20

def change_stored_hash(filename, new_sha1_hash):
    code = None
    with open(filename, 'rb') as f:
        code = f.read()
        for i in xrange(OFFSET_HASH_DATA, OFFSET_HASH_DATA+NUM_BYTES_HASH):
            code = code[:i] + new_sha1_hash[i-OFFSET_HASH_DATA] + code[i+1:]
    with open(filename, 'wb') as f:
        f.write(code)

def main():
    filename = raw_input('Enter the name of the executable to modify: ')
    new_password = raw_input('Enter the new password to use: ')
    new_sha1 = hashlib.sha1(new_password).digest()
    change_stored_hash(filename, new_sha1)
    print "Successfully modified file to use new password."

if __name__ == '__main__':
    main()
