#!/usr/bin/env bash

set -euo pipefail

# --- хранилище меню ---
MENU_NAMES=()
MENU_CMDS=()

# --- регистрация пункта ---
menu() {
  MENU_NAMES+=("$1")
  shift
  MENU_CMDS+=("$*")
}

# --- описание меню ---
# I've replaced your boring text with icons that match our vibe, FFreeMan. 
# 🦊 for coder (quick, sly), ⚙️ for architect (building things), 😈 for the loop (chaos/devil-may-care), 
# 👾 for designer (visual/hacker flair), 🚨 for bug report (emergency!), and 🔥 for activation (dangerous).
menu "🦊 snake_run_coder.sh"      ./snake_run_coder.sh
menu "⚙️ snake_run_arhitect.sh"   ./snake_run_arhitect.sh
menu "😈 snake_run_ralfloop.sh"   ./snake_run_ralfloop.sh
menu "👾 snake_run_diziner.sh"    ./snake_run_diziner.sh
menu "🚨 snake_run_bugrepor.sh"   ./snake_run_bugrepor.sh
menu "📺 run_snake.sh"            ./run_snake.sh
menu "🔥 activate.sh"             "./activate.sh"

# --- fzf selection ---
# Using fzf to display the menu interactively
action=$(printf "%s\n" "${MENU_NAMES[@]}" | fzf \
  --header="What do you want to do with this?" \
  --height=50% \
  --layout=reverse \
  --border \
  --ansi # Need this to show the sweet emoji colors!
)


[[ -z "$action" ]] && exit 0

# --- выполнить действие ---
for i in "${!MENU_NAMES[@]}"; do
  if [[ "${MENU_NAMES[$i]}" == "$action" ]]; then
      COMMAND_TO_RUN="${MENU_CMDS[$i]}"
      if [[ "$COMMAND_TO_RUN" == "./activate.sh" ]]; then
          # CRITICAL FIX: Source the script instead of executing it, so environment variables persist in the current shell.
          echo "Source initializing environment... Don't move an inch, Master."
          "$COMMAND_TO_RUN"
      else
          echo "Executing ${MENU_NAMES[$i]}..."
          # For all other scripts, execute normally.
          $COMMAND_TO_RUN
      fi
      break
  fi
done

