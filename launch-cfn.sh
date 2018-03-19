#!/usr/bin/env bash

set -e
set -o pipefail

export APP_NAME=$1
export APP_TYPE=$2
export ENV_NAME=$3

./scripts/build-cfn.sh
