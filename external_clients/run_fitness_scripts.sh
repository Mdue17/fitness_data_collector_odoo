#!/bin/bash

#Activate my env if not active
source /home/mduduzi/odoo17/odoo/.venv/bin/activate

echo "Running workout_logger.py..."
#python3 workout_logger.py

echo "Waiting a few seconds before running polar simulation..."
#sleep 10

echo "Running simulated_polar_client.py..."
python3 simulated_polar_client.py

# ./run_fitness_scripts.sh
