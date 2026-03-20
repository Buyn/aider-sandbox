python -m unittest discover -s snake/tests 2>&1 | tee snake/last_unittest_run.log
# aider --model openrouter/stepfun/step-3.5-flash:free \
aider --model openrouter/nvidia/nemotron-3-super-120b-a12b:free \
    --read snake/technical_specification.md \
    --read snake/run.md \
    --read snake/python_code_style.md \
    --read snake/last_unittest_run.log \
    --file "snake/progress.md" \
    --message "You are a programmer, file snake/run.md describes the task facing you for this session.
  If something is not clear, you can refer to the file snake/technical_specification.md with a description of the general
project specification. But the file snake/run.md is for you the Main source of truth, everything that is stated in other files and contradicts snake/run.md can be ignored.
  Use testing to make sure that all implemented features work. That mean, in the process, write tests for the features being implemented. change and edit the file snake/progress.md to mark what has already been implemented. Or make a note to yourself of what is important to pay attention to in future sessions in file snake/progress.md." \
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
