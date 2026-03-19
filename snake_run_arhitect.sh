# python -m unittest discover -s snake/tests 2>&1 | tee snake/last_unittest_run.log
aider --model openrouter/stepfun/step-3.5-flash:free \
    --read snake/last_unittest_run.log \
    --file snake/technical_specification.md \
    --file snake/run.md \
    --file snake/python_code_style.md \
    --file "snake/progress.md" \
    --message " You are a code reviewer and a project architect. Your task is to formulate a task for the programmer. And tracking the progress of the project. You don't write code. The programmer is experienced enough to figure out how to write it correctly. Your job is to check that the programmer has done everything correctly and check the feature as implemented. And give the programmer the right task.
  Based on the file snake/technical_specification.md, highlight the next action step. This could be the implementation of a feature or the correction of a discovered bug or non-compliance with the specification file. change the file snake/technical_specification.md based on the implemented features so that it remains relevant to the state of the project.
  Based on this, create a task for the programmer in the file snake/run.md. Where the most logical action/feature that you
consider logical to implement next should be stated. This should be the simplest next action/feature written in accordance with all requirements and specifications. This file will be used by the programmer. Your task is to set a specific task for the program that it will have to implement. Keep in mind that the programmer will have access to both snake/technical_specification.md and
snake/progress.md. But the file snake/run.md will be the main file for him; he will only use the rest if he doesn’t understand
something.
  Use testing to make sure that all implemented features work. Change and edit the file snake/progress.md to mark what has already been implemented. Or make a note to yourself of what is important to pay attention to in future sessions file snake/progress.md. Your task as a reviewer is to make sure that the progress in the snake/progress.md file is marked and verified and meets the standards and requirements." \
    --notifications\
    --weak-model openrouter/mistralai/mistral-small-3.1-24b-instruct:free \
    --exit 
    # --weak-model groq/llama-3.1-8b-instant \
    # --notifications-command "" \
# python -m unittest discover -s snake/tests 2>&1 | tee snake/last_unittest_run.log
# Show system popup message (in GNOME/KDE/any notifyd)
notify-send "aider Architect session ended" "Done"
python -m unittest discover -s snake/tests
 
