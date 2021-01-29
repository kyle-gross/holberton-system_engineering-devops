#0x01-shell_permissions

0-iam_betty 		     - changes user ID to betty
1-who_am_i  		     - prints effective UID of current user
2-groups    		     - prints groups the current user is a part of
3-new_owner 		     - changes owner of file "hello" to user "betty"
4-empty	    		     - creates empty file called "hello"
5-execute   		     - adds execute permission to the owner of the file "hello"
6-multiple_permissions 	     - adds execute permissions to owner, group owner, and read permission to others
7-everybody 		     - adds execute permissions to everybody for file "hello"
8-James_Bond		     - sets permission for file "hello" to 007
9-John_Doe		     - sets mode of file "hello" to 753
10-mirror_permissions  	     - sets mode of file "hello" to the same as "olleh"'s mode
11-directories_permissions   - changes subdirectories of current directory for owner, group owner, and 
			       all other users to execute
12-directory_permissions     - creates a directory called dir_holberton with permisssions 751
13-change_group		     - changes group owner to "holberton" for the file "hello"
14-change_owner_and_group    - changes owner to "betty" and the group owner to "holberton" for all files and
			       directories in the working directory
15-symbolic_link_permissions - changes the owner and the group owner of file "_hello" to "betty" and 
			       "holberton"
16-if_only		     - changes owner of file "hello" to "betty" only if it's owned by "guillaume"
100-Star_Wars		     - plays Star Wars episode IV
