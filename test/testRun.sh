#!/usr/bin/env bash

# Exit on first error
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

python3 $DIR/../generate_results_md.py -vvvv --profilesServer=$DIR/ServerProjects/uaprofiles.xml --profilesClient=$DIR/ClientProjects/uaprofiles.xml --results=$DIR/test.results.xml --selection=$DIR/test.selection.xml $DIR/../TEST.md

echo -e "======== TEST.md ==========\n"
cat $DIR/../TEST.md
echo -e "===========================\n"
