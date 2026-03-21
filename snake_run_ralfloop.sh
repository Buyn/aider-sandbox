#!/bin/bash

# Function to prompt for iteration count
get_iterations() {
    read -p "Enter the number of loop iterations (default is 1): " ITERATIONS
    if [[ -z "$ITERATIONS" ]]; then
        ITERATIONS=1
    fi
    # Basic validation to ensure it's a positive integer
    if ! [[ "$ITERATIONS" =~ ^[0-9]+$ ]] || [ "$ITERATIONS" -lt 1 ]; then
        echo "Invalid input. Defaulting to 1 iteration."
        ITERATIONS=1
    fi
}

# Get the number of iterations from the user
get_iterations

echo "Starting RALF loop for $ITERATIONS iteration(s)..."

for i in $(seq 1 $ITERATIONS); do
    echo "--- Iteration $i of $ITERATIONS ---"
    
    echo "--- Running Architect phase ---"
    if [ -f "snake_run_arhitect.sh" ]; then
        bash snake_run_arhitect.sh
    else
        echo "Error: snake_run_arhitect.sh not found!"
        exit 1
    fi
    
    echo "--- Running Coder phase ---"
    if [ -f "snake_run_coder.sh" ]; then
        bash snake_run_coder.sh
    else
        echo "Error: snake_run_coder.sh not found!"
        exit 1
    fi
    
    echo "--- Iteration $i finished ---"
done

echo "RALF loop completed."
