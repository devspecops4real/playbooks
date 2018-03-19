#!/usr/bin/env bash

set -e
set -o pipefail

export APP_NAME=$1
export ENV_NAME=$2


./scripts/build.sh

if [ -z $IGNORE_PROVISION ]; then
    ./scripts/provision.sh
else
    echo "'$APP_NAME' provision skipped."
fi

echo "'$APP_NAME' in '$ENV_NAME' complete."
