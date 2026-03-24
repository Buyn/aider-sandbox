#!/usr/bin/env bash

aider --model openrouter/stepfun/step-3.5-flash:free \
    --weak-model mistral/open-mistral-7b \
    --file snake/technical_specification.md \
    --file snake/review_and_comments.md \
    --file "snake/progress.md" \
    --load snake/bugreporter_role.md \
    --notifications \
    --verbose \
    --no-auto-lint \
    --no-auto-test \

    # --architect \
    # --weak-model nvidia_nim/meta/llama3-8b-instruct \
