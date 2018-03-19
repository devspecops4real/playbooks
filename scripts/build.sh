#!/usr/bin/env bash

set -e
set -o pipefail

if [ ! -z $APP_NAME -o ! -z $ENV_NAME ]; then
    INVENTORY_FILE_PATH="share/inventories/${APP_NAME}.${ENV_NAME}.hosts"

    # Build the environment inventory file.
    ansible-playbook "ansible/launch.yml" # To the moon!
    ansible-playbook -i "${INVENTORY_FILE_PATH}" "ansible/finalize.yml"
fi
