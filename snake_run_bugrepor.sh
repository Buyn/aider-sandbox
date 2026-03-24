#!/usr/bin/env bash
# File: dynamic_aider_script_generator.sh

# --- Configuration ---
ROLE_FILE="snake/bugreporter_role.md"
OUTPUT_SCRIPT="snake/bugreport.script"

# --- Step 2: Prompt user for the actual instruction ---
echo ""
echo "Acid Burn Reporting Interface Initialized."
echo "------------------------------------------"
echo "Please enter the specific instruction/question for the AI"
# Read the entire line of input from the user
read -r USER_INPUT

# Basic input validation, just in case you're feeling lazy, Master.
if [[ -z "$USER_INPUT" ]]; then
    echo "Warning: No input provided. Creating an empty instruction block."
    USER_INPUT=""
fi

# --- Step 3: Construct the dynamic script file ---
# We pipe everything into the desired output script file.
{
    # 1. Load the role definition first. This sets the context.
    cat "$ROLE_FILE"
    echo "" # Ensure separation

    # 2. Inject the user's command as a single line, prefixed.
    # This is the payload you wanted.
    echo "/ask $USER_INPUT"
    echo "" # Ensure separation

} > "$OUTPUT_SCRIPT"

# --- Step 4: Final confirmation ---
echo "------------------------------------------"
echo "Success! Dynamic script '$OUTPUT_SCRIPT' created."
echo "Ready to be fed to the main application."
echo ""
    # --load snake/snake_run_bugrepor.script \

aider --model openrouter/stepfun/step-3.5-flash:free \
    --weak-model mistral/open-mistral-7b \
    --file snake/technical_specification.md \
    --file snake/review_and_comments.md \
    --file "snake/progress.md" \
    --load $OUTPUT_SCRIPT \
    --verbose \
    --notifications \
    --no-auto-lint \
    --no-auto-test \

    # --architect \
    # --weak-model nvidia_nim/meta/llama3-8b-instruct \
