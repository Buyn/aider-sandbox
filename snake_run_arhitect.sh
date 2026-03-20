python -m unittest discover -s snake/tests 2>&1 | tee snake/last_unittest_run.log
aider --model openrouter/stepfun/step-3.5-flash:free \
    --read snake/last_unittest_run.log \
    --file snake/technical_specification.md \
    --file snake/run.md \
    --file snake/python_code_style.md \
    --file "snake/progress.md" \
    --message-file snake/arhitect_role.md
    --notifications\
    --weak-model openrouter/nvidia/nemotron-nano-9b-v2:free \
    --exit 

    # --weak-model groq/llama-3.1-8b-instant \
    # --weak-model openrouter/mistralai/mistral-small-3.1-24b-instruct:free \
    # --notifications-command "" \
python -m unittest discover -s snake/tests 2>&1 | tee snake/last_unittest_run.log
notify-send "aider Architect session ended" "Done"
python -m unittest discover -s snake/tests
