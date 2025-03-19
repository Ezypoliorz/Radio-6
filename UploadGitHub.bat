#!/bin/bash

MESSAGE = "Upload automatique"

git add .
git commit -m "$MESSAGE"
git push origin "main"