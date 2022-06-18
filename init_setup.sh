# Shell script to setup the environment for the init script

# Set up the environment
echo "Setting up the environment"
echo "running Makefile"
# Make file contains all the required commands to setup the environment
make activate
make setup