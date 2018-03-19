#!/usr/bin/env bash

set -e
set -o pipefail

if [ ! -z $APP_NAME -o ! -z $ENV_NAME -o ! -z $APP_TYPE ]; then
  ansible-playbook "ansible/launch-cfn.yml"
fi
