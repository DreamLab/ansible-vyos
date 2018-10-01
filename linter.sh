#!/usr/bin/env bash

for file in $(find . -name "*.yml")
do
    yamllint  $file
    rc=$?
    if [ "$rc" -ne 0 ] ; then
        exit $rc
    fi
done

echo "TEST PASSED all *.yml files are correct"

exit 0
