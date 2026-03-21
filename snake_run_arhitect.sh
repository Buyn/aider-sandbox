# python -m unittest discover -s snake/tests 2>&1 | tee snake/last_unittest_run.log
# стоит держать за коменченым тогда можно написать баг прямо в лог и он сразу поподёт на стол архитектору

echo "# Task:" > snake/run.md
echo "## Objective" >> snake/run.md
echo "" >> snake/run.md
echo "## Background" >> snake/run.md
echo "" >> snake/run.md
echo "## Issues to Address" >> snake/run.md
echo "" >> snake/run.md
echo "## Additional Notes" >> snake/run.md
echo "" >> snake/run.md
echo "## Referenced code quoting" >> snake/run.md
echo "" >> snake/run.md

# aider --model openrouter/nvidia/nemotron-3-super-120b-a12b:free \
aider --model openrouter/stepfun/step-3.5-flash:free \
    --weak-model openrouter/nvidia/nemotron-nano-9b-v2:free \
    --read snake/last_unittest_run.log \
    --read snake/technical_specification.md \
    --read snake/python_code_style.md \
    --file snake/run.md \
    --file snake/review_and_comments.md \
    --file "snake/progress.md" \
    --message-file snake/arhitect_role.md \
    --notifications \
    --no-auto-lint \
    --no-auto-test \
    --exit 

    # --weak-model groq/llama-3.1-8b-instant \
    # --weak-model openrouter/mistralai/mistral-small-3.1-24b-instruct:free \
    # --notifications-command "" \
python -m unittest discover -s snake/tests 2>&1 | tee snake/last_unittest_run.log
notify-send "aider Architect session ended" "Architect session is Done"
echo "Architect session is Done" >> snake/last_unittest_run.log
python -m unittest discover -s snake/tests
echo "Architect session is Done"
