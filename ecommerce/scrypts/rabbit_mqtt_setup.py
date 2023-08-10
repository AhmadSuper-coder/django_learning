# rabbitmqctl  this is the cli for rabbitmqtt

# to get the help about rabbitmqtt cli 
# sudo rabbitmqctl



# create user 
# rabbitmqctl add_user <username> <password>

# change the created user passowrd
# rabbitmqctl change_password <username> <new_password>

# delete the user 
# rabbitmqctl delete_user <username>

# get the list of users
# rabbitmqctl list_users

# to create new v_host 
# rabbitmqctl add_vhost <vhost_name>

# grant permission to particular for particular host 
# rabbitmqctl set_permissions -p <vhost_name> <username> ".*" ".*" ".*"

# get the list of vhost 
# rabbitmqctl list_vhosts
