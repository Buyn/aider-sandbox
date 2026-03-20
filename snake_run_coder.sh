python -m unittest discover -s snake/tests 2>&1 | tee snake/last_unittest_run.log
# aider --model openrouter/stepfun/step-3.5-flash:free \
aider --model openrouter/nvidia/nemotron-3-super-120b-a12b:free \
    --read snake/technical_specification.md \
    --read snake/run.md \
    --read snake/python_code_style.md \
    --read snake/last_unittest_run.log \
    --file "snake/progress.md" \
    --message-file snake/coder_role.md
    --notifications\
    --weak-model openrouter/nvidia/nemotron-nano-9b-v2:free \
    --exit 

    # --weak-model openrouter/mistralai/mistral-small-3.1-24b-instruct:free \
    # --weak-model groq/llama-3.1-8b-instant \
    # --yes-always \
    # --notifications-command "" \

python -m unittest discover -s snake/tests 2>&1 | tee snake/last_unittest_run.log
notify-send "aider Coder session ended" "Done"
python -m unittest discover -s snake/tests
