import random
import os
import subprocess

#diskutil eraseDisk FILE_SYSTEM DISK_NAME DISK_IDENTIFIER
#0:      GUID_partition_scheme                         500.3 GB   disk0
#   1:             Apple_APFS_ISC ⁨⁩                        524.3 MB   disk0s1
 #  2:                 Apple_APFS ⁨Container disk3⁩         494.4 GB   disk0s2
  # 3:        Apple_APFS_Recovery ⁨⁩                        5.4 GB     disk0s3
##

command = 'diskutil list'
os.system(command)