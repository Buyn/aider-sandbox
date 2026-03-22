
notify-send "aider Coder session Started" "Coder session is Started"
echo "Coder session is Started"
python -m unittest discover -s snake/tests 2>&1 | tee snake/last_unittest_run.log
echo "Coder session is Starting" >> snake/last_unittest_run.log
# crash
# aider --model openrouter/arcee-ai/trinity-large-preview:free \
# aider --model openrouter/openai/gpt-oss-120b:free \
#limit
# aider --model openrouter/meta-llama/llama-3.3-70b-instruct:free \
# aider --model openrouter/z-ai/glm-4.5-air:free \
# aider --model openrouter/qwen/qwen3-coder:free \
# working
# aider --model openrouter/nvidia/nemotron-3-super-120b-a12b:free \
# aider --model openrouter/stepfun/step-3.5-flash:free \

# aider --model gemini/gemini-flash-lite-latest \

aider --model openrouter/stepfun/step-3.5-flash:free \
    --weak-model nvidia_nim/meta/llama3-8b-instruct \
    --read snake/technical_specification.md \
    --read snake/run.md \
    --read snake/python_code_style.md \
    --read snake/last_unittest_run.log \
    --file "snake/progress.md" \
    --message-file snake/coder_role.md \
    --notifications \
    --auto-lint \
    --test-cmd "python -m unittest discover -s snake/tests" \
    --auto-test \
    --exit 

    # --weak-model openrouter/nvidia/nemotron-nano-9b-v2:free \
    # --weak-model openrouter/mistralai/mistral-small-3.1-24b-instruct:free \
    # --weak-model groq/llama-3.1-8b-instant \
    # --yes-always \
    # --notifications-command "" \
    # --read snake/review_and_comments.md \

python -m unittest discover -s snake/tests 2>&1 | tee snake/last_unittest_run.log
notify-send "aider Coder session ended" "Coder session is Done"
echo "Coder session is Done" >> snake/last_unittest_run.log
python -m unittest discover -s snake/tests
echo "Coder session is Done"

