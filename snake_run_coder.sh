python -m unittest discover -s snake/tests 2>&1 | tee snake/last_unittest_run.log
# working
# aider --model openrouter/stepfun/step-3.5-flash:free \
# aider --model openrouter/nvidia/nemotron-3-super-120b-a12b:free \
# crash
# aider --model openrouter/arcee-ai/trinity-large-preview:free \
#limit
# aider --model openrouter/meta-llama/llama-3.3-70b-instruct:free \
# aider --model openrouter/z-ai/glm-4.5-air:free \
# aider --model openrouter/qwen/qwen3-coder:free \
aider --model openrouter/stepfun/step-3.5-flash:free \
    --weak-model openrouter/nvidia/nemotron-nano-9b-v2:free \
    --read snake/technical_specification.md \
    --read snake/run.md \
    --read snake/python_code_style.md \
    --read snake/review_and_comments.md \
    --read snake/last_unittest_run.log \
    --file "snake/progress.md" \
    --message-file snake/coder_role.md \
    --notifications \
    --auto-lint \
    --test-cmd "python -m unittest discover -s snake/tests" \
    --auto-test \
    --exit 

    # --weak-model openrouter/mistralai/mistral-small-3.1-24b-instruct:free \
    # --weak-model groq/llama-3.1-8b-instant \
    # --yes-always \
    # --notifications-command "" \

python -m unittest discover -s snake/tests 2>&1 | tee snake/last_unittest_run.log
notify-send "aider Coder session ended" "Coder session is Done"
echo "Coder session is Done" >> snake/last_unittest_run.log
python -m unittest discover -s snake/tests
echo "Coder session is Done"

